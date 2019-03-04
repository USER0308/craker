import socket

client = socket.socket()
client.connect(('127.0.0.1',3360))
file = open('from_remote.log', 'w')
result = str(client.recv(4096))
while result:
	print result
	file.write(result)
	result = str(client.recv(4096))
client.close()
#while True:
#	print 'in loop'
#	print client.recv(16)
#	result = str(client.recv(16))
#	print result
