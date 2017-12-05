import socket
port=8081
host='localhost'

str=input("请输入")

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto(str.encode('utf-8'),(host,port))

data=s.recv(1024)

print('Received',data,'from the Server')

