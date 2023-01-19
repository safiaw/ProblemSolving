from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName='localhost'
serverPort=8082


class MyServer(BaseHTTPRequestHandler):
    
    # get data from memory
    def do_GET(self):

        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()

        print("server is listening to port 8082")
        print(self.headers)
                   
    
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