# mysite/routing.py


from django.conf.urls import url

from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from channels.auth import AuthMiddlewareStack
import chat.routing
import chat.consumers

application = ProtocolTypeRouter({

    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
            # url(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
        )
    ),

})


channel_routing = {
    'websocket.connect': chat.consumers.ChatConsumer.connect,
    'websocket.receive': chat.consumers.ChatConsumer.receive,
    'websocket.disconnect': chat.consumers.ChatConsumer.disconnect,
}
