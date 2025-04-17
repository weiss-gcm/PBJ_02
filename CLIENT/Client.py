import socket
from threading import Thread

SERVER_HOST = "192.168.137.158"  #IP Address disamakan dengan Server

SERVER_PORT = 5002
separator_token = "<SEP>"

name = input("Enter your name: ")
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")

def listen_for_messages():
    while True:
        try:
            message = s.recv(1024).decode()
            if message:
                print("\n" + message)
        except:
            print("[!] Disconnected from server.")
            s.close()
            break

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    msg = input()
    if msg.lower() == 'exit':
        break
    message = f"{name}{separator_token}{msg}"
    s.send(message.encode())

s.close()
print("[-] Connection closed.")
