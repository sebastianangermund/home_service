import requests
from requests.exceptions import HTTPError


def request_get(url, params):
    """Convert to http request and forward."""
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        return {
            'status': response.status_code,
            'encoding': response.encoding,
            'headers': response.headers,
            'content': response.content,
        }
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.Timeout as time_err:
        print(time_err)
    except Exception as err:
        print(f'{err}')
