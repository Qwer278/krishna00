from django.urls import re_path,path
# from django.conf.urls import url
from . import consumers
from . import consumers

websocket_urlpattern=[
    re_path(r'text/ws/$',consumers.ChatConsumer.as_asgi()),
]   