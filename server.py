import socket

if __name__ == '__main__':
	sock = socket.socket()
	print("Created socket successfully")

	port = 1111

	sock.bind(('', port))
	print('Socket binded to:', port)

	sock.listen(5)
	listening = True

	while listening:
		connection, addr = sock.accept()
		connection.send(b"Hey, what's up!")
		connection.close()