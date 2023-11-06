import datetime
import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from app.forms import RegisterUserForm, ReplyForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Agenda, BincangAlumni, DataAlumni, Loker, Pengumuman, Reply, UserProfile
from django.core.paginator import Paginator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.db.models import Q

def header(request):
    return render(request, 'layout/header.html')

def footer(request):
    return render(request, 'layout/footer.html')

def sigin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                # Pengguna adalah superuser, arahkan ke halaman baseadmin
                login(request, user)
                return redirect('homeadmin')
            else : 
                login(request, user)
                return redirect('homeuser')
        else:
            try:
                user = User.objects.get(username=username)
                if not user.check_password(password):
                    messages.error(request, "Password yang anda masukkan salah.")
                else:
                    messages.error(request, "Silahkan aktivasi akun anda terlebih dahulu!")
            except User.DoesNotExist:
                messages.error(request, "Akun tidak ditemukan.")
            return redirect('login')

    else:
        return render(request, 'auth/login.html', {})

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.success(request, 'Berhasil logout')
    return redirect('/login')


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Aktivasi Akun Anda'
            message = render_to_string('auth/verify.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request, ("Berhasil mendaftar! Silahkan periksa email anda untuk aktivasi akun!"))
            return redirect('login')
        else:
            # Jika formulir tidak valid, pesan kesalahan akan ditampilkan
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f" {error}")
    else:
        form = RegisterUserForm()
    return render(request, 'auth/register.html', {'form': form, })

def verification(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Akun anda berhasil di aktivasi, silahkan login!')
        return redirect('/login')
    else:
        messages.error(request, 'Link aktivasi tidak valid')
        return redirect('login')
    
# Create your views here.

def beranda(request):
    dataagenda = Agenda.objects.all().order_by('dateagenda')
    datapengumuman = Pengumuman.objects.all().order_by('datepengumuman')
    dataloker = Loker.objects.all().order_by('dateloker')
    context = {
        'dataagenda' : dataagenda,
        'datapengumuman' : datapengumuman,
        'dataloker' : dataloker
    }
    return render(request, 'landingpage/beranda.html', context)

def informasi(request):
    dataagenda = Agenda.objects.all().order_by('dateagenda')
    datapengumuman = Pengumuman.objects.all().order_by('datepengumuman')
    dataloker = Loker.objects.all().order_by('dateloker')
    context = {
        'dataagenda' : dataagenda,
        'datapengumuman' : datapengumuman,
        'dataloker' : dataloker
    }
    return render(request, 'landingpage/informasi.html', context)

def visimisi(request):
    return render(request, 'landingpage/tentangkami/visimisi.html')


def strorg(request):
    return render(request, 'landingpage/tentangkami/strukturorganisasi.html')


def alumni(request):
    if 'search' in request.GET:
        search = request.GET['search']
        multiple_q = Q(Q(nama__icontains=search) | Q(nim__icontains=search))
        dataalumni = DataAlumni.objects.filter(multiple_q)
    else :
        dataalumni = DataAlumni.objects.filter(status=True).order_by('nama')
    paginator = Paginator(dataalumni, 6)  # Membagi data menjadi 10 item per halaman
    page = request.GET.get('page')
    dataalumni = paginator.get_page(page)
    context = {
        'dataalumni' : dataalumni
    }
    return render(request, 'landingpage/alumni/alumni.html', context)

def detailalumni(request, nim):
    dataalumni = DataAlumni.objects.get(nim=nim)
    context = {
        'dataalumni' : dataalumni
    }
    return render(request, 'landingpage/alumni/detailalumni.html', context)


def agenda(request):
    return render(request, 'landingpage/informasi/agenda.html')

def detailagenda(request, idagenda):
    dataagenda = Agenda.objects.get(idagenda=idagenda)
    context = {
        'dataagenda' : dataagenda
    }
    return render(request, 'landingpage/informasi/detailagenda.html', context)

def pengumuman(request):
    return render(request, 'landingpage/informasi/pengumuman.html')

def detailpengumuman(request, idpengumuman):
    datapengumuman = Pengumuman.objects.get(idpengumuman=idpengumuman)
    context = {
        'datapengumuman' : datapengumuman
    }
    return render (request, 'landingpage/informasi/detailpengumuman.html', context)

def loker(request):
    return render(request, 'landingpage/informasi/loker.html')

def detailloker(request, idloker):
    dataloker = Loker.objects.get(idloker=idloker)
    context ={
        'dataloker' : dataloker
    }
    return render (request, 'landingpage/informasi/detailloker.html', context)

def donasi(request):
    return render(request, 'landingpage/donasi.html')


@login_required(login_url='login')
def ajukandata(request):
    user = request.user
    if DataAlumni.objects.filter(user=user).exists():
        messages.error(request, 'Anda sudah mengajukan data.')
        return redirect('/homeuser')  # Ubah ini sesuai dengan URL yang sesuai
    else:
        username = user.username
        return render(request, 'user/ajukandata.html', {'username': username})

def postajukandata(request):
    nim = request.POST['nim']
    nama = request.POST['nama']
    alamat = request.POST['alamat']
    email = request.POST['email']
    nohp = request.POST['nohp']
    thnlulus = request.POST['thnlulus']
    prodi = request.POST['prodi']
    instansi = request.POST['instansi']
    jabatan = request.POST['jabatan']
    gambar = request.FILES['gambar']
    grup = request.POST['grup']
    linkedin = request.POST['linkedin']
    instagram = request.POST['instagram']
    facebook = request.POST['facebook']

    if DataAlumni.objects.filter(nim=nim).exists():
        messages.error(request, 'Nim yang di input sudah ada')
        return redirect('/ajukandata')
    else:
        dataalumni = DataAlumni(
            nim=nim,
            nama=nama,
            alamat=alamat,
            email=email,
            nohp=nohp,
            thnlulus=thnlulus,
            prodi=prodi,
            instansi=instansi,
            jabatan=jabatan,
            gambar=gambar,
            grup=grup,
            linkedin = linkedin,
            instagram = instagram,
            facebook = facebook,
            user=request.user 
        )
        dataalumni.status = False
        dataalumni.save()
        messages.success(request, 'Data berhasil di ajukan, silahkan menunggu verifikasi dari admin')
    return redirect('/homeuser')

@login_required(login_url='login')
def updatedata(request, nim):
    user_data = DataAlumni.objects.get(nim=nim)
    context = {
        'user_data' : user_data
    }
    return render (request, 'user/updatedata.html', context)

def postupdatedata(request):
    nim = request.POST['nim']
    
    user_data = DataAlumni.objects.get(nim=nim)
    if len(request.FILES) != 0:
        if len(user_data.gambar) > 0:
            os.remove(user_data.gambar.path)
        user_data.gambar = request.FILES['gambar']
    user_data.nama = request.POST.get('nama')
    user_data.alamat = request.POST.get('alamat')
    user_data.email = request.POST.get('email')
    user_data.nohp = request.POST.get('nohp')
    user_data.thnlulus = request.POST.get('thnlulus')
    user_data.prodi = request.POST.get('prodi')
    user_data.instansi = request.POST.get('instansi')
    user_data.jabatan = request.POST.get('jabatan')
    user_data.grup = request.POST.get('grup')
    user_data.linkedin = request.POST.get('linkedin')
    user_data.instagram = request.POST.get('instagram')
    user_data.facebook = request.POST.get('facebook')
    user_data.save()
    messages.success(request, 'Data anda berhasil diperbaharui')
    return redirect('/homeuser')

@login_required(login_url='login')
def verifikasi(request):
    if request.method == 'GET':
        unverified_data = DataAlumni.objects.filter(status=False)
        return render(request, 'admin/alumni/verifikasidata.html', {'unverified_data': unverified_data})
    elif request.method == 'POST':
        # Lakukan verifikasi data dan perbarui status data yang diverifikasi
        nim = request.POST.get('nim')
        dataalumni = DataAlumni.objects.get(nim=nim)
        dataalumni.status = True
        dataalumni.save()
        messages.success(request, 'Data Alumni Berhasil Di Verifikasi')
        return redirect('/dataalumni')

def tolakverif(request, nim):
    dataalumni = DataAlumni.objects.get(nim=nim)
    context = {
        'dataalumni' : dataalumni
    }
    return render(request, 'admin/alumni/tolakverifikasi.html', context)

def posttolakverif(request, nim):
    DataAlumni.objects.get(nim=nim).delete()
    return redirect('/verifikasi')

@login_required(login_url='login')
def dataalumni(request):
    if 'search' in request.GET:
        search = request.GET['search']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(nim__icontains=search) | Q(nama__icontains=search))
        dataalumni = DataAlumni.objects.filter(multiple_q)
    else :
        dataalumni = DataAlumni.objects.filter(status=True).order_by('nama')
    page_number = request.GET.get('page')
    items_per_page = 10
    paginator = Paginator(dataalumni, items_per_page)
    page = paginator.get_page(page_number)
    context = {
        'dataalumni': page
    }
    return render(request, 'admin/alumni/dataalumni.html', context)

def deletealumni(request, nim):
    dataalumni = DataAlumni.objects.get(nim=nim)
    context = {
        'dataalumni' : dataalumni
    }
    return render(request, 'admin/alumni/deletealumni.html', context)

def postdeletealumni(request, nim):
    DataAlumni.objects.get(nim=nim).delete()
    messages.success(request, 'Data Berhasil Di Hapus')
    return redirect('/dataalumni')

@login_required(login_url='login')
def homeadmin(request):
    dataagenda = Agenda.objects.count()
    datapengumuman = Pengumuman.objects.count()
    dataloker = Loker.objects.count()
    dataalumni = DataAlumni.objects.filter(status=True).count()
    verifikasi = DataAlumni.objects.filter(status=False).count()
    user = request.user
    context = {
        'dataagenda' : dataagenda,
        'datapengumuman' : datapengumuman,
        'dataloker' : dataloker,
        'dataalumni' :dataalumni,
        'verifikasi' : verifikasi,
        'user' : user
    }
    return render(request, 'admin/beranda.html', context)

def addagenda(request):
    return render(request,'admin/agenda/tambahagenda.html')

def postagenda(request):
    namaagenda = request.POST['namaagenda']
    dateagenda = request.POST['dateagenda']
    deskripsiagenda = request.POST['deskripsiagenda']
    dataagenda = Agenda(
        namaagenda = namaagenda,
        dateagenda = dateagenda,
        deskripsiagenda = deskripsiagenda 
    )
    dataagenda.save()
    messages.success(request, 'Agenda baru berhasil ditambahkan')
    return redirect('/dataagenda')

@login_required(login_url='login')
def dataagenda(request):
    dataagenda = Agenda.objects.all().order_by('idagenda')
    page_number = request.GET.get('page')
    items_per_page = 5
    paginator = Paginator(dataagenda, items_per_page)
    page = paginator.get_page(page_number)
    context = {
        'dataagenda' : page
    }
    return render(request, 'admin/agenda/dataagenda.html', context)

def updateagenda(request, idagenda):
    dataagenda = Agenda.objects.get(idagenda=idagenda)
    context = {
        'dataagenda' : dataagenda
    }
    return render(request, 'admin/agenda/updateagenda.html', context)

def postupdateagenda(request):
    idagenda = request.POST['idagenda']
    namaagenda = request.POST['namaagenda']
    dateagenda = request.POST['dateagenda']
    deskripsiagenda = request.POST['deskripsiagenda']
    
    dataagenda = Agenda.objects.get(idagenda=idagenda)
    
    dataagenda.idagenda = idagenda
    dataagenda.namaagenda = namaagenda
    dataagenda.dateagenda = dateagenda
    dataagenda.deskripsiagenda = deskripsiagenda
    dataagenda.save()
    messages.success(request, 'Agenda Berhasil Diubah')
    return redirect('/dataagenda')

def deleteagenda(request, idagenda):
    dataagenda = Agenda.objects.get(idagenda=idagenda)
    context = {
        'dataagenda': dataagenda
    }
    return render(request, 'admin/agenda/deleteagenda.html', context)


def postdeleteagenda(request, idagenda):
    Agenda.objects.get(idagenda=idagenda).delete()
    messages.success(request, 'Agenda Berhasil Dihapaus')
    return redirect('/dataagenda')

#Pengumuman 

def addpengumuman(request):
    return render (request,'admin/pengumuman/tambahpengumuman.html')

def postpengumuman(request):
    namapengumuman = request.POST['namapengumuman']
    deskripsipengumuman = request.POST['deskripsipengumuman']
    filepengumuman = request.FILES['filepengumuman']
    
    datapengumuman = Pengumuman(
        namapengumuman = namapengumuman ,
        datepengumuman = datetime.date.today(),
        deskripsipengumuman = deskripsipengumuman,
        filepengumuman = filepengumuman
    )
    datapengumuman.save()
    messages.success(request, 'Pengumuman berhasil di tambahkan')
    return redirect('/datapengumuman')

@login_required(login_url='login')
def datapengumuman(request):
    datapengumuman = Pengumuman.objects.all().order_by('idpengumuman')
    page_number = request.GET.get('page')
    items_per_page = 5
    paginator = Paginator(datapengumuman, items_per_page)
    page = paginator.get_page(page_number)
    context = {
        'datapengumuman' : page
    }
    return render(request, 'admin/pengumuman/datapengumuman.html', context)

def updatepengumuman(request, idpengumuman):
    datapengumuman = Pengumuman.objects.get(idpengumuman=idpengumuman)
    context = {
        'datapengumuman' : datapengumuman
    }
    return render (request, 'admin/pengumuman/updatepengumuman.html', context)

def postupdatepengumuman(request):
    idpengumuman = request.POST['idpengumuman']
    
    datapengumuman = Pengumuman.objects.get(idpengumuman=idpengumuman)
    if len(request.FILES) != 0:
        if len(datapengumuman.filepengumuman) > 0:
            os.remove(datapengumuman.filepengumuman.path)
        datapengumuman.filepengumuman = request.FILES['filepengumuman']
    datapengumuman.namapengumuman = request.POST.get('namapengumuman')
    datapengumuman.datepengumuman = datetime.date.today()
    datapengumuman.deskripsipengumuman = request.POST.get('deskripsipengumuman')
    datapengumuman.save()
    messages.success(request, 'Pengumuman berhasil diubah')
    return redirect('/datapengumuman')

def deletepengumuman(request, idpengumuman):
    datapengumuman = Pengumuman.objects.get(idpengumuman=idpengumuman)
    context = {
        'datapengumuman': datapengumuman
    }
    return render(request, 'admin/pengumuman/deletepengumuman.html', context)

def postdeletepengumuman(request, idpengumuman):
    Pengumuman.objects.get(idpengumuman=idpengumuman).delete()
    messages.success(request, 'Pengumuman berhasil dihapus')
    return redirect('/datapengumuman')

#Lowongan Pekerjaan

def addloker(request):
    return render(request, 'admin/loker/tambahloker.html')

def postloker(request):
    namaloker = request.POST['namaloker']
    instansi = request.POST['instansi']
    fileloker = request.FILES['fileloker']
    
    dataloker = Loker(
        dateloker = datetime.date.today(),
        namaloker = namaloker,
        instansi = instansi,
        fileloker = fileloker
    )
    dataloker.save()
    messages.success(request, 'Loker berhasil di tambahkan')
    return redirect('/dataloker')

@login_required(login_url='login')
def dataloker(request):
    dataloker = Loker.objects.all().order_by('idloker')
    page_number = request.GET.get('page')
    items_per_page = 5
    paginator = Paginator(dataloker, items_per_page)
    page = paginator.get_page(page_number)
    context = {
        'dataloker' : page
    }
    return render(request, 'admin/loker/dataloker.html', context)

def updateloker(request, idloker):
    dataloker = Loker.objects.get(idloker=idloker)
    context = {
        'dataloker' : dataloker
    }
    return render (request, 'admin/loker/updateloker.html', context)

def postupdateloker(request):
    idloker = request.POST['idloker']
    
    dataloker = Loker.objects.get(idloker=idloker)
    
    if len(request.FILES) != 0:
        if len(dataloker.fileloker) > 0:
            os.remove(dataloker.fileloker.path)
        dataloker.fileloker = request.FILES['fileloker']
    dataloker.dateloker = datetime.date.today()
    dataloker.namaloker = request.POST.get('namaloker')
    dataloker.instansi = request.POST.get('instansi')
    dataloker.save()
    messages.success(request, 'Loker berhasil di perbaharui')
    return redirect('/dataloker')

def deleteloker(request, idloker):
    dataloker = Loker.objects.get(idloker=idloker)
    context = {
        'dataloker' : dataloker
    }
    return render(request, 'admin/loker/deleteloker.html', context)


def postdeleteloker(request, idloker):
    Loker.objects.get(idloker=idloker).delete()
    messages.success(request, 'Loker Berhasil Dihapus')
    return redirect('/dataloker')

def addadmin(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username yang Anda masukkan sudah ada, silakan masukkan username yang lain')
            return redirect('/addadmin')
        else:
            # Membuat objek User baru sebagai admin
            dataadmin = User(
                first_name=name,
                username=username
            )
            dataadmin.set_password(password)  # Mengatur password dengan benar
            dataadmin.is_staff = True  # Menandai sebagai staff
            dataadmin.save()
            
            messages.success(request, 'Admin berhasil ditambahkan')
        
        return redirect('/dataadmin')
    else:
        return render(request, 'admin/tambahadmin.html', {})

def deleteadmin(request, id):
    dataadmin = User.objects.get(id=id)
    context = {
        'dataadmin' : dataadmin
    }
    return render(request, 'admin/deleteadmin.html', context)

def postdeleteadmin(request, id):
    User.objects.get(id=id).delete()
    messages.success(request, 'Admin berhasil di hapus')
    return redirect('/dataadmin')

@login_required(login_url='login')
def dataadmin(request):
    dataadmin = User.objects.filter(is_staff=True).order_by('id')
    context = {
        'dataadmin' : dataadmin
    }
    return render(request, 'admin/admin.html', context)

@login_required(login_url='login')
def homeuser(request):
    user = request.user
    user_data = DataAlumni.objects.filter(user=request.user) 
    context = {
        'user' : user,
        'user_data' : user_data
    }
    return render(request, 'user/home.html', context)

@login_required(login_url='login')
def bincangalumni(request):
    # dataalumni = DataAlumni.objects.get(user=request.user)
    datapesan = BincangAlumni.objects.all().order_by('-date')
    datareply = Reply.objects.all().order_by('date_reply')
    context = {
        'datapesan' : datapesan,
        'datareply' : datareply,
        'dataalumni' : dataalumni
    }
    return render(request, 'user/bincangalumni.html', context)

def addmessage(request):
    pesan = request.POST['pesan']
    
    datapesan = BincangAlumni (
        pesan = pesan,
        date = datetime.date.today(),
        user = request.user
    )
    datapesan.save()
    messages.success(request, 'Pesan Anda Berhasil Dikirim')
    return redirect('bincangalumni')

def reply(request, id):
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            message = BincangAlumni.objects.get(pk=id)
            reply = form.cleaned_data['reply']
            Reply.objects.create(message=message, user=request.user, reply=reply, date_reply=datetime.date.today())
            messages.success(request, 'Balasan anda berhasil terkirim')
    return redirect('bincangalumni') 

# @login_required(login_url='login')
# def profile(request):
#     user = request.user
#     profileimage = UserProfile.objects.filter(user=user)
#     context = {
#         'user' : user,
#         'profileimage' : profileimage
#     }
#     return render(request, 'user/profile.html', context)

# def addprofileimage(request):
#     image = request.FILES['image']
    
#     profileimage = UserProfile(
#         image = image,
#         user = request.user
#     )
#     profileimage.save()
#     messages.success(request, 'Foto berhasil ditambah')
#     return redirect('profile')