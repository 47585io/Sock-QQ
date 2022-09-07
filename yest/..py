import socket
sock=socket.socket()#socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)
sock.connect(("127.0.0.1",1295))
print("exit")
while 1:   
    s=sock.recv(1024)
    print(s)
sock.close()