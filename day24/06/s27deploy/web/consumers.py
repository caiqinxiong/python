import json
import time
import threading
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.exceptions import StopConsumer
from web import models

def create_node(task_object,task_id):
    """
    创建节点
    :return:
    """
    # 数据库已有节点了，不要在创建了
    db_node_object_list = models.Node.objects.filter(task_id=task_id)
    if db_node_object_list:
        return db_node_object_list

    # 数据库没有节点，需要去创建
    node_object_list = []
    start_node = models.Node.objects.create(text='开始', task_id=task_id)
    node_object_list.append(start_node)
    # 判断第一个钩子处是否自定义脚本：任务单对象.before_download_script
    if task_object.before_download_script:
        start_node = models.Node.objects.create(text="下载前", task_id=task_id, parent=start_node)
        node_object_list.append(start_node)

    download_node = models.Node.objects.create(text='下载', task_id=task_id, parent=start_node)
    node_object_list.append(download_node)

    if task_object.after_download_script:
        download_node = models.Node.objects.create(text="下载后", task_id=task_id, parent=download_node)
        node_object_list.append(download_node)

    upload_node = models.Node.objects.create(text='上传', task_id=task_id, parent=download_node)
    node_object_list.append(upload_node)

    for server_object in task_object.project.servers.all():
        server_node = models.Node.objects.create(
            text=server_object.hostname,
            task_id=task_id,
            parent=upload_node,
            server=server_object)
        node_object_list.append(server_node)
        # 发布前钩子
        if task_object.before_deploy_script:
            server_node = models.Node.objects.create(
                text="发布前",
                task_id=task_id,
                parent=server_node,
                server=server_object)
            node_object_list.append(server_node)

        deploy_node = models.Node.objects.create(
            text="发布",
            task_id=task_id,
            parent=server_node,
            server=server_object)
        node_object_list.append(deploy_node)
        # 发布后钩子
        if task_object.after_deploy_script:
            after_deploy_node = models.Node.objects.create(
                text="发布后",
                task_id=task_id,
                parent=deploy_node,
                server=server_object)
            node_object_list.append(after_deploy_node)

    return node_object_list

def convert_object_to_gojs(node_object_list):
    """
    将对象列表转换为gojs识别的json格式
    :param node_object_list:
    :return:
    """
    node_list = []
    for node_object in node_object_list:
        temp = {
            'key': str(node_object.id),
            'text': node_object.text,
            'color':node_object.status,
        }
        if node_object.parent:
            temp['parent'] = str(node_object.parent_id)
        node_list.append(temp)

    return node_list



class PublishConsumer(WebsocketConsumer):

    def deploy(self,task_object,task_id):
        # 第一步：开始，找到数据库中的开始节点，给他变状态（颜色），同时将状态给前端返回。
        start_node = models.Node.objects.filter(text='开始', task_id=task_id).first()
        start_node.status = "green"
        start_node.save()
        async_to_sync(self.channel_layer.group_send)(
            task_id, {'type': 'my.send', 'message': {'code': 'update', 'node_id': start_node.id, 'color': "green"}}
        )

        # 第二步：下载前
        if task_object.before_download_script:
            # TODO 要去做一些具体的动作，执行钩子脚本，执行成功；失败
            before_download_node = models.Node.objects.filter(text='下载前', task_id=task_id).first()
            before_download_node.status = "green"
            before_download_node.save()
            async_to_sync(self.channel_layer.group_send)(
                task_id,
                {'type': 'my.send', 'message': {'code': 'update', 'node_id': before_download_node.id, 'color': "green"}}
            )

        # 第三步：下载
        # TODO 要去做一些具体的动作，去git中拉取
        time.sleep(2)
        download_node = models.Node.objects.filter(text='下载', task_id=task_id).first()
        download_node.status = "green"
        download_node.save()
        async_to_sync(self.channel_layer.group_send)(
            task_id,
            {'type': 'my.send', 'message': {'code': 'update', 'node_id': download_node.id, 'color': "green"}}
        )

        # 第四步：下载后
        if task_object.after_download_script:
            # TODO 要去做一些具体的动作，执行钩子脚本，执行成功；失败
            after_download_node = models.Node.objects.filter(text='下载后', task_id=task_id).first()
            after_download_node.status = "green"
            after_download_node.save()
            async_to_sync(self.channel_layer.group_send)(
                task_id,
                {'type': 'my.send',
                 'message': {'code': 'update', 'node_id': after_download_node.id, 'color': "green"}}
            )
        # 第五步：上传
        upload_node = models.Node.objects.filter(text='上传', task_id=task_id).first()
        upload_node.status = "green"
        upload_node.save()
        async_to_sync(self.channel_layer.group_send)(
            task_id,
            {'type': 'my.send',
             'message': {'code': 'update', 'node_id': upload_node.id, 'color': "green"}}
        )

        # 第六步：连接每台服务器
        for server_object in task_object.project.servers.all():

            # 第 六点一 步：上传代码
            # TODO，通过paramiko将代码上传到服务器
            time.sleep(2)
            server_node = models.Node.objects.filter(text=server_object.hostname, task_id=task_id,
                                                     server=server_object).first()
            server_node.status = "green"
            server_node.save()
            async_to_sync(self.channel_layer.group_send)(
                task_id,
                {'type': 'my.send',
                 'message': {'code': 'update', 'node_id': server_node.id, 'color': "green"}}
            )

            # 第 六点二 步：发布前钩子
            # TODO
            if task_object.before_deploy_script:
                before_deploy_node = models.Node.objects.filter(text="发布前",
                                                                task_id=task_id,
                                                                server=server_object).first()
                before_deploy_node.status = "green"
                before_deploy_node.save()
                async_to_sync(self.channel_layer.group_send)(
                    task_id,
                    {'type': 'my.send',
                     'message': {'code': 'update', 'node_id': before_deploy_node.id, 'color': "green"}}
                )
            # 第 六点三 步：发布
            # TODO
            deploy_node = models.Node.objects.filter(text="发布",
                                                     task_id=task_id,
                                                     server=server_object).first()
            deploy_node.status = "green"
            deploy_node.save()
            async_to_sync(self.channel_layer.group_send)(
                task_id,
                {'type': 'my.send',
                 'message': {'code': 'update', 'node_id': deploy_node.id, 'color': "green"}}
            )

            # 第 六点四 步：发布后钩子
            # TODO
            if task_object.after_deploy_script:
                after_deploy_node = models.Node.objects.filter(text="发布后",
                                                               task_id=task_id,
                                                               server=server_object).first()
                after_deploy_node.status = "green"
                after_deploy_node.save()
                async_to_sync(self.channel_layer.group_send)(
                    task_id,
                    {'type': 'my.send',
                     'message': {'code': 'update', 'node_id': after_deploy_node.id, 'color': "green"}}
                )

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

        # 当用户打开页面时，如果已经创建好节点了，则默认展示所有节点数据。
        db_node_object_list = models.Node.objects.filter(task_id=task_id)
        if db_node_object_list:
            node_list = convert_object_to_gojs(db_node_object_list)
            self.send(text_data=json.dumps({'code': 'init', 'data': node_list}))

    def websocket_receive(self, message):
        task_id = self.scope['url_route']['kwargs'].get('task_id')
        task_object = models.DeployTask.objects.filter(id=task_id).first()
        # 获取用户发送过来的指令：init
        txt = message['text']

        if txt == 'init':
            # 第一步：没有创建过，则去数据库创建所有节点。有的话，直接读取。
            node_object_list = create_node(task_object,task_id)

            # 第二步：根据对象列表生成特定JSON格式数据给用户返回
            node_list = convert_object_to_gojs(node_object_list)

            # 第三步：把数据通过websocket发给前端，前端赋值给gojs
            async_to_sync(self.channel_layer.group_send)(task_id, {'type': 'my.send',
                                                                   'message': {'code': 'init', 'data': node_list}})

        if txt == 'deploy':
            # 代码发布
            # self.deploy(task_object,task_id)
            # channels的小别扭
            thread = threading.Thread(target=self.deploy,args=(task_object,task_id,))
            thread.start()

    def my_send(self, event):
        message = event['message']  # 123
        self.send(json.dumps(message))

    def websocket_disconnect(self, message):
        task_id = self.scope['url_route']['kwargs'].get('task_id')
        async_to_sync(self.channel_layer.group_discard)(task_id, self.channel_name)
        raise StopConsumer()
