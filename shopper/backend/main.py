from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

origins = [
    "http://frontend:8080",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read():
    return {"message": "Hello World"}