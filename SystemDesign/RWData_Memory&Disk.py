from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName='localhost'
serverPort=8080


string = ''
diskfilename='D:\CodingPractise\disk.text'

class MyServer(BaseHTTPRequestHandler):
    
    # get data from memory
    def do_GET(self):

        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()

        if self.path=='/disk':
            with open(diskfilename,'r') as f:
                read_data=f.read()
                print(read_data)
            self.wfile.write(bytes("Reading data from disk","utf-8"))
            self.wfile.write(bytes(read_data,"utf-8"))
            
        elif self.path=='/memory':
            #print("hello"+string)
            self.wfile.write(bytes("Reading data from memory","utf-8"))
            
            self.wfile.write(bytes(string,"utf-8"))
        

    # post data to disk and memory
    def do_POST(self):
        print("Hello, I'm in POST!")
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        print(self.path)
        if self.path=='/disk':
            print("Hello, I am writing to disk!")
            content_len = int(self.headers.get('content-length'))
            #content_len=int(self.headers.getheader('content-length',0))
            post_body = str(self.rfile.read(content_len))
            print(post_body)
            with open(diskfilename,'w') as f:
                f.write(post_body)
                print(post_body)
            self.wfile.write(bytes("Just written data to disk","utf-8"))
        elif self.path=='/memory':
            content_len=int(self.headers.get('content-length'))
            post_body = str(self.rfile.read(content_len))
            #print(post_body)
            global string
            string = post_body
            #print(string)
            self.wfile.write(bytes("Just written data to memory","utf-8"))
            
    
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
