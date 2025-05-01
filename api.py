#create a server to use to get data
from fastapi import FastAPI
import pandas as pd
import sqlite3
import httpx
from datetime import datetime
# run fastapi dev api.py in the terminal 

app = FastAPI() #url able us to map a resource

@app.get("/hello") #path: what we are mapping
def hello():
    return "Hello, world!"

@app.get("/health")
def health():
    return {"Server is working"}

@app.get("/data")
def data():
    with sqlite3.connect("crypto.db") as conn:
        df= pd.read_sql("SELECT * FROM crypto;", conn) # * used to select all
    return df.to_dict(orient="records")

@app.get("/crypto/{name}")
def crypto(name: str):
    with sqlite3.connect("crypto.db") as conn:
        df = pd.read_sql(f"SELECT Datetime, {name} FROM crypto;", conn) #to take specific column
    return df.to_dict(orient="records")

@app.get("/update")
def update():
    response = httpx.get(
      'https://api.binance.com/api/v3/ticker/price?symbols=["ETHUSDT","DOGEUSDT","BTCUSDT"]', verify=False
    )
    data = response.json()
    print(data)

    row = {coin["symbol"]: coin["price"] for coin in data}
    with sqlite3.connect("crypto.db") as conn:
        conn.execute(
            "INSERT INTO crypto (Datetime, Bitcoin, Dogecoin, Ethereum)"
            " VALUES (:datetime, :bitcoin, :dogecoin, :ethereum);",
            {
                "bitcoin": row["BTCUSDT"],
                "dogecoin": row["DOGEUSDT"],
                "ethereum":row["ETHUSDT"],
                "datetime": datetime.now(),
            },
        )
    return "Success"