
#!/usr/bin/env python
 
import random, time, os, sys
 
join = os.path.join
 
import mimetypes
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
 
### Utils #####################################################################
 
def read_file(path, binary=False):
    if binary:
        f = open(path, 'rb')
    else:
        f = open(path, 'r')
 
    result = f.read()
    f.close()
 
    return result
 
def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text
 
def remove_prefix_slash(text):
    return remove_prefix(remove_prefix(text, '\\'), '/')
 
### Request Handler ###########################################################
 
class RequestHandler(BaseHTTPRequestHandler):
 
    def __init__(self, *args, **kwargs):
        self.server_path = os.path.dirname(sys.argv[0])
        BaseHTTPRequestHandler.__init__(self, *args, **kwargs)
 
        self.pages = {}
 
    def do_GET(self):
	print("in  get")
        if self.path == '/favicon.ico': return 
 
        self.base_local_path = os.path.normpath(os.getcwd())
        self.local_path      = os.path.normpath( join(self.base_local_path, remove_prefix_slash(os.path.normpath(self.path))) )
 
        page = '/' + self.path
 
        if page in self.pages:
            self.pages[page].do_GET()
 
    def do_POST(self):
        self.base_local_path = os.path.normpath(os.getcwd())
        self.local_path      = os.path.normpath( join(self.base_local_path, remove_prefix_slash(os.path.normpath(self.path))) )
 
        page = '/' + self.path
 
        if page in self.pages:
            self.pages[page].do_POST()
 
 
    def render_listing(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
 
        self.wfile.write('<html><body>')
 
        self.wfile.write('</body></html>')
        self.wfile.close()
 
 
### Driver ####################################################################
 
def main():
    server = HTTPServer(
        ('localhost', 8000),
        RequestHandler
    )
 
    while 1:
        server.handle_request()
 
main()

