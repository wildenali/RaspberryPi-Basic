import socket

BUFFER_SIZE = 20    # normally 1924, but we want fast response

print 'TCP Server...'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 5005))
s.listen(1) # Listen 1 client
conn, addr = s.accept()
print 'Connection address: ', addr

while True:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    print "received data: ", data

conn.send(data) # echo
conn.close()