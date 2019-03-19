import requests
import time

adress = '192.168.1.58'
port = '80'
path1 = 'on'
path2 = 'off'

i = 0
while True:
    i = (i + 1) % 2
    if i == 0:
        path = path1
    else:
        path = path2

    url = f'http://{adress}:{port}/{path}/'
    r = requests.put(url)
    # print(r.status_code, r.text)
    time.sleep(3)
