import socket

if __name__ == '__main__':
	sock = socket.socket()

	port = 1111

	sock.connect(('127.0.0.1', port))
	print(sock.recv(1024))
	sock.close()