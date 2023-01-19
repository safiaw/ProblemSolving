from http.server import BaseHTTPRequestHandler, HTTPServer


class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
  

    def do_GET(self, body=True):
        try:
            #req_header = self.parse_headers()
            self.send_response(200)
            self.send_header("content-type","text/html")
            self.end_headers()
            #self.send_resp_headers(req_header, 11)
            self.wfile.write(bytes("Hello, I am at reverse proxy server","utf-8"))
            if self.path=="/hello":
                req_header = "Header from reverse proxy"
                resp = requests.get('localhost:8080/hello', headers=req_header, verify=False)
                # Respond with the requested data
                self.send_response(resp.status_code)

if __name__ == "__main__":

    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, ProxyHTTPRequestHandler)
    print('Reverse proxy server started http://%s"%s' %(server_address[0],server_address[1]))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print("Reverse proxy server stopped.")
