# -*- coding: utf-8 -*-
import socket
import time
import threading


# função que realixa a conexao ao broker
def conectar():
    tcp.send('CONNECT-SUB1')
    msg_total = tcp.recv(1024)
    if msg_total == 'CONNECT REFUSED':
        print msg_total
        exit()
    msg_con,msg_id = msg_total.split('-') 
    #print msg_con,'->',msg_id
    if msg_con == 'CONNACK':
        #print msg_con
        tcp.send('SUBSCRIBE')
        msg_sub = tcp.recv(1024)
        if msg_sub == 'SUBACK':
           print 'SUBACK'
           
    return True
# função de ferificacao da conexao
def vericar_conec():
    time.sleep(1)
    while True:
        try :
           tcp.send(' ')
        except:
            print 'CONNECTION CLOSED'
            tcp.close()
            exit()
        time.sleep(0.01)
#função que recebe os dados do broker
def recebe_dados():
    tempo = 0
    while True:
        try:
            msg_dados = tcp.recv(1024)
        except:
            exit()
        if msg_dados[0] == ' ':
            tempo = 0.005
        else:
            tempo = 0.5
            print msg_dados

        time.sleep(tempo)

#####################################################
################Publisher############################
HOST = '0.0.0.0'   # Endereco IP do Servidor
PORT = 30001 # Porta que o Servidor esta
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
# menu
while True:
     time.sleep(0.5)
tcp.close()