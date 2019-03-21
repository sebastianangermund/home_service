from http.server import HTTPServer, BaseHTTPRequestHandler


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('localhost', 80)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

    handler_class.handle_one_request()
