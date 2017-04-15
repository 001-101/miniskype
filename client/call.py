#Mini-Skype dialer
import socket
import sys

user = sys.argv[1]
peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create TCP socket / Socket létrehozása
peer_address = ('localhost', 550)
print "Connecting to peer..."
peer.connect(peer_address) #Connect to the peer / Kapcsolódás a peer-hez
print "Requesting user IP address..."
try:
	peer.send("CONNECT " + user) #Send connection request to the peer / Kapcsolódási kérelem küldése a peer-nek
	while True:
		try:
			ip = peer.recv(15) #Receive 15 bytes / 15 bájtnyi (vagy kevesebb) adat fogadása (IP cím)
		except socket.timeout:
			continue
		break
finally:
    print "%s ==> %s" % (user, ip)
    peer.close()

