from django.urls import re_path,path
# from django.conf.urls import url
from . import consumers
from .consumers import ChatConsumer

websocket_urlpattern=[
    re_path(r'^ws/chat',ChatConsumer.as_asgi()),
]   