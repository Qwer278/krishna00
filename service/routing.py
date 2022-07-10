from django.urls import re_path,path
from . import consumers
from .consumers import ChatConsumer

websocket_urlpattern=[
    url(r'^ws/chat/$',ChatConsumer.as_asgi()),
]   