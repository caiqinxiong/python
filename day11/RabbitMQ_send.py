# -*- coding:utf-8 -*-
# Author:caiqinxiong
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel() # 声明一个管道

# 声明queue
channel.queue_declare(queue='hello')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello', # queue名字
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()