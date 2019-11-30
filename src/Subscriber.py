import socket
import time
import threading



def conectar():
    tcp.send('CONNECT-TEMP2')
    msg_total = tcp.recv(1024)
    if msg_total == 'CONNECT REFUSED':
        print msg_total
        exit()
    msg_con,msg_id = msg_total.split('-') 
    print msg_con,'->',msg_id
    if msg_con == 'CONNACK':
        #print msg_con
        tcp.send('SUBSCRIBE')
        msg_sub = tcp.recv(1024)
        if msg_sub == 'SUBACK':
           print 'SUBACK'
           
    return True

def vericar_conec():
    time.sleep(1)
    while True:
        ping = tcp.recv(7)
        print ping
        if ping == 'PINGREG':
            tcp.send('PINGRESP_SUB')
        time.sleep(1)
        #print 0
################Publisher############################

HOST = '0.0.0.0'   # Endereco IP do Servidor
PORT = 30002 # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print 'Subscriber on-line'


thread_conec = threading.Thread(target=vericar_conec,args=())
thread_conec.daemon = True
thread_conec.start()
conectar()



while True:
    time.sleep(0.5)
tcp.close()