#!/usr/bin/env python
import pika, sys, os, ssl

def main():

    host = "localhost" # hostname do rabbit
    port = "5671" # porta do rabbit
    vhost = "/" # nome do vhost
    credentials = pika.PlainCredentials('username', 'password')


    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host,port,vhost,credentials,ssl_options=pika.SSLOptions(context)))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)