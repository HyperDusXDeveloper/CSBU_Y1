import sqlite3
conn = sqlite3.connect('db_1670700044.db')
cursor = conn.cursor()
sql = "select * from member where mid=1002"
cursor.execute(sql)
result = cursor.fetchall()#fetcall
print(result[0][2])

conn.close()
