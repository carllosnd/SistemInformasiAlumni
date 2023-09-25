from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from app.forms import RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			# login(request, user)
			return redirect('base')
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login')	

	else:
		return render(request, 'auth/login.html', {})

def logout_user(request):
	# logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('beranda')


def register(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			# login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('login')
	else:
		form = RegisterUserForm()

	return render(request, 'auth/register.html', {'form':form,})

# Create your views here.
def beranda(request):
    return render(request,'landingpage/beranda.html')

def visimisi(request):
    return render(request,'landingpage/tentangkami/visimisi.html')

def strorg(request):
    return render(request,'landingpage/tentangkami/strukturorganisasi.html')

def dataalumni(request):
    return render(request,'landingpage/dataalumni.html')

def agenda(request):
    return render(request,'landingpage/informasi/agenda.html')

def pengumuman(request):
    return render(request,'landingpage/informasi/pengumuman.html')

def loker(request):
    return render(request,'landingpage/informasi/loker.html')

def donasi(request):
    return render(request,'landingpage/donasi.html')

def base(request):
    return render(request,'base.html')

# def ajukandata(request):
#     return render(request,'user/ajukandata.html')