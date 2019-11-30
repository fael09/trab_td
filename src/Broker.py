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
    time.sleep(1)
    while True:
        print lista_de_clientes
        if (len(lista_de_clientes) >=1):
            #print lista_de_clientes
            
            for i in range(0,len(all_connections)):
                
               
                try:
                    all_connections[i].send('PINGREG')
                    echo = all_connections[i].recv(12)
                    #
                except:
                    
                    all_connections[i].close()
                    del all_connections[i]
                    print "Topico Deletádo:", lista_de_clientes[i+1]
                    del lista_de_clientes[i+1]
                    break
                    try:
                        pass
                    except:
                        pass
                      

                        
        time.sleep(0.5)

   
        
    
###########################################################
# Inicio do Broker#########################################
HOST = ''              # Endereco IP do Servidor
PORT = 30002    # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(10)

##################  ###########
lista_de_clientes = ["Boker"] # inicialmente vazia
#############################
#print 'Broker on-line!'


thread_conec = threading.Thread(target=vericar_conec,args=())
thread_conec.daemon = True
thread_conec.start()

conectar()

#conectar()
while True:
    time.sleep(0.5)    
con.close()