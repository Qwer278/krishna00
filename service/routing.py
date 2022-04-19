from django.urls import re_path,path
from . import consumers
from consumers import ChatConsumer

websocket_urlpattern=[
    path('ws/socket-server/',ChatConsumer.as_asgi())
]   