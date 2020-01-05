# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/12/29 下午3:10
from channels.routing import ProtocolTypeRouter,URLRouter
from django.conf.urls import url
from app01 import consumers

application = ProtocolTypeRouter({
    'websocket':URLRouter([
        url(r'^chat/$', consumers.ChatConsumer),
    ])
})
