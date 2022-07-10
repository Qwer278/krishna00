from django.urls import re_path,path
from . import consumers
from .consumers import ChatConsumer

websocket_urlpattern=[
    path(r'ws/chat/',ChatConsumer.as_asgi()),
]   