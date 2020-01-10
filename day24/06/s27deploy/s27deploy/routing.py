from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from web import consumers


application = ProtocolTypeRouter({
    'websocket': URLRouter([
        url(r'^publish/(?P<task_id>\d+)/$', consumers.PublishConsumer),
    ])
})