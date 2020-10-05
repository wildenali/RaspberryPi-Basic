import socket

UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data = "Thank You\n"
addr = ("localhost",5556)
UDPSock.sendto(data,addr)