from django.urls import path,include

from . import views
from routing import websocket_urlpattern
urlpatterns = [
    path('', views.homepage, name='index'),
    path('text/', views.text ,name="home"),
    path('text/chat', views.texting ,name="texting"),
    path('text/ip', views.ip_check ,name="ip"),
    path('', include('websocket_urlpattern'))
]