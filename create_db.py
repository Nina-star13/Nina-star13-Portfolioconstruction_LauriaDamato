import sqlite3
import pandas as pd # to read the csv file and upload it to sqlite

df = pd.read_csv("static/data.csv")
print(df.head()) # display the first 5 strings

with sqlite3.connect("crypto.db") as conn: # connettore
    df.to_sql("crypto", conn, index= False) # index= False to delete the index column