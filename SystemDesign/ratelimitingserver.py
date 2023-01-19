from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests

serverName = 'localhost'
port = 8083

accesses = {}

class RateLimitingServer(BaseHTTPRequestHandler):

    def do_GET(self):

        #print(self.headers)
        user = self.path.split('=')[1]
        if user in accesses.keys():
            previousAccessTime = accesses[user]

            if (int(round(time.time())) - previousAccessTime) < 5:
                self.send_response(429)
                self.send_header('content-type','text')
                self.end_headers()
                self.wfile.write(bytes('Too many requests.\n','utf-8'))

        try:
            response = requests.get('http://localhost:8082/index.html')
            accesses[user] = int(round(time.time()))
            print(response.status_code)
            response.raise_for_status()
        except requests.exceptions.HTTPError as eerh:
            print(errh)
            






if __name__=="__main__":

    webserver = HTTPServer((serverName,port), RateLimitingServer)
    print("Rate Limiting Server started at http://%s:%s" %(serverName, port))

    try:
        webserver.serve_forever()

    except KeyboardInterrupt:

        webserver.server_close()
        print("Server stopped.")


        
    
