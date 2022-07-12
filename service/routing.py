from django.urls import re_path,path
# from django.conf.urls import url
from . import consumers
from .consumers import ChatConsumer

websocket_urlpattern=[
    url(r"ws/chat/",ChatConsumer),
]   