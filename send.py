#!/usr/bin/env python
from datetime import datetime
import pika, ssl

host = "localhost" # hostname do rabbit
port = "5672" # porta do rabbit
vhost = "/" # nome do vhost
credentials = pika.PlainCredentials('username', 'password')

connection = pika.BlockingConnection(pika.ConnectionParameters(host,port,vhost,credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%H:%M:%S.%f - %b %d %Y")

channel.basic_publish(exchange='', routing_key='hello', body=timestampStr)
print(" [x] Sent " + timestampStr)
connection.close()