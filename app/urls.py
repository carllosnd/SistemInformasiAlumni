from django.urls import path
from .views import beranda, visimisi, strorg, dataalumni, agenda, pengumuman, loker,  donasi
from .views import register, login, base, logout_user
# from .views import ajukandata
# from .views import register, login, logout_user, base
# from .views import base

urlpatterns = [
    #Landing Page
    path('',beranda,name="beranda"),
    path('visimisi/',visimisi,name='visimisi'),
    path('strorg/',strorg,name='strorg'),
    path('dataalumni/',dataalumni,name='dataalumni'),
    path('agenda',agenda,name='agenda'),
    path('pengumuman/',pengumuman,name='pengumuman'),
    path('loker/',loker,name='loker'),
    path('donasi/',donasi,name='donasi'),
    
    #Authentication
    path('register/', register, name='register'),
    # path('verification/<uidb64>/<token>', verification, name='verification'),
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout'),
    
    #Template
    path('base',base,name="base"),
    
    #User
    # path('ajukandata',ajukandata,name='ajukandata')
    
]
