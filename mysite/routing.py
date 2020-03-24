# mysite/routing.py


from django.conf.urls import url

from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from channels.auth import AuthMiddlewareStack
import chat.routing

application = ProtocolTypeRouter({

    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
            # url(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
        )
    ),

})
