from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
import shoppingservice as ss

logging.basicConfig(level=logging.INFO)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:6523",
    "http://localhost:8080",
    "http://localhost:8001/message",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    quantity_type_id: int
    quantity_value: float

@app.post("/items/")
async def create_item(item: Item):
    try:
        ss.insert_item(item.name, item.quantity_type_id, item.quantity_value)
        return {"message": "Item created successfully"}
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/items/")
async def read_items(bought: bool = False):
    try:
        items = ss.get_items(bought)
        return items
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.put("/items/{item_id}/bought")
async def update_item(item_id: int):
    try:
        ss.mark_item_as_bought(item_id)
        return {"message": "Item marked as bought"}
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get("/")
async def read():
    return {"message": "Hello World"}