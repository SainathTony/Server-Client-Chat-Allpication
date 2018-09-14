from tkinter import *
import socket
import _thread
from pygame import mixer

class ChatBox:
    global message
    message=''
    mixer.init()
    def chat_box(self,a,b):
        self.name='Rani'
        self.root=Tk()

        self.get_sound=mixer.Sound('message_alert.wav')

        HEIGHT=500
        WIDTH=500

        self.root.iconbitmap('icon.ico')
        photo=PhotoImage(file='send_ico.png').subsample(3,4)

        self.root.title('Chat Room')
        self.root.geometry(str(WIDTH)+'x'+str(HEIGHT))

        self.text_area=Text(self.root,height=17,width=40,font=('arial',15,'bold'))
        scroll=Scrollbar(self.root)
        self.text_area.configure(yscrollcommand=scroll.set)
        scroll.configure(command=self.text_area.yview)

        self.entry_box=Entry(self.root,font=('arial',15,'bold'),bg='powder blue',bd=2,width=32)
        self.send=Button(self.root,image=photo,command=self.send_msg_bt,relief='flat')

        self.text_area.place(x=10,y=10)
        scroll.pack(side=RIGHT,fill=Y)
        self.entry_box.place(x=10,y=HEIGHT-50)
        self.send.place(x=(WIDTH-110),y=HEIGHT-55)

        self.enter=self.root.bind("<Return>",self.send_msg)

        self.root.mainloop()

    def client(self,a,b):
        print('client stared')
        self.s=socket.socket()
        port=5000
        host='localhost'

        def getmsg(s):
            while True:
                msg=self.s.recv(1024)
                if msg:
                    print(msg)
                    self.print_recvd_msg(msg)
                else:
                    break
                
        self.s.connect((host,port))
        while True:
            getmsg(self.s)
        self.s.close()

    def print_recvd_msg(self,msg):
        global message
        msg=str(msg)
        msg=msg[2:]
        msg=msg[0:-1]
        message+='\n'+msg
        self.text_area.delete('1.0',END)
        self.text_area.insert(INSERT,message)
        self.get_sound.play()

    def send_msg_bt(self):
        global message
        msg=self.entry_box.get()
        msg=self.name+' : '+msg
        self.s.send(msg.encode())
        message+='\n'+msg
        self.entry_box.delete(0,END)
        self.text_area.delete('1.0',END)
        self.text_area.insert(INSERT,message)

    def send_msg(self,event):
        global message
        msg=self.entry_box.get()
        msg=self.name+' : '+msg
        self.s.send(msg.encode())
        message+='\n'+msg
        self.entry_box.delete(0,END)
        self.text_area.delete('1.0',END)
        self.text_area.insert(INSERT,message)


c=ChatBox()
_thread.start_new_thread(c.chat_box,('',''))
_thread.start_new_thread(c.client,('',''))




