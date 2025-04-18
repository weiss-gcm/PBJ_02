import socket
from threading import Thread

SERVER_HOST = "192.168.157.138"  # IP Address disamakan dengan server agar bisa terhubung
SERVER_PORT = 5002
separator_token = "<SEP>"

name = input("Enter your name: ")
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
try:
    s.connect((SERVER_HOST, SERVER_PORT))
    print("[+] Connected.")
except socket.error as e:
    print(f"[!] Connection error: {e}")
    exit()

def listen_for_messages():
    while True:
        try:
            message = s.recv(1024).decode()
            if message:
                print("\n" + message)
            else:
                print("[!] Disconnected from server.")
                break
        except Exception as e:
            print(f"[!] Error while receiving message: {e}")
            break

    s.close()

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    msg = input()
    if msg.lower() == 'exit':
        break
    if msg.strip():
        message = f"{name}{separator_token}{msg}"
        s.send(message.encode())

s.close()
print("[-] Connection closed.")
