import requests
import pika
import json


def communication_2(payload):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'),
    )

    channel = connection.channel()
    channel.queue_declare(queue='home_server')

    rawMessage = {
        'payload': payload,
    }
    message = json.dumps(rawMessage)

    response = channel.basic_publish(
        exchange='',
        routing_key='home_server',
        body=message,
    )
    print(response)
    channel.queue_declare(queue='home_server')
    connection.close()


# adress = '192.168.1.58'
# adress = 'localhost'
# port = '80'

# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(host='localhost')
# )
# channel = connection.channel()
# channel.queue_delete(queue='home_server')
# channel.queue_declare(queue='home_server')


def communication(payload):
    """Convert to http request and forward.

    """
    # payload = 'http://localhost:80/'  # use for testing
    try:
        response = requests.request('GET', payload, timeout=5)
        return response.status_code
    except requests.exceptions.Timeout as e:
        return e


def get_state(payload):
    """Convert to http request and forward.

    """
    # payload = 'http://localhost:80/'  # use for testing
    try:
        response = requests.request('GET', payload, timeout=5)
        print(response)
        return response
    except requests.exceptions.Timeout as e:
        return e
