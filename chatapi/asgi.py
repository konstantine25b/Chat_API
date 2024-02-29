import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapi.settings')

# Import your channel layers configuration from settings
from chatapi.settings import CHANNEL_LAYERS

# Define your ASGI application
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
    # Add the channel layers configuration here
    'channel': CHANNEL_LAYERS,
})