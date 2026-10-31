import sqlite3
conn = sqlite3.connect("sqlite.db")
cursor = conn.cursor()
# cursor.execute("create table sample (id integer, name varchar(20))")
# cursor.execute("insert into sample values (2, 'Yash Teki'),(3,'someone')")
resp = cursor.execute("select * from sample")
conn.commit()
print(resp.fetchall())

#recursive cte
#rdd
#sqlalchemy