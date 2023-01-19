from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName='localhost'
serverPort=8080


class MyServer(BaseHTTPRequestHandler):
    
    # get data from memory
    def do_GET(self):

        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()

        if self.path=='/hello':
            print("server is listening to port 8080")
            self.wfile.write(bytes("Hello Wahdat!","utf-8"))
            
            
    
if __name__=="__main__":

    webServer = HTTPServer((hostName,serverPort),MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")



# send data to the server >curl --header 'content-type':application/json localhost:8080 --data '{"foo":"bar"}'
# request data from the server >curl localhost:8080
