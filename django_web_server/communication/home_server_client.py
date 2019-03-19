"""
Receive a mqtt request from home_server client.

Forward the message to appropriate arduino-ESP web server.

Return status code to home_server client.
"""

import pika
import json
import requests


# adress = '192.168.1.58'
adress = 'localhost'
port = '80'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()
channel.queue_delete(queue='home_server')
channel.queue_declare(queue='home_server')


def callback(ch, method, properties, body):
    """Handle mqtt payload and convert to http request. Then return status.

    """
    print(f' [*] Received {body}')
    raw_message = json.loads(body)
    thing_state = raw_message['payload']['thing_state']
    thing_id = raw_message['payload']['thing_id']
    # do a match search for id
    if thing_state and thing_id:
        ON = thing_state.endswith('on')
        OFF = thing_state.endswith('off')
        if ON:
            pass
        elif OFF:
            pass

    # path = f'http://{adress}:{port}/{thing_id}/{thing_state'
    path = 'http://localhost:80'
    print(path)
    response = requests.put(path)

    print(f' [x] Done, status {response.status_code} ')


channel.basic_consume(
    callback,
    queue='home_server',
)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
