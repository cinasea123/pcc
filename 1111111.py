import socket
import threading
def scan(port):
    s = socket.socket()
    s.settimeout(0.1)
    if s.connect_ex(('localhost', port)) == 0:
        print port, 'open'
    s.close()
 
if __name__ == '__main__':
    threads = [threading.Thread(target=scan, args=(i,)) for i in xrange(1,65536)]
    map(lambda x:x.start(),threads)