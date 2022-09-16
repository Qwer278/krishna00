from django.urls import path,include
from django.conf.urls import include, url

from . import views
from . import routing
urlpatterns = [
    path('', views.homepage, name='index'),
    path('text/', views.text ,name="home"),
    path('text/chat', views.texting ,name="texting"),
    path('text/ip', views.ip_check ,name="ip"),
    url(r'^', include(routing.websocket_urlpattern)),
]