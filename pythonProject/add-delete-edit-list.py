import os
import pymysql

conn = pymysql.connect(host='localhost',user='root',password=None,db='pythonTest')
cur = conn.cursor(pymysql.cursors.DictCursor)


def giris():
    print("Bilgi Giriş")
    name=input("Ad ve Soyad Gir : ")
    email = input("Email Gir : ")
    role = input("Rol Gir : ")
    ekle(name,email,role)
def ekle(name,email,role):
    sql = "INSERT INTO pythontest (name,email,role) VALUES ('%s','%s','%s')" %(name,email,role)
    cur.execute(sql)
    conn.commit()
    listele()

def listele():
    sql = "SELECT * FROM pythontest"
    cur.execute(sql)
    results = cur.fetchall()
    for rs in results:
        print(rs['id'],rs['name'],rs['email'],rs['role'])

def sil(id):
    sql = "DELETE FROM pythontest WHERE id = %s " % id
    cur.execute(sql)
    conn.commit()
    listele()

def duzenle(id):
    sql = "SELECT * FROM pythontest WHERE id = %s" % id
    cur.execute(sql)
    rs = cur.fetchone()
    print(rs['id'], rs['name'], rs['email'], rs['role'])

    name = input("Ad ve Soyad Gir : ")
    email = input("Email Gir : ")
    role = input("Rol Gir : ")
    guncelle(name, email, role,id)
    listele()

def guncelle(name,email,role,id):
    sql = "UPDATE pythontest SET name = '%s', email = '%s', role = '%s' WHERE id = %s" % (name,email,role,id)
    cur.execute(sql)
    conn.commit()
    listele()



sec=99
clear = lambda :os.system('cls')
clear()
while(sec!=0):
    print(" | 1 Kayıt giriş |")
    print(" | 2 Listele     |")
    print(" | 3 Sil         |")
    print(" | 4 Düzenle     |")
    print(" | 0 Çıkış       |")
    sec=int(input('Seçenek giriniz : '))
    if sec==1:
        clear()
        giris()
    elif sec==2:
        clear()
        listele()
    elif sec == 3:
        clear()
        listele()
        id = input("Silinecek ID gir : ")
        sil(id)
    elif sec == 4:
        clear()
        listele()
        id = input("Düzenlenecek ID gir : ")
        duzenle(id)



