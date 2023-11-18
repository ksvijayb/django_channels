# execution_stream/routing.py

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/execute/$', consumers.ExecutionConsumer.as_asgi()),
]
