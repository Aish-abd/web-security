from django.urls import path

from . import views

app_name='items'
urlpatterns=[

    path('new/',views.newItem,name='newitem'),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/edit/',views.edit,name='edit'),
    
]