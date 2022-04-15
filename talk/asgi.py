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
from service import routing

import service.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'talk.settings')
# django.setup()

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  'websocket':AuthMiddlewareStack(
    URLRouter(
      routing.websocket_urlpattern
    )
  )
  # We will add WebSocket protocol later, but for now it's just HTTP.
})