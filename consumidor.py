#Lucas Cunha Peres Rodrigues - 83481
import socket
import random

msgconsumida=0


HOST = "127.0.0.1" 
PORT = 5000
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.connect( (HOST,PORT) )
mensagem = "con"
serv.send(mensagem.encode())
msg = serv.recv(1024).decode()
while msgconsumida<100:
    mensagem = str(random.randint(1,10))
    serv.send(mensagem.encode())
    msg = serv.recv(1024).decode()
    
    if(msg!="ok2"):
        msgconsumida=msgconsumida+1
        print("numero de mensagens consumidas " + str(msgconsumida) +" mensagem: "+str(msg))
 



serv.close()
