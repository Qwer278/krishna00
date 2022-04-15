from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('text/', views.text ,name="home"),
    path('text/chat', views.texting ,name="texting"),
    path('text/ip', views.ip_check ,name="ip"),
    # path('<str:room_name>/', views.room, name='room')
]