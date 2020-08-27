import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class CustomHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # if self.path == '/':
        #     self.path = '/index.html'
        # try:
        #     file_to_open = open(self.path[1:]).read()
        #     self.send_response(200)
        # except:
        #     file_to_open = 'File not found'
        #     self.send_response(404)
        # self.end_headers()
        # self.wfile.write(bytes(file_to_open, 'utf-8'))
        self.send_response(400)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"CSV UPLOADING")

    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type', 'application/json')
        self.send_header('Server', 'CoolServer')
        self.end_headers()
        self.wfile.write(json.dumps({'result': True}).encode())

    def do_PUT(self):
        self.send_response(200)
        self.send_header('content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"PUT request\n")


server_address = ('', 8888)
httpd = HTTPServer(server_address, CustomHandler)
httpd.serve_forever()