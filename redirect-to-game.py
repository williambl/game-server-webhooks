from http.server import *
import sys

class FakeRedirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(301)
       new_path = 'steam://connect/'+sys.argv[1]
       self.send_header('Location', new_path)
       self.end_headers()

HTTPServer(("", 8080), FakeRedirect).serve_forever()
