from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "127.0.0.1"
hostPort = 89


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print('\n')
        print(self.path)
        print('\n')
        if 'other-stuff' in self.path:
            response = 'other response'
        else:
            response = 'response'
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(response, "utf-8"))


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), f'Server Starts - {hostName} {hostPort}')

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
