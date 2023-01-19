from http.server import BaseHTTPRequestHandler, HTTPServer
import time

serverName = 'localhost'
port = 8082

database = {
    'index.html':'<html>Hello World!</html>'
    }


class DatabaseServer(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path=='/index.html':
            time.sleep(5)
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.wfile.write(bytes(database['index.html'], 'utf-8'))
            self.end_headers()

if __name__=="__main__":

    webserver = HTTPServer((serverName,port), DatabaseServer)
    print("Database Server started at http://%s:%s" %(serverName, port))

    try:
        webserver.serve_forever()

    except KeyboardInterrupt:

        webserver.server_close()
        print("Server stopped.")

        
