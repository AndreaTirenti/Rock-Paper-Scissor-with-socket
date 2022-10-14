import socket       
import sys
import random

host = "127.0.0.1"  
port = 5001


try:
    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_sock.bind((host, port))          
    my_sock.listen(1)                  
except Exception as err:
    print(err)
    sys.exit()
    
    
print("Server listening...")
print("\nROCK PAPER SCISSOR\n")
conn, addr = my_sock.accept()
print (f'\nConnection incoming from... {addr}\n')
while 1:
    data = conn.recv(256)
    if data.decode()=="quit":
        print("PROGRAM ENDED!")
        break
    else:
        data1=input("\nChoose beetwen rock(r), paper(p), scissor(s) -> ")
        if data1=="r" and data.decode()=="r":
            print("\nDraw, you both chose rock\n")
            conn.send("Draw, you both chose rock".encode())
        elif data1=="r" and data.decode()=="p":
            print("\nClient won because chose paper and server rock\n")
            conn.send("Client won because chose paper and server rock".encode())     
        elif data1=="r" and data.decode()=="s":
            print("\nServer won because chose rock and client scissor\n")
            conn.send("Server won because chose rock and client scissor".encode())
        
        elif data1=="p" and data.decode()=="p":
            print("\nDraw, you both chose paper\n")
            conn.send("Draw, you both chose paper".encode())
        elif data1=="p" and data.decode()=="r":
            print("\nServer won because chose paper and client rock\n")
            conn.send("Server won because chose paper and client rock".encode()) 
        elif data1=="p" and data.decode()=="s":
            print("\nClient won because chose scissor and server paper\n")
            conn.send("Client won because chose scissor and server paper".encode())
        
        elif data1=="s" and data.decode()=="s":
            print("\nDraw, you both chose scissor\n")
            conn.send("Draw, you both chose scissor".encode())
        elif data1=="s" and data.decode()=="r":
            print("\nClient won because chose rock and server paper\n")
            conn.send("Client won because chose rock and server paper".encode())
        elif data1=="s" and data.decode()=="p":
            print("\nServer won because chose scissor and client paper\n")
            conn.send("Server won because chose scissor and client paper".encode())
        else:
            print("\nINCORRECT VALUE!\n")
            conn.send("INCRRECT VALUE".encode())
            break
            
            
            
            
conn.close()
my_sock.close()