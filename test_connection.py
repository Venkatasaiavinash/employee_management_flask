from db import get_connection

conn=get_connection()
cursor=conn.cursor()
cursor.execute("SELECT COUNT(*) FROM Employees")
print("Connected! Employees in table:",cursor.fetchone()[0])
conn.close()