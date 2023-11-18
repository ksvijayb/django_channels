# live_execution/asgi.py

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import execution_stream.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        execution_stream.routing.websocket_urlpatterns
    ),
})
