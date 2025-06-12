# NAMA: DARMA ADHYAKSA PUTRA
# NIM: 1124102188

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost" #HostName bisa digantikan dengan IP Address jika ingin diakses secara external selain didalam komputer.
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):  
    def do_GET(self): 
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://testserver.com</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes('<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg" alt="lasagna">', "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass
webServer.server_close()
