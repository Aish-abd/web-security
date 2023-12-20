from django.urls import path
from . import views
from django.contrib.auth import views as view_auth
from .forms import FuncLogin


app_name='main'

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('logout/', views.viewlogout, name='logout'),
    path('newlogin/',views.otp_view,name='newlogin'),
    path('verify/',views.verification,name='verify')
    
    
]
