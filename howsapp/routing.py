from django.urls import path , include,re_path
from .consumers import ChatConsumer

# Here, "" is routing to the URL ChatConsumer which 
# will handle the chat functionality.
websocket_urlpatterns = [
    path("ws/chat/<room_slug>/" , ChatConsumer.as_asgi()) , 
] 


