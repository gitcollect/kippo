import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def send_response(self, code, message=None):
        self.log_request(code)
        self.wfile.write('%s %s %s\r\n' %
                         ('HTTP/1.1', str(401), 'Unauthorized'))

        self.send_header('Date', self.date_time_string())
        self.send_header('Server', 'Virata-EmWeb/R6_0_1')
        self.send_header('Connection', 'close')
        self.send_header('WWW-Authenticate', 'Basic realm=\"NetScreen Web Auth User Authentication\"')
        self.end_headers()

httpd = SocketServer.TCPServer(("", 8080), Handler)
httpd.serve_forever()

if __name__ == '__main__':
    main()
