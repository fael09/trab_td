# -*- coding: utf-8 -*-
import socket
import time
import threading
import sys


def conectar():
    tcp.send('CONNECT-PUB1')
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
           print 'PUBACK'
           
    return True

def vericar_conec():
    time.sleep(1)
    while True:  
        try:
            tcp.send('')  
        except:
            print 'CONNECTION CLOSED'
            tcp.close()
            exit()
        time.sleep(0.01)
       
################Publisher############################

def envia_dados():
    while True:
        time.sleep(1)
        arquivo = open("htDHT11.txt","r")
        for linha in arquivo:
            try:
                
                tcp.send(linha)
            except:
                pass
            time.sleep(1)
        ref_arquivo.close()


HOST = '0.0.0.0'   # Endereco IP do Servidor
PORT = 30001 # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print 'Subscriber on-line'

#########################################################
v_conec = threading.Thread(target=vericar_conec,args=())
v_conec.daemon = True
v_conec.start()
#########################################################
conec = threading.Thread(target=conectar,args=())
conec.daemon = True
conec.start()
#########################################################
env_dados = threading.Thread(target=envia_dados,args=())
env_dados.daemon = True
env_dados.start()

#menu
while True:
    time.sleep(1)
tcp.close()