import time

from config import get_connection
import pika
import json


def process_new_message(channel: pika.adapters.blocking_connection.BlockingChannel, method, properties, body):
    data = json.loads(body)
    print(f"Новий лог: {data.get('event')}, user_id: {data.get('user_id')}")
    channel.basic_ack(delivery_tag=method.delivery_tag)
    time.sleep(1)


def consume_logs(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = 'logs'
    channel.basic_consume(
        queue=QUEUE,
        on_message_callback=process_new_message,
    )
    channel.start_consuming()


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            consume_logs(channel)


if __name__ == "__main__":
    main()