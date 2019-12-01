# -*- coding: utf-8 -*-
import socket
import threading
import time
import os


all_connections = []
# função que realixa a conexao e desconexao de nos cliestes (publisher e subscriber)
def conectar():
    global msg_id
    global con
    
    while True:
        print'Broker on-line!'
        con, cliente = tcp.accept()
        
        ip,id_con = cliente
       
        msg_total = con.recv(1024)
        # print msg_total
        
        msg_con, msg_id = msg_total.split('-')

        client_id = 'ok'
        if msg_con == 'CONNECT':
            ###################################
            for i in range(0, len(lista_de_clientes)):
                if lista_de_clientes[i] == msg_id:
                    con.send('CONNECT REFUSED')
                    print 'CONNECT REFUSED'
                    client_id = 'no'
                    break
                        
            ###################################
            if client_id == 'ok':
                all_connections.append(con)
                lista_de_clientes.append(msg_id)
                print msg_con,'->',msg_id
                con.send('CONNACK'+'-'+ msg_id)
                msg_sub = con.recv(1024)
                if msg_sub == 'SUBSCRIBE':
                    print msg_sub 
                    con.send('SUBACK')
                # print lista_de_clientes        

# função de ferificacao das conexoes
def vericar_conec():
    
    while True:
        
        if (len(lista_de_clientes) >=1):
            
            for i in range(0,len(all_connections)):
                try:
                    
                    all_connections[i].send(' ')    
                         
                except:
                    print 'DISCONNECT', lista_de_clientes[i+1]
                    all_connections[i].close()
                    del all_connections[i]
                    del lista_de_clientes[i+1]
                    break
                    try:
                        pass
                    except:
                        pass
        time.sleep(0.01)
# função que recebe os dados dos publisher
def recebe_dados():
    global msg_dados
    while True:
        i  = 0
        # print lista_de_clientes
         
        if len(all_connections) > 0:
            while i < len(all_connections):
                
                if (i + 0) >= len(all_connections):
                    break
                if lista_de_clientes[i+1][0] == 'P': # he um publisher
                    if (i + 0) >= len(all_connections):
                        break
                    msg_dados = all_connections[i].recv(1024)
                    if (i + 0) >= len(all_connections):
                        break
                    #print 'recebendo ...'
                if lista_de_clientes[i+1][0] == 'S': # he um subscriber 
                    if (i + 0) >= len(all_connections):
                        break
                    for j in range(0,len(all_connections)):
                        if lista_de_clientes[j+1][0] == 'P':
                            all_connections[i].send(msg_dados)
                            break
                    if (i + 0) >= len(all_connections):
                        break
                    #print 'enviando ...'
                
                i = 1+i
        
        time.sleep(1)

###########################################################
# Inicio do Broker#########################################
HOST = ''              # Endereco IP do Servidor
PORT = 30001    # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(10)
lock = threading.Lock()
msg_dados = ['Humidity: 46.00%  Temperature: 24.00°C 75.20°F']
##################  ###########
lista_de_clientes = ["Boker"] # inicialmente vazia
#############################
###########################################################
# Thread que gerencia as novas conexoes e aloca os topicos
thread_conec = threading.Thread(target=conectar,args=())
thread_conec.daemon = True
thread_conec.start()
###########################################################
###########################################################
#Thread que gerencia o estado das conexoes
v_conec = threading.Thread(target=vericar_conec,args=())
v_conec.daemon = True
v_conec.start()
########################################################
#Thread que recebe os dados 
recv_dados = threading.Thread(target=recebe_dados,args=())
recv_dados.daemon = True
recv_dados.start()
###########################################################
#meno de visualizacao
while True:
    if len(all_connections) > 0:
        print 'Dugite 1 para ver a lista de clientes'
        print 'Digite 2 para ver as mensagens'
        ent = input()
        if ent == 1:
            print 'Lista de clientes: ', lista_de_clientes
        elif ent == 2:
            print 'Dados: ', msg_dados
        else:
            print 'Entrada invalida'
    time.sleep(0.5)    
con.close()