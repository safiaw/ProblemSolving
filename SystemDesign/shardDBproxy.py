from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from urllib import request

hostName='localhost'
serverPort=8000


class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    
    # get data from memory
    def do_GET(self):

        req_header = self.headers
        print(self.path)

        firstchar = self.path.strip('/')[0]
        if ord(firstchar) % 2 == 0:
            # forward request to shardDB1
            print("Forwarding to Database server at localhost:3000")

            server_url = 'http://localhost:3000'
            # call the target server
            #response = request.get(server_url, headers = req_header, verify=False)
            
            self.send_response(301)
            self.send_header('Location','http://localhost:3000')
            self.end_headers()
            self.copyfile(urllib.urlopen(server_url))

        else:
            # forward request to shardDB2
            print("Forwarding to Database server at localhost:3001")

            server_url = 'http://localhost:3001'
            # call the target server
            response = request.get(server_url, headers = req_header, verify=False)
            self.send_response(response.status_code)
            self.send_header(response.headers)
            self.end_headers()
                
    
if __name__=="__main__":

    webServer = HTTPServer((hostName,serverPort),ProxyHTTPRequestHandler)
    print("Proxy Server started at http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")



# send data to the server >curl --header 'content-type':application/json localhost:8080 --data '{"foo":"bar"}'
# request data from the server >curl localhost:8080
