from wsgiref import headers
import pandas as pd
from dbmodule import connect

url = ""
df = pd.read_csv(url, header=None)
df.head()
df.columns = headers
# path = "" #path to save in PC
# df.to_csv(path) #to save in path
# df.dtypes #to check data types
# df.describe(include="all") #for statistical summary


###Conection to DB###
connection = connect("databasename", "username", "pswd")

cursor = connection.cursor()
cursor.execute("select* from mytable")
results = cursor.fetchall()

cursor.close()
connection.close
