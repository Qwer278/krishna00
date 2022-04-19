from django.urls import re_path
from . import consumers

websocket_urlpattern=[
    re_path(r'ws/socket-server/',consumers.ChatConsumer.as_asgi())
]   