import socket
import threading
import time

def conectar():
    global msg_id
    while True:
        con, cliente = tcp.accept()
        msg_total = con.recv(1024)
        msg_id, msg_con = msg_total.split('-')
        print 'Client_ID: ', msg_id
        time.sleep(3) 
        if msg_con == 'CONNECT':
            print msg_con
            con.send('CONNACK')
        
            msg_sub = con.recv(1024)
            if msg_sub == 'SUBSCRIBE':
                print msg_sub 
                con.send('SUBACK')
                break
    con.close()
    return True

###########################################################
# Inicio do Broker#########################################
HOST = ''              # Endereco IP do Servidor
PORT = 5000         # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(2)

print 'Broker on-line!'
# thread_conec = threading.Thread(target=conectar,args=())
# thread_conec.start()
# thread_conec.join() 
conectar()




# while True:
#     # con, cliente = tcp.accept()
#     # print 'Concetado por', cliente
#     while True:
#         msg = con.recv(1024)
#         if msg == 'CONNECT':
#             print msg 
#             con.send('CONNACK')
#         if not msg: break
#         #print cliente, msg
#     # print 'Finalizando conexao do cliente', cliente
