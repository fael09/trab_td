# -*- coding: utf-8 -*-
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
    
    while True:
        ping = tcp.recv(1024)
        print ping
        if ping == 'PINGREG':
            tcp.send('PINGRESP_SUB')
        time.sleep(5)
        #print 0
################Publisher############################
def recebe_dados():
    while True:
        if tcp:
            msg_dados = tcp.recv(1024)
            print msg_dados
        time.sleep(1)

#####################################################

HOST = '0.0.0.0'   # Endereco IP do Servidor
PORT = 30003 # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print 'Subscriber on-line'
#########################################################
conec = threading.Thread(target=conectar,args=())
conec.daemon = True
conec.start()
#########################################################
#########################################################
v_conec = threading.Thread(target=vericar_conec,args=())
v_conec.daemon = True
v_conec.start()
#########################################################
recv_dados = threading.Thread(target=recebe_dados,args=())
recv_dados.daemon = True
recv_dados.start()
##########################################################



while True:
    time.sleep(0.5)
tcp.close()