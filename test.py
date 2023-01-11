import mysql.connector
import pandas as pd
data=pd.read_csv('glass.data')
# data.head()
mydb=mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)
mycursor=mydb.cursor()
mycursor.execute('create database glass')
print("database created")
mycursor.execute("""CREATE TABLE glass.glass_data (ind INT, RI DOUBLE , Na DOUBLE, Mg DOUBLE,Al DOUBLE, Si DOUBLE, K DOUBLE, Ca DOUBLE, Ba DOUBLE, Fe DOUBLE, lass INT)""")
for i,row in data.iterrows():
    sql = "INSERT INTO glass.glass_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    mydb.commit()
    print("Record inserted")
mycursor.execute("select * from glass.glass_data")
for x in mycursor:
    print(x)