import socket
import time

def networking():
	sk = socket.socket()
	server_ip = '127.0.0.1'
	sk.connect((server_ip, 3360))

	#time.sleep(5)

	sk.close()

if __name__ == '__main__':
	networking()
