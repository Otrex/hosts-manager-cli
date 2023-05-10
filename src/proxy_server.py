import json
import socket
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from tabulate import tabulate
from constants import PID_REGISTER, DOMAIN_MAP_REGISTER, ERROR_HTML_PATH

import os

with open(PID_REGISTER, "w") as f:
    f.write(str(os.getpid()))

# Load the configuration file
with open(DOMAIN_MAP_REGISTER) as f:
    config = json.load(f)

# Define a request handler class
class RequestHandler(BaseHTTPRequestHandler):
    def send_error_html(self, status_code = 400):
        with open(ERROR_HTML_PATH, 'rb') as f:
                self.wfile.write(f.read())

    def do_GET(self):
        # Get the server name from the request header
        server_name = self.headers.get("Host", "")
        status_code = 500
        response_headers = []
        response_data = b''

        # Look up the IP address and port in the configuration
        if server_name in config:
            ip, port = config[server_name]
        else:
            self.send_error(404)
            return

        # Forward the request to the destination server
        try:
            url = "http://{}:{}{}".format(ip, port, self.path)
            response = urlopen(url)
            status_code = response.getcode()
            response_headers = response.headers.items()
            response_data = response.read()
        except Exception as e:
            self.send_error_html(status_code)
            print(e)

        except (HTTPError, ConnectionRefusedError) as e:
            print("\U0001F525 Error: %s" % e.reason)
            status_code = getattr(e, 'code', 400)
            response_headers = e.headers.items()
            response_data = e.read()
            for header, value in response_headers:
                self.send_header(header, value)
            self.end_headers()
            self.send_error_html(status_code)
            return

        except URLError as e:
            self.send_error_html()
            print("\U0001F525 Error: ")
            return
            
        # Send the response back to the client
        self.send_response(status_code)
        for name, value in response_headers:
            self.send_header(name, value)
        self.end_headers()
        self.wfile.write(response_data)

# Start the HTTP server on port 8080
server_address = ("", 80)
httpd = HTTPServer(server_address, RequestHandler)

# Print the mappings in a table
table = []
for server_name, (ip, port) in config.items():
    try:
        host_name = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        host_name = ip
    table.append((server_name, host_name, ip, port))
print(tabulate(table, headers=["Server Name", "Host Name", "IP Address", "Port"]))

# Start the HTTP server in a separate thread
thread = threading.Thread(target=httpd.serve_forever)
thread.daemon = True
thread.start()

# Wait for the user to press Ctrl-C to stop the server
try:
    while True:
        pass
except KeyboardInterrupt:
    httpd.shutdown()