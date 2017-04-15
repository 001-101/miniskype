#Mini-Skype peer
import socket
import os

os.system('cls' if os.name == 'nt' else 'clear')
ttyheight, ttywidth = os.popen('stty size', 'r').read().split()
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
address = ('localhost', 550)
print '\n'.join(('{:^'+ttywidth+'}').format(s) for s in "Mini-Skype 2017 v1.0".split('\n'))
print "Starting server on %s:%s..." % address
listener.bind(address)
print "Waiting for connections..."
listener.settimeout(1)
listener.listen(1)

while True:
	try:
		connection, cli_address = listener.accept()
	except socket.timeout:
		continue
	except KeyboardInterrupt:
		print "User shutdown requested"
		break
	print "Client connected: %s:%s" % cli_address
	try:
		while True:
			request = connection.recv(128)
			if request:
				break
		if request.split()[0] == "CONNECT":
			users = {}
			with open("users.txt") as file:
				for user in file:
					username, ipaddress = line.partition("=")[::2]
					users[username.strip()] = ipaddress
			print "CONNECT " + request.split()[1] + " ==> " + users[request.split()[1]]
		elif request.split()[0] == "REGISTER":
			print "REGISTER " + request.split()[1] + " ==> " + request.split()[2]
			with open("users.txt", "a") as file:
				file.write(request.split()[1] + "=" + request.split()[2] + "\n")
			connection.send("OK")
	finally:
		connection.close()
listener.close()
