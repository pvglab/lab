import socket 

s=socket.socket()
host='192.168.4.222'
port=10007
s.connect((host,port))
while 1:
	msg=raw_input('Send a Message :') 
	s.send(msg)
	print '\n'+s.recv(1024)+'\n'
	if(msg=='exit'):
		break
s.close()


