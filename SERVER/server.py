import socket
from threading import Thread

SERVER_HOST = "192.168.137.158" #IP address Komputer Anda
SERVER_PORT = 5002
separator_token = "<SEP>"

clients = set()

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

def client_handler(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
            if not msg:
                break
        except Exception as e:
            print(f"[!] Error: {e}")
            clients.remove(cs)
            cs.close()
            break
        else:
            msg = msg.replace(separator_token, ":")
            for client in list(clients):
                try:
                    client.send(msg.encode())
                except:
                    clients.remove(client)

while True:
    cs, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    clients.add(cs)
    t = Thread(target=client_handler, args=(cs,))
    t.daemon = True
    t.start()

