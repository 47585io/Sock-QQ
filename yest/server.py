import socket
from time import sleep
sock=socket.socket()#)socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 1295))
sock.listen(20)
new_sock,addr=sock.accept()
print("connect!")
while 1:
    new_sock.send("hello".encode())
    sleep(10)
sock.close()
new_sock.close()