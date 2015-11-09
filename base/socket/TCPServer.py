#!/usr/bin/env python

#TCP时间戳服务器
#创建一个能接受客户端消息,在消息前加一个时间戳或返回的TCP服务器

from socket import *
from time import ctime

HOST=''
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
  print 'waiting for connection ...'
  tcpCliSock,addr=tcpSerSock.accept()
  print '... connected from : ',addr

  while True:
    data=tcpCliSock.recv(BUFSIZE)
    if not data: break
    tcpCliSock.send('[%s] %s' % (ctime(),data))
  tcpCliSock.close()

tcpSerSock.close()