from django.urls import path,include,re_path
# from django.conf.urls import url

from . import views
from . import routing
urlpatterns = [
    path('', views.homepage, name='index'),
    path('text/', views.text ,name="home"),
    path('text/chat', views.texting ,name="texting"),
    path('text/ip', views.ip_check ,name="ip"), 
    re_path(r'', include(routing.websocket_urlpattern)),
]