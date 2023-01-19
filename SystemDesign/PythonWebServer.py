from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName='localhost'
serverPort=8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>","utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(bytes("Post request recieved","utf-8"))


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
