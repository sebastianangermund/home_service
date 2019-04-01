from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = '127.0.0.1'
hostPort = 88


class MyLedLightServer(BaseHTTPRequestHandler):
    mock_state = '-'
    get_led_state = '/uuid/get-state/'
    set_led_off = '/uuid/set-state=0/'
    set_led_on = '/uuid/set-state=1/'

    def do_GET(self):
        if self.get_led_state in self.path:
            response = self.mock_state
        elif self.set_led_off in self.path:
            response = 'you\'ve just changed the state to OFF'
        elif self.set_led_on in self.path:
            response = 'you\'ve just changed the state to ON'
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('I\'m a teapot', 'utf-8'))

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(response, 'utf-8'))


myServer = HTTPServer((hostName, hostPort), MyLedLightServer)
print(time.asctime(), f'Server Starts - {hostName} {hostPort}')

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), f'Server Stops - {hostName} {hostPort}')
