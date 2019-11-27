from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = '0.0.0.0'
hostPort = 9753


class MyLedLightServer(BaseHTTPRequestHandler):

    get_led_state = '/uuid/get-state/'
    set_led_off = '/uuid/set-state=0/'
    set_led_on = '/uuid/set-state=1/'

    def do_GET(self):
        if self.get_led_state in self.path:
            led_state = 'OFF'
            try:
                f = open('led_state', 'r')
                led_state = f.read().strip()
                f.close()
            except:
                f = open('led_state', 'w+')
                f.write(led_state)
                f.close()
            response = led_state
        elif self.set_led_off in self.path:
            f = open('led_state', 'w+')
            f.write('OFF')
            f.close()
            response = 'you\'ve just changed the state to OFF'
        elif self.set_led_on in self.path:
            f = open('led_state', 'w+')
            f.write('ON')
            f.close()            
            response = 'you\'ve just changed the state to ON'
        else:
            self.send_response(418)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('I\'m a teapot', 'utf-8'))
            return

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(response, 'utf-8'))


myServer = HTTPServer((hostName, hostPort), MyLedLightServer)
print(time.asctime(), 'Server Starts - {} {}'.format(hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), 'Server Stops - {} {}'.format(hostName, hostPort))
