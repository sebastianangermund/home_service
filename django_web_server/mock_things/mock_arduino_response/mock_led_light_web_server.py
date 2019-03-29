from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = '127.0.0.1'
hostPort = 89
state = 'ON'


class MyLedLightServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print('request: ', self.path)
        if '/id/state/' in self.path:
            response = state
        elif '/id/0/' in self.path:
            state = 'OFF'
            response = 'you just changed the state to OFF'
            print(response)
        elif '/id/1/' in self.path:
            state = 'ON'
            response = 'you just changed the state to ON'
            print(response)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        if response:
            self.wfile.write(bytes(response, 'utf-8'))


myServer = HTTPServer((hostName, hostPort), MyLedLight)
print(time.asctime(), f'Server Starts - {hostName} {hostPort}')

try:
    MyLedLight.serve_forever()
except KeyboardInterrupt:
    pass

MyLedLight.server_close()
print(time.asctime(), f'Server Stops - {hostName} {hostPort}')
