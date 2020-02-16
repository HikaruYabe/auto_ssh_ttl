from tkinter import *
from tkinter import ttk
import tkinter,tkinter.filedialog
import os

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

root = Tk()
root.title('sshマクロ')

# Frame
frame = ttk.Frame(root,padding=30)
frame.grid()

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
    value='A')
key_button.grid(row=0,column=0)

#pass
password_button = ttk.Radiobutton(
    lf,
    text='パスワード認証',
    value='B')
password_button.grid(row=0,column=1)

#user_label
user_label = ttk.Label(
    frame,
    text='ユーザ名',
)


#pass_label
pass_label = ttk.Label(
    frame,
    text='パスワード',
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
    text='ttkファイル名',
)

#datファイル名
dat_label = ttk.Label(
    frame,
    text='datファイル名',
)

user_label.grid(row=1,column=0)
pass_label.grid(row=2,column=0)
IP_label.grid(row=3,column=0)
key_label.grid(row=4,column=0)
out_label.grid(row=5,column=0)
port_label.grid(row=6,column=0)
ttl_label.grid(row=7,column=0)
dat_label.grid(row=8,column=0)


user_entry = StringVar()
pass_entry = StringVar()
IP_entry = StringVar()
key_entry = StringVar()
out_entry = StringVar()
port_entry = StringVar()
ttl_entry = StringVar()
dat_entry = StringVar()

user_text = ttk.Entry(
    frame,
    textvariable=user_entry,
    width=20
)

pass_text = ttk.Entry(
    frame,
    textvariable=pass_entry,
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

dat_text = ttk.Entry(
    frame,
    textvariable=dat_entry,
    width=20
)

user_text.grid(row=1,column=1,pady=10)
pass_text.grid(row=2,column=1,pady=10)
IP_text.grid(row=3,column=1,pady=10)
key_text.grid(row=4,column=1,pady=10)
out_text.grid(row=5,column=1,pady=10)
port_text.grid(row=6,column=1,pady=10)
ttl_text.grid(row=7,column=1,pady=10)
dat_text.grid(row=8,column=1,pady=10)

decide = ttk.Button(
    frame,
    text='出力')
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

select_key.grid(row=4,column=2)
select_out.grid(row=5,column=2)
root.mainloop()