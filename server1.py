import socket
from _thread import *


BACKOLG = 5

def multythreading(client):
    while True :
        data = client.recv(2048)
        if data :
            print("recived from client : %s" % data)
            client.send(data)
    client.close()



sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server_adress = ('localhost' , 10110)

print("server running on %s : %d " % server_adress)

sock.bind(server_adress)
sock.listen(BACKOLG)

###
while True :
    client, address = sock.accept()
    start_new_thread(multythreading,(client,))

sock.close()
