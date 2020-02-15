import tkinter as tk

app = tk.Tk() 
app.geometry("500x500") #ウィンドウサイズを指定
app.title("sshマクロ自動生成アプリ") #タイトルを指定

var = tk.IntVar() #ラジオボタンのチェック状態を管理する変数
var.set(0) #ラジオボタンにチェックを入れる

key_auth = tk.Radiobutton(app,value=0,variable=var,text="公開鍵認証") #ラジオボタンを作成
key_auth.place(x=100,y=30) #場所を指定
pass_auth = tk.Radiobutton(app,value=1,variable=var,text="パスワード認証")
pass_auth.place(x=300,y=30)

name = tk.Label(app,text="ユーザ名")
name.grid(row=1,column=0,padx=100,pady=100)

name_text = tk.Entry(app)
name_text.grid(row=1,column=1,padx=0,pady=70)

app.mainloop()