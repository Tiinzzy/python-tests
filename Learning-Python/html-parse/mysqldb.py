import mysql.connector
import pandas as pd

my_conn = mysql.connector.connect(
    host="127.0.0.1", database='tests', user="dbadmin", passwd="washywashy")




query = "Select * from tests.wiki_articles_relations;"
df = pd.read_sql(query, my_conn)



for index, row in df.iterrows():
    print(index, ' , ', row['from_title'], ' , ', row['to_title'])


print(df.values)