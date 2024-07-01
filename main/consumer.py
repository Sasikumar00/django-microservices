import pika

params = pika.URLParameters("amqps://hlvufrru:fhvdfqZzT2DgfRzz7qXQZwX1oMqZyV3S@moose.rmq.cloudamqp.com/hlvufrru")
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="main")

def callback(ch, method, properties, body):
    print("Recieved", body)

channel.basic_consume(queue="main", on_message_callback=callback)

print("Started Consuming...")

channel.start_consuming()