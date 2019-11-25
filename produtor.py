#Lucas Cunha Peres Rodrigues - 83481
import socket
import random

msgenviada=0;


HOST = "127.0.0.1" 
PORT = 5000
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.connect( (HOST,PORT) )
mensagem = "prod"
serv.send(mensagem.encode())


msg = serv.recv(1024).decode()
print(msg)
while msgenviada<100:
    mensagem = str(random.randint(1,10))
    print("mensagem enviada " + str(mensagem))

    serv.send(mensagem.encode())
    msg = serv.recv(1024).decode()
    print("msg enviada numero "+ str(msgenviada))
    if(msg!="ok2"):
            msgenviada=msgenviada+1


msg = serv.recv(1024).decode()


serv.close()
