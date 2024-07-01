import pika

params = pika.URLParameters("amqps://hlvufrru:fhvdfqZzT2DgfRzz7qXQZwX1oMqZyV3S@moose.rmq.cloudamqp.com/hlvufrru")
connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    channel.basic_publish(exchange="", routing_key="main", body="Hello Main!")