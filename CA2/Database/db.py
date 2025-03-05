import sqlite3

conn=sqlite3.connect("./CA2/Database/weather")
cur=conn.cursor()
cur.execute("CREATE TABLE userCities(id INTEGER PRIMARY KEY AUTOINCREMENT,city VARCHAR NOT NULL,latitude FLOAT NOT NULL,longitude FLOAT NOT NULL,temp FLOAT NOT NULL,max_temp FLOAT NOT NULL,min_temp FLOAT NOT NULL)")
conn.commit()
conn.close()