from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter,tkinter.filedialog
import os



def disable2entry():
    key_text.config(state="disable")
    select_key.config(state="disable")

def enable2entry():
    key_text.config(state="enable")
    select_key.config(state="enable")

def search2file():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    key_entry = file
    key_text.insert(tkinter.END,key_entry)
    
def search2dir():
    iDir = os.path.abspath(os.path.dirname(__file__))
    dir = tkinter.filedialog.askdirectory(initialdir = iDir) 
    out_entry = dir
    out_text.insert(tkinter.END,out_entry)

def output():
    with open(out_text.get() + "/" + ttl_text.get() + ".dat",mode="w"):
        pass
    if var.get() == 0:
        with open(out_text.get()+ "/" +ttl_text.get()+".ttl",mode="w") as f:
            f.write("username = '{}'\n".format(user_text.get()))
            f.write("hostname = '{}'\n".format(IP_text.get()))
            f.write("keyfile = '{}'\n".format(key_text.get()))
            f.write("passwdfile = './{}'\n".format(ttl_text.get() + ".dat"))
            f.write("msg = 'Enter password for user'\n")
            f.write("strconcat msg username\n")
            f.write("passwdkey = username\n")
            f.write("strconcat passwdkey '@'\n")
            f.write("strconcat passwdkey hostname\n")
            f.write("getpassword passwdfile passwdkey password\n")
            f.write("msg = hostname\n")
            f.write("strconcat msg ':{} /ssh /auth=publickey /user='\n".format(port_text.get()))
            f.write("strconcat msg username\n")
            f.write("strconcat msg ' /keyfile='\n")
            f.write("strconcat msg keyfile\n")
            f.write("strconcat msg ' /passwd='\n")
            f.write("strconcat msg password\n")
            f.write("connect msg")
    else:
        with open(out_text.get()+ "/" +ttl_text.get()+".ttl",mode="w") as f:
            f.write("username = '{}'\n".format(user_text.get()))
            f.write("hostname = '{}'\n".format(IP_text.get()))
            f.write("passwdfile = './{}'\n".format(ttl_text.get() + ".dat"))
            f.write("msg = 'Enter password for user'\n")
            f.write("strconcat msg username\n")
            f.write("passwd = username\n")
            f.write("strconcat passwd '@'\n")
            f.write("strconcat passwd hostname\n")
            f.write("getpassword passwdfile passwd password\n")
            f.write("msg = hostname\n")
            f.write("strconcat msg ':{} /ssh /auth=password /user='\n".format(port_text.get()))
            f.write("strconcat msg username\n")
            f.write("strconcat msg ' /passwd='\n")
            f.write("strconcat msg password\n")
            f.write("connect msg")
    messagebox.showinfo("出力","出力しました") 

        
root = Tk()
root.title('sshマクロ')

# Frame
frame = ttk.Frame(root,padding=30)
frame.grid()

# ラジオボタン判定
var = tkinter.IntVar()
var.set(0)

# auth way
lf = ttk.Labelframe(
    frame, 
    text='認証方式',
    padding=5)
lf.grid(row=0,column=1)

#key
key_button = ttk.Radiobutton(
    lf,
    text='公開鍵認証',
    value=0,
    variable=var,
    command=enable2entry)
key_button.grid(row=0,column=0)

#pass
password_button = ttk.Radiobutton(
    lf,
    text='パスワード認証',
    value=1,
    variable=var,
    command=disable2entry)
password_button.grid(row=0,column=1)

#user_label
user_label = ttk.Label(
    frame,
    text='ユーザ名',
)

#IP_label
IP_label = ttk.Label(
    frame,
    text='IPアドレス',
)

#公開鍵path
key_label = ttk.Label(
    frame,
    text='公開鍵path',
)

#出力先
out_label = ttk.Label(
    frame,
    text='出力先',
)

#ポート
port_label = ttk.Label(
    frame,
    text='ポート',
)

#ttlファイル名
ttl_label = ttk.Label(
    frame,
    text='ttlファイル名',
)


user_label.grid(row=1,column=0)
IP_label.grid(row=2,column=0)
key_label.grid(row=3,column=0)
out_label.grid(row=4,column=0)
port_label.grid(row=5,column=0)
ttl_label.grid(row=6,column=0)


user_entry = StringVar()
pass_entry = StringVar()
IP_entry = StringVar()
key_entry = StringVar()
out_entry = StringVar()
port_entry = StringVar()
ttl_entry = StringVar()

user_text = ttk.Entry(
    frame,
    textvariable=user_entry,
    width=20
)

IP_text = ttk.Entry(
    frame,
    textvariable=IP_entry,
    width=20
)

key_text = ttk.Entry(
    frame,
    textvariable=key_entry,
    width=20
)


out_text = ttk.Entry(
    frame,
    textvariable=out_entry,
    width=20
)

port_text = ttk.Entry(
    frame,
    textvariable=port_entry,
    width=20
)

ttl_text = ttk.Entry(
    frame,
    textvariable=ttl_entry,
    width=20
)


user_text.grid(row=1,column=1,pady=10)
IP_text.grid(row=2,column=1,pady=10)
key_text.grid(row=3,column=1,pady=10)
out_text.grid(row=4,column=1,pady=10)
port_text.grid(row=5,column=1,pady=10)
ttl_text.grid(row=6,column=1,pady=10)

decide = ttk.Button(
    frame,
    text='出力',
    command=output)
decide.grid(row=9,column=1)

select_key = ttk.Button(
    frame,
    text="エクスプローラを開く",
    command=search2file
)

select_out = ttk.Button(
    frame,
    text="エクスプローラを開く",
    command=search2dir
)

select_key.grid(row=3,column=2)
select_out.grid(row=4,column=2)
root.mainloop()