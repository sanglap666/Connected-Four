import os

from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import re_path 
from .consumer import ChatConsumer,GameConsumer
from django.conf.urls import url


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = ProtocolTypeRouter({

    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                   url(r"^profile/(?P<username>[\w.@+-]+)",GameConsumer), 
                   url("profile",ChatConsumer)
                ]
            )
        )
    )
    
    
})