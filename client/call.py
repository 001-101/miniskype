#Mini-Skype dialer
import socket
import sys

user = sys.argv[1]
peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
peer_address = ('localhost', 550)
print "Connecting to peer..."
peer.connect(peer_address)
print "Requesting user IP address..."
try:
	peer.send("CONNECT " + user)
	while True:
		try:
			ip = peer.recv(15)
		except socket.timeout:
			continue
		break
finally:
    print "%s ==> %s" % (user, ip)
    peer.close()

