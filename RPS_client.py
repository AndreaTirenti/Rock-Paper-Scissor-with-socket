import socket       
import sys

host = "127.0.0.1"
port = 5001


try:
    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_sock.connect((host, port))       
except Exception as err:
    print(err)
    sys.exit()
print("Connection establioshed with success...")
print("\nROCK PAPER SCISSOR\n")

while 1:
    data=input("\nChoose beetwen rock(r), paper(p), scissor(s) -> ")
    my_sock.send(data.encode())
    if data=="quit":
        print("PROGRAM ENDED!")
        break
    data = my_sock.recv(256)
    print(f"\n{data.decode()}\n")


my_sock.close()