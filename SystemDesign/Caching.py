from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName='localhost'
serverPort=8080

cache = {}

def database(key):
    data={}
    data['index.html'] = '<html>Hello World!</html>'

    time.sleep(3)
    if key=='index.html':
        return data[key]

class MyServer(BaseHTTPRequestHandler):
    
    # get data from memory
    def do_GET(self):

        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()

        if self.path=='/nocache/index.html':
            read_data = database('index.html')
            #self.wfile.write(bytes("Reading data from disk","utf-8"))
            self.wfile.write(bytes(read_data,"utf-8"))
            
        elif self.path=='/withcache/index.html':
            if 'index.html' in cache.keys():
                self.wfile.write(bytes(cache['index.html'],"utf-8"))
            else:
                get_data = database('index.html')
                #global cache
                cache['index.html'] = get_data
                self.wfile.write(bytes(get_data,"utf-8"))
        
    
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
