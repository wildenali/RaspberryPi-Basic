import socket

UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Listen on port 5556 (to all IP addresses on this system)
listen_addr = ("",5556)
UDPSock.bind(listen_addr)

while True:
    data,addr = UDPSock.recvfrom(1024)
    print data.strip(),addr
    UDPSock.sendto("OK\n", addr)