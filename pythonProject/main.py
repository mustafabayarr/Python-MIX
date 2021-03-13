import os
import pymysql

conn = pymysql.connect(host='localhost',user='root',password=None,db='test')
cur = conn.cursor()
if cur:
    print("Connection Succcesfully")
else:
    print("Connection Denied.")

