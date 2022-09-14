from django.urls import path,include

from . import views
import routing
urlpatterns = [
    path('', views.homepage, name='index'),
    path('text/', views.text ,name="home"),
    path('text/chat', views.texting ,name="texting"),
    path('text/ip', views.ip_check ,name="ip"),
    path('', include('routing.websocket_urlpattern'))
]