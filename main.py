from tkinter import *
from tkinter import ttk


root = Tk()
root.title('sshマクロ')

# Frame
frame = ttk.Frame(root,padding=30)
frame.grid()

# Label Frame
lf = ttk.Labelframe(
    frame, 
    text='認証方式',
    padding=5)
lf.grid(row=0,column=0,pady=5)

#Radiobutton 1
key_button = ttk.Radiobutton(
    lf,
    text='公開鍵認証',
    value='A')
key_button.grid(row=0,column=0)

#Radiobutton 2
password_button = ttk.Radiobutton(
    lf,
    text='パスワード認証',
    value='B')
password_button.grid(row=0,column=1)


root.mainloop()