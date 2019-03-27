import requests
import pika
import json

from ..analytics.models import LedLightData


""" There should be a function that runs logging every x minutes
"""


def schedule_ledlight_data_update():
    queryset = LedLightData.objects.all()
    logging_service(queryset)


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


def logging_service(queryset):
    for thing in queryset:
        thing.write_data_point


def request_get(payload):
    """Convert to http request and forward.

    """
    # payload = 'http://localhost:80/'  # use for testing
    try:
        response = requests.request('GET', payload, timeout=5)
        return response
    except requests.exceptions.Timeout as e:
        return 'time out'
