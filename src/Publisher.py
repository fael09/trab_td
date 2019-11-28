import socket
import time




def conectar(tcp):
    tcp.send('temp1-CONNECT')
    msg_con = tcp.recv(1024)
    if msg_con == 'CONNACK':
        print msg_con
        tcp.send('SUBSCRIBE')
        msg_sub = tcp.recv(1024)
        if msg_sub == 'SUBACK':
            print 'SUBACK'
    return True
def mandar_msg():

    return True

################Publisher############################

HOST = '127.0.0.1'   # Endereco IP do Servidor
PORT = 5000    # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print 'Subscrober on-line'

conectar(tcp)
mandar_msg()

# while True:
#     msg = raw_input()
#     tcp.send (msg)
tcp.close()