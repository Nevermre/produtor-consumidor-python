#Lucas Cunha Peres Rodrigues - 83481
import socket
import select
import random


place=[0,0,0,0,0,0,0,0,0,0]
enter=0
saida=0
count = 0
contador=0



HOST,PORT = "",5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind( (HOST,PORT) )
tcp.listen(5)

for _ in range(0,2):
    con, cliente = tcp.accept()
    if con.recv(4).decode() == 'prod':
        prod=con
    else:
        cons=con
    
  



inputs=[prod,cons]
prod.send("ok".encode())
cons.send("ok".encode())


while True:
    if count>0 and count <10:
        
        entrada,_,erro=select.select(inputs,[],inputs)
        con = entrada[random.randint(0,len(entrada)-1)]
        msg = con.recv(1024)
        if con is prod:
            print("recebeu do produtor")
            place[enter%10 ]=msg
            prod.send("ok".encode())
            
            enter=enter+1
            count = count+1
        else:
            print("consumidor")
            anterior = place[saida%10 ]
            place[saida%10 ]=0
            cons.send(str(anterior).encode())
            saida=saida+1
            count = count-1
            
            contador=contador+1
    
    elif count==0:
        entrada,_,erro=select.select(inputs,[],inputs)
        con = entrada[random.randint(0,len(entrada)-1)]
        msg = con.recv(1024)
        if con is prod:
            print("recebeu do produtor")
            place[enter%10 ]=msg
            prod.send("ok".encode())
            enter=enter+1
            count = count+1
        else:
             if(contador==100):
                print("O programa terminou, todas as 100 mensagens foram produzidas e consumidas ")
                break
             cons.send("ok2".encode())
    elif count==10:
        entrada,_,erro=select.select(inputs,[],inputs)
        con = entrada[random.randint(0,len(entrada)-1)]
        msg = con.recv(1024)
        if con is cons:
            print("consumidor")
            anterior = place[saida%10 ]
            place[saida%10 ]=0
            cons.send(str(anterior).encode())
            saida=saida+1
            count = count-1
            
            contador=contador+1
        else:
             prod.send("ok2".encode())
    print(place)



tcp.close()
