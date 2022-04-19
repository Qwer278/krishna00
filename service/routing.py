from django.urls import re_path
from . import consumers
from consumers import ChatConsumer

websocket_urlpattern=[
    re_path(r'ws/socket-server/',ChatConsumer.connect())
]   