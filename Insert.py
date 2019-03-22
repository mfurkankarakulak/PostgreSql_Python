# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 13:53:50 2019

@author: furkan.karakulak
"""
"""
import psycopg2
	
conn = psycopg2.connect("dbname=python user=postgres password=123")
	
cur = conn.cursor()

sql = " INSERT INTO giris ( name , lastname ) VALUES ( 'Mustafa Furkan Karakulak' , 'Karakulak' );"

cur.execute(sql)
conn.commit()
cur.close()
conn.close()
"""
import psycopg2

 
 
def insert_giris():
    """ insert a new vendor into the vendors table """
    sql = "INSERT INTO giris ( name , lastname ) VALUES ( 'Onur' , 'Karakulak' );"
    conn = None
    connStr = "dbname=python user=postgres password=123"
    try:
        
        # connect to the PostgreSQL database
        conn = psycopg2.connect(connStr)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 

insert_giris()
