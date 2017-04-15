#Mini-Skype registration
import socket
import sys

user = sys.argv[1]
ip = "123.45.67.89"
peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
peer_address = ('localhost', 550)
print "Connecting to peer..."
peer.connect(peer_address)
print "Sending current IP address..."
try:
	peer.sendall("REGISTER " + user + " " + ip)
	reply = peer.recv(32)
finally:
    print "%s <== %s ==> %s" % (user, reply, ip)
    peer.close()

