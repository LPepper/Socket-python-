from socket import *
from time import ctime
from time import localtime
import time


HOST=''
PORT=1122  #设置侦听端口
BUFSIZ=1024
ADDR=(HOST, PORT)
sock=socket(AF_INET, SOCK_STREAM)

sock.bind(ADDR)

sock.listen(5)
#设置退出条件
STOP_CHAT=False
while not STOP_CHAT:
    print('等待接入，侦听端口:%d' % (PORT))
    tcpClientSock, addr=sock.accept()
    print('接受连接，客户端地址：',addr)
    while True:
        try:
            data=tcpClientSock.recv(BUFSIZ)
        except:
            #print(e)
            tcpClientSock.close()
            break
        if not data:
            break


        ISOTIMEFORMAT='%Y-%m-%d %X'
        stime=time.strftime(ISOTIMEFORMAT, localtime())
        s='服务器：%s' %(data.decode('utf8').upper())
        tcpClientSock.send(s.encode('utf8'))
        print([stime], ':', data.decode('utf8'))
        #如果输入quit(忽略大小写),则程序退出
        STOP_CHAT=(data.decode('utf8').upper()=="QUIT")
        if STOP_CHAT:
            break
tcpClientSock.close()
sock.close()