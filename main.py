from typing import Union
from fastapi import FastAPI     #import fastApi
from pydantic import BaseModel

app=FastAPI()  #create fastAPI instance  #main point to create the API                 #FastAPI is a Python class that provides all the functionality for your API

class Item(BaseModel):
    name:str
    price:float
    is_offer:Union[bool,None]=None

@app.get("/") #@app.get("/items/{item_id}")      #define a path operation decorator      #handling request that go to the path/usign a get operation
async def read_root():  #async def read_item(item_id):     #define the operation function/ the function that goes below the path operation decorator #this will be called by FastAPI whenever it receives a request to the specified URL(/)
    return {"Hello":"World"}    #return content

@app.get("/{item_id}")
async def read_item(item_id:int, q:Union[str, None]=None):
    return{"item_id":item_id,"q":q}

@app.put("item/{item_id}")
def update_item(item_id:int, item:Item):
    return{"item_name":item.name,"item_id":item_id}


