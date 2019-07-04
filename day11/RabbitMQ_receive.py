# -*- coding:utf-8 -*-
# Author:caiqinxiong
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(ch,method,properties)
    print(" [x] Received %r" % body)

# 消费消息
channel.basic_consume(callback, # 如果收到消息就调用callback函数来处理消息
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
# 开始接收，一启动就一直运行
channel.start_consuming()

