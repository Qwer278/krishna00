"""
ASGI config for talk project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from service.routing import websocket_urlpattern
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
import django
from service.routing import websocket_urlpattern


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'talk.settings')
django.setup()

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  'websocket':AuthMiddlewareStack(
      URLRouter(websocket_urlpattern)
  )
  # We will add WebSocket protocol later, but for now it's just HTTP.
})