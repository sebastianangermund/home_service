import requests


def request_get(payload):
    """Convert to http request and forward.

    """
    # payload = 'http://localhost:80/'  # use for testing
    try:
        response = requests.request('GET', payload, timeout=5)
        return response
    except requests.exceptions.Timeout as e:
        return 'time out'
