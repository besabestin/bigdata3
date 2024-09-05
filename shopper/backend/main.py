from fastapi import FastAPI, HTTPException

import logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/")
async def read():
    return {"message": "Hello World"}