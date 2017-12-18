import socket

if __name__ == '__main__':
	server = socket.socket()
	print("Created socket successfully")

	port = 1111

	server.bind(('', port))
	print('Socket binded to:', port)

	server.listen(5)
	listening = True

	while listening:
		connection, addr = server.accept()
		threading.Thread(target=)
		connection.send(b"Hey, what's up!")
		connection.close()

	server.close()