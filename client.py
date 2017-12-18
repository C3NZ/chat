import socket

if __name__ == '__main__':
	sock = socket.socket()

	port = 1111

	sock.connect(('localhost', port))
	print(sock.recv(1024).decode())
	sock.close()