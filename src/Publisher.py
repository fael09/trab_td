# -*- coding: utf-8 -*-
import socket
import time
import threading
import sys


def conectar():
    tcp.send('CONNECT-TEMP1')
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
        # print ping
        if ping == 'PINGREG':
            tcp.send('PINGRESP_PUB')
        time.sleep(5)
        #print 0
################Publisher############################

def envia_dados():
    while True:
        arquivo = open("htDHT11.txt","r")

        for linha in arquivo:
            print 'Dados: ',linha # dados a serem enviados 
            time.sleep(1)
            tcp.send(linha)
        ref_arquivo.close()


HOST = '0.0.0.0'   # Endereco IP do Servidor
PORT = 30003 # Porta que o Servidor esta
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


while True:
    time.sleep(1)
    print('ok')
tcp.close()