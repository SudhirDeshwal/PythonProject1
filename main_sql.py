#  Dictionary Project using SQL

import mysql.connector

con = mysql.connector.connect(
    
    user = "root",
    password = "",
    host = "127.0.0.1",
    port = '3307',
    database = "lab_4_n01324321"

)

cursor = con.cursor()
word = input("Enter a word : ")
query = cursor.execute("SELECT * FROM sudhir Where ID = '%s' " % word)
results = cursor.fetchall()

for i in results:
     print(i[1])



