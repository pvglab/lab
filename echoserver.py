import socket, struct, fcntl
import ftplib
import socket
import os

IP_ADDR          = "192.168.4.227"

SIOCSIFADDR     = 0x8916
SIOCGIFADDR     = 0x8915

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def setIpAddr(iface, ip):
     bin_ip = socket.inet_aton(ip)
     ifreq = struct.pack('16sH2s4s8s', iface, socket.AF_INET, '\x00'*2, bin_ip, '\x00'*8)
     fcntl.ioctl(sock, SIOCSIFADDR, ifreq)
     return

def getIpAddr(iface = 'eth0'):
     ifreq = struct.pack('16sH14s', iface, socket.AF_INET, '\x00'*14)
     try:
         res = fcntl.ioctl(sock, SIOCGIFADDR, ifreq)
     except:
         return None
         
     ip = struct.unpack('16sH2x4s8x', res)[2]
     return socket.inet_ntoa(ip)

print "Current IP Address: %s" % getIpAddr('eth0')
oldip = getIpAddr('eth0')
if(oldip <> IP_ADDR):
        setIpAddr('eth0', IP_ADDR)

print "Setting IP to: %s" % IP_ADDR
print "New IP Address: %s" % getIpAddr('eth0')
port=10007
sock.bind(('192.168.4.227',port))
sock.listen(10)
while True:
        c, addr=sock.accept()
        print 'Got Connection from',addr
        while 1:
                print 'Message is :'
                m=c.recv(1024)
                print m
                c.send(m)
                if m=='exit':
                        c.close()
                        break
        c.close()






