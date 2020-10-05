import socket
import threading
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

def sockReceive():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    lock.acquire()
    print "Connect to Server"
    lock.release()

    while True:
        s.send(MESSAGE)
        data = s.recv(BUFFER_SIZE)
        lock.acquire()
        print "received data:", data
        lock.release()
        s.close()

def printConsole():    
    while True:
        lock.acquire()
        print MESSAGE
        lock.release()
        time.sleep(2)

lock = threading.Lock()

thread1 = threading.Thread(target = sockReceive)
thread1.daemon = True
thread1.start()

thread2 = threading.Thread(target = printConsole)
thread2.daemon = True
thread2.start()

while True:
    time.sleep(0.1)