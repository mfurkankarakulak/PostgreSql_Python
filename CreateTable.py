# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:10:36 2019

@author: furkan.karakulak
"""

import psycopg2
	
conn = psycopg2.connect("dbname=python user=postgres password=123")
	
cur = conn.cursor()

sql = """ CREATE TABLE table_name (
            column_name VARCHAR (50),
            table_constraint VARCHAR (50)
            ) ;"""

cur.execute(sql)
conn.commit()
cur.close()
conn.close()