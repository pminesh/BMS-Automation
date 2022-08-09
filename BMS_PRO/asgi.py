"""
ASGI config for BMS_host project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import os
import django
from django.core.asgi import get_asgi_application
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from BMS_Apps.BMS_Main.BmsConsumer import BmsConsumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BMS_PRO.settings')

django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r'^ws/', BmsConsumer.as_asgi()),
        ])
    ),
})
