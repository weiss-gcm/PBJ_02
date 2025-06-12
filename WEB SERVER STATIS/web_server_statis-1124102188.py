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
        self.wfile.write(bytes('<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg" alt="makanan">', "utf-8"))
        self.wfile.write(bytes('<img src="https://en.wikichip.org/w/images/4/4e/amd_ryzen_7_logo.png" alt="cpu">', "utf-8"))
        self.wfile.write(bytes('<img src="https://images.squarespace-cdn.com/content/v1/607f89e638219e13eee71b1e/1684821560422-SD5V37BAG28BURTLIXUQ/michael-sum-LEpfefQf4rU-unsplash.jpg" alt="Kucing">', "utf-8"))
        self.wfile.write(bytes('<img src="https://www.ginoguitars.com/libimg2/products/2160x1440/0/90/Fender-American-Original-60s-Telecaster-099-RW-LPB_01.jpg" alt="Telecaster 60s">', "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass
webServer.server_close()
