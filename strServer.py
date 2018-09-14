import socket
import _thread

host='localhost'
port=5000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)
print(s,"\nServer started on port",port)
list_clients=[]

def broadcaste(message,conn,addr):
    for clients in list_clients:
        if clients!=conn:
            print("Sending msg to",addr," : ",message)
            #message=str(addr)+str(message)
            try:
                clients.send(message)
            except Exception:
                print('cant send message to ',clients)

def clientthread(con,addr):
    con.send(("Welcome to chatbox").encode())
    while True:
        msg=''
        try:
            msg=con.recv(1024)
        except Exception:
            print(addr," is disconnected")
        if msg:
            print(addr,"==>",msg)
            broadcaste(msg,con,addr)
        else:
            break
            
while True:
    conn,addr=s.accept()
    list_clients.append(conn)
    print("Got connection from ",conn)
    _thread.start_new_thread(clientthread,(conn,addr))
s.close()
