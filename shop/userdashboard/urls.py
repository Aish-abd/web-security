from django.urls import path

from . import views

app_name='userdashboard'

urlpatterns = [
    path('',views.index,name='index'),
]
