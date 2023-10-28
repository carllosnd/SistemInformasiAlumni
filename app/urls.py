from django.urls import path
from django.contrib.auth import views as auth_views
from .views import beranda, visimisi, strorg, alumni, detailalumni, agenda, pengumuman, loker,  donasi, detailagenda, detailpengumuman, detailloker, informasi
from .views import register, sigin, logout_user, verification
from .views import ajukandata, postajukandata, homeuser, updatedata, postupdatedata, bincangalumni, addmessage, reply
from .views import header
from .views import dataalumni, deletealumni, postdeletealumni, homeadmin, footer, verifikasi, tolakverif, posttolakverif, addadmin, dataadmin, deleteadmin, postdeleteadmin
from .views import dataagenda, addagenda, postagenda, deleteagenda, postdeleteagenda, updateagenda, postupdateagenda
from .views import datapengumuman, addpengumuman, postpengumuman, updatepengumuman, postupdatepengumuman, deletepengumuman, postdeletepengumuman 
from .views import dataloker, addloker, postloker, updateloker, postupdateloker, deleteloker, postdeleteloker
# addagenda, addpengumuman, addloker

urlpatterns = [
    #Landing Page
    path('',beranda,name="beranda"),
    path('visimisi/',visimisi,name='visimisi'),
    path('strorg/',strorg,name='strorg'),
    path('alumni',alumni,name='alumni'),
    path('detailalumni/<str:nim>',detailalumni,name='detailalumni'),
    path('agenda',agenda,name='agenda'),
    path('detailagenda/<str:idagenda>',detailagenda,name='detailagenda'),
    path('pengumuman/',pengumuman,name='pengumuman'),
    path('detailpengumuman/<str:idpengumuman>',detailpengumuman,name='detailpengumuman'),
    path('loker/',loker,name='loker'),
    path('detailloker/<str:idloker>',detailloker,name='detailloker'),
    path('donasi/',donasi,name='donasi'),
    path('informasi',informasi,name='informasi'),
    
    #Authentication
    path('register/', register, name='register'),
    path('verification/<uidb64>/<token>/', verification, name='verification'),
    path('login/', sigin, name='login'),
    path('logout/', logout_user, name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="auth/resetpassword.html"), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name="auth/resetpasswordmessage.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="auth/resetpasswordconfirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="auth/resetpassworddone.html"), name='password_reset_complete'),

    
    #Template
    path('footer',footer,name='footer'),
    path('header',header,name='header'),
    
    #User
    path('ajukandata',ajukandata,name='ajukandata'),
    path('postajukandata',postajukandata,name='postajukandata'),
    path('homeuser',homeuser,name='homeuser'),
    path('updatedata/<str:nim>',updatedata,name='updatedata'),
    path('postupdatedata',postupdatedata,name='postupdatedata'),
    path('bincangalumni',bincangalumni,name='bincangalumni'),
    path('addmessage',addmessage,name='addmessage'),
    path('reply/<int:id>',reply,name='reply'),
    # path('postreply',postreply,name='postreply'),
    
    #Admin
    path('dataalumni/',dataalumni,name='dataalumni'),
    path('deletealumni/<str:nim>', deletealumni, name='deletealumni'),
    path('postdeletealumni/<str:nim>',postdeletealumni,name='postdeletealumni'),
    path('homeadmin',homeadmin,name='homeadmin'),
    path('verifikasi',verifikasi,name='verifikasi'),
    path('tolakverif/<str:nim>',tolakverif,name='tolakverif'),
    path('posttolakverif/<str:nim>',posttolakverif,name='posttolakverif'),
    path('addadmin',addadmin,name='addadmin'),
    path('deleteadmin/<str:id>',deleteadmin,name='deleteadmin'),
    path('postdeleteadmin/<str:id>',postdeleteadmin,name='postdeleteadmin'),
    
    # path('postadmin',postadmin,name='postadmin'),
    path('dataadmin',dataadmin,name='dataadmin'),
    #Admin => CRUD Agenda
    path('dataagenda',dataagenda,name='dataagenda'),
    path('addagenda',addagenda,name='addagenda'),
    path('postagenda',postagenda,name='postagenda'),
    path('deleteagenda/<str:idagenda>',deleteagenda,name='deleteagenda'),
    path('postdeleteagenda/<str:idagenda>',postdeleteagenda,name='postdeleteagenda'),
    path('updateagenda/<str:idagenda>',updateagenda,name='updateagenda'),
    path('postupdateagenda',postupdateagenda,name='postupdateagenda'),
    #Admin => CRUD Pengumuman
    path('datapengumuman',datapengumuman,name='datapengumuman'),
    path('addpengumuman',addpengumuman,name='addpengumuman'),
    path('postpengumuman',postpengumuman,name='postpengumuman'),
    path('updatepengumuman/<str:idpengumuman>',updatepengumuman,name='updatepengumuman'),
    path('postupdatepengumuman',postupdatepengumuman,name='postupdatepengumuman'),
    path('deletepengumuman/<str:idpengumuman>',deletepengumuman,name='deletepengumuman'),
    path('postdeletepengumuman/<str:idpengumuman>',postdeletepengumuman,name='postdeletepengumuman'),
    #Admin => CRUD LOKER
    path('dataloker',dataloker,name='dataloker'),
    path('addloker',addloker,name='addloker'),
    path('postloker',postloker,name='postloker'),
    path('updateloker/<str:idloker>',updateloker,name='updateloker'),
    path('postupdateloker',postupdateloker,name='postupdateloker'),
    path('deleteloker/<str:idloker>',deleteloker,name='deleteloker'),
    path('postdeleteloker/<str:idloker>',postdeleteloker,name='postdeleteloker')
    
    
    
]

