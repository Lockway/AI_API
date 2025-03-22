from fastapi import FastAPI
app = FastAPI()

import pymysql

@app.get("/")
def read_root():
    print("Hello!")
