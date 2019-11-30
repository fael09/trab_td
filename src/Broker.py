# -*- coding: utf-8 -*-
import socket
import threading
import time

all_connections = []

def conectar():
    global msg_id
    global con
    
    while True:
        print'Broker on-line!'
        con, cliente = tcp.accept()
        
         # lista de todas as conexoes
        #print 'depois de accept'
        ip,id_con = cliente
       
        msg_total = con.recv(1024)
        
        
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
                print lista_de_clientes        
            
        
    

def vericar_conec():
    
    while True:
        # print lista_de_clientes
        if (len(lista_de_clientes) >=1):
            #print lista_de_clientes
            
            for i in range(0,len(all_connections)):
                
               
                try:
                    all_connections[i].send('PINGREG')
                    echo = all_connections[i].recv(1024)
                    #print echo
                    #
                except:
                    
                    all_connections[i].close()
                    del all_connections[i]
                    # print "Topico Deletado:", lista_de_clientes[i+1]
                    del lista_de_clientes[i+1]
                    break
                    try:
                        pass
                    except:
                        pass
               
        time.sleep(0.01)


def recebe_dados():

    while True:
        if len(all_connections) > 0:
            msg_dados = all_connections[0].recv(1024)
            if len(all_connections) > 1:
                all_connections[1].send(msg_dados)
            print msg_dados
        time.sleep(1)


        
    
###########################################################
# Inicio do Broker#########################################
HOST = ''              # Endereco IP do Servidor
PORT = 30003    # Porta que o Servidor esta
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
thread_conec = threading.Thread(target=conectar,args=())
thread_conec.daemon = True
thread_conec.start()

###########################################################
###########################################################
v_conec = threading.Thread(target=vericar_conec,args=())
v_conec.daemon = True
v_conec.start()
########################################################
recv_dados = threading.Thread(target=recebe_dados,args=())
recv_dados.daemon = True
recv_dados.start()
###########################################################






#conectar()
while True:
    time.sleep(0.5)    
con.close()