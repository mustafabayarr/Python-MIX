import os
import pymysql

conn = pymysql.connect(host='localhost',user='root',password=None,db='pythonTest')
cur = conn.cursor()
if cur:
    print("Connection Succcesfully")
else:
    print("Connection Denied.")

sql = "SELECT * FROM pythontest"
cur.execute(sql)
for rs in cur:
    print(rs[0],rs[1])