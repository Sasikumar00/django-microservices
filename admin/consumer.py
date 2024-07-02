import pika
import pika.exceptions

params = pika.URLParameters("amqps://hlvufrru:fhvdfqZzT2DgfRzz7qXQZwX1oMqZyV3S@moose.rmq.cloudamqp.com/hlvufrru")

def main():
    try:
        connection = pika.BlockingConnection(params)

        channel = connection.channel()

        channel.queue_declare(queue="admin")

        def callback(ch, method, properties, body):
            print(f"Received {body}")

        channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=True)

        print("Started Consuming...")

        channel.start_consuming()
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Failed to connect to RabbitMQ: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()