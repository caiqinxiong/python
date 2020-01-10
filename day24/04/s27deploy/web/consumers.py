import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.exceptions import StopConsumer
from web import models


class PublishConsumer(WebsocketConsumer):

    def websocket_connect(self, message):
        """
        客户端要向服务端创建websocket连接
        :param message:
        :return:
        """

        task_id = self.scope['url_route']['kwargs'].get('task_id')
        # 接收客户端的连接
        self.accept()
        async_to_sync(self.channel_layer.group_add)(task_id, self.channel_name)

        node_queryset = models.Node.objects.filter(task_id=task_id)
        # 数据库有节点,应该给用户返回.
        if node_queryset:
            node_list = []
            for node_object in node_queryset:
                temp = {
                    'key': str(node_object.id),
                    'text': node_object.text,
                }
                if node_object.parent:
                    temp['parent'] = str(node_object.parent_id)
                node_list.append(temp)
            self.send(text_data=json.dumps({'code':'init','data':node_list}))

    def websocket_receive(self, message):
        task_id = self.scope['url_route']['kwargs'].get('task_id')

        txt = message['text']
        if txt == 'init':
            """
            node_list = [
                {"key": "start", "text": '开始'},
                {"key": "download", "parent": 'start', "text": '下载代码'},
                {"key": "compile", "parent": 'download', "text": '本地编译'},
            ]
            """

            # 创建节点,并返回给前端

            node_object_list = []

            node_queryset = models.Node.objects.filter(task_id=task_id)
            # 在数据库生成节点
            if not node_queryset:
                start_node = models.Node.objects.create(text='开始',task_id=task_id)
                node_object_list.append(start_node)

                download_node = models.Node.objects.create(text='下载',task_id=task_id,parent=start_node)
                node_object_list.append(download_node)

                upload_node = models.Node.objects.create(text='上传',task_id=task_id,parent=download_node)
                node_object_list.append(upload_node)

                task_object = models.DeployTask.objects.filter(id=task_id).first()
                for server_object  in task_object.project.servers.all():
                    row = models.Node.objects.create(text=server_object.hostname,
                                               task_id=task_id,
                                               parent=upload_node,
                                               server=server_object)
                    node_object_list.append(row)
            else:
                node_object_list = node_queryset

            node_list = []
            for node_object in node_object_list:
                temp = {
                    'key':str(node_object.id),
                    'text':node_object.text,
                }
                if node_object.parent:
                    temp['parent'] = str(node_object.parent_id)
                node_list.append(temp)

            # self.send(text_data=json.dumps({'code':'init','data':node_list}))
            async_to_sync(self.channel_layer.group_send)(task_id, {'type': 'my.send','message':{'code':'init','data':node_list} })

    def my_send(self,event):
        message = event['message'] # 123
        self.send(json.dumps(message))

    def websocket_disconnect(self, message):
        task_id = self.scope['url_route']['kwargs'].get('task_id')
        async_to_sync(self.channel_layer.group_discard)(task_id, self.channel_name)
        raise StopConsumer()