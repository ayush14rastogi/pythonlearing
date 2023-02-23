import socket

s=socket.socket()
#print(s)
s.bind(('localhost',9999))
s.listen(3)

print('waiting for connections')

while True:
    c,addr= s.accept()
    name=c.recv(1024).decode()
    print("connected with ", addr,name)

    c.send(bytes("welcome to telusko",'utf-8',errors="hello"))

    c.close()