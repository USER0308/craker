
import socket


def networking():
	sk = socket.socket()
	sk.bind(('', 3360))
	sk.listen(3)
	while True:
#		logging.info('in while loop')
		conn, address = sk.accept()
		# change logging position
		print(address[0])

		#file = open('iplogger.log', 'a')

		#file.write(address)
		conn.close()

if  __name__ == '__main__':
	networking()
