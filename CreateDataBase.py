import psycopg2
	
conn = psycopg2.connect("dbname=python user=postgres password=123")
	
cur = conn.cursor()

sql = """ CREATE TABLE MyDbPythons ;"""

cur.execute(sql)
conn.commit()
cur.close()
conn.close()