import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import os
import pymysql

conn = pymysql.connect(host='localhost',user='root',password=None,db='pythonTest')
cur = conn.cursor(pymysql.cursors.DictCursor)

def message(text):
    msg = messagebox.showinfo(text,"İşlem tamamlandı.")

def kaydet():
    sql = "INSERT INTO pythontest (name,email,role) VALUES ('%s','%s','%s')" %(Eadi.get(),Eemail.get(),Erole.get())
    cur.execute(sql)
    conn.commit()
    listele()

def guncelle():
    sql = "UPDATE pythontest SET name='%s',email='%s',role='%s' WHERE Id='%s'" %(Eadi.get(),Eemail.get(),Erole.get(),idtxt.get())
    cur.execute(sql)
    conn.commit()
    listele()

def sil():
    sql = "DELETE FROM pythontest WHERE Id=%s" %idtxt.get()
    cur.execute(sql)
    conn.commit()
    listele()

def listele():
    liste.delete(*liste.get_children())
    sql = "SELECT * FROM pythontest"
    cur.execute(sql)
    results = cur.fetchall()

    for rs in results:
        liste.insert("",0,text=rs['id'],values=(rs['adi'],rs['email'],rs['role'],))

def datagetir(event):
    idno=liste.item(liste.selection()[0])['text']
    sql="SELECT * FROM pythontest WHERE Id=%s"%(idno)
    cur.execute(sql)
    results=cur.fetchone()

    idtxt.delete(0,END)
    idtxt.insert(0,results['Id'])

    Eadi.delete(0, END)
    Eadi.insert(0, results['adi'])

    Eemail.delete(0, END)
    Eemail.insert(0, results['email'])

    Erole.delete(0, END)
    Erole.insert(0, results['role'])



top = tkinter.Tk()
top.geometry('500x300')

idtxt = Entry(top,bd=1)
idtxt.place(x=200,y=10)

Ladi = Label(top,text='Adi Soyadi :').place(x=10,y=10)
Eadi = Entry(top, bd=1)
Eadi.place(x = 100, y = 10)

Lemail = Label(top,text='Email : ').place(x=10,y=30)
Eemail = Entry(top, bd=1)
Eemail.place(x = 100, y = 30)

Lrole = Label(top,text='Role : ').place(x=10,y=50)
Erole = ttk.Combobox(top)
Erole['values'] = ('Admin','User','Student')
Eemail.place(x = 100, y = 50)

Kaydet = Button(top,text = "Kaydet",command=kaydet)
Kaydet.place(x = 50, y = 70)

Guncelle = Button(top,text = "Güncelle",command=guncelle)
Guncelle.place(x = 120, y = 70)

Sil = Button(top,text = "Sil",command=sil)
Sil.place(x = 200, y = 70)

liste = ttk.Treeview(top)
liste['columns'] = ("sut1","sut2","sut3")
liste.place(x=0,y=90)
liste.heading("#0",text="Id")
liste.heading("sut1",text="Adi")
liste.heading("sut2",text="Email")
liste.heading("sut3",text="Role")

liste.bind('<ButtonRelease-1>',datagetir)

listele()





top.mainloop()