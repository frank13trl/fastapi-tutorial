from fastapi import FastAPI, Query
from pydantic import BaseModel, AfterValidator
from typing import Annotated
from enum import Enum

class ModelName(Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    desc: str | None = None
    price: float
    tax: float | None = None

def custom_validator(q: str):
    if q[0] == 'a':
        return q


app = FastAPI()

@app.get('/')
async def root():
    return {"message" : "Hello World"}

# db_items = [{'name':'foo'}, {'name':'bar'}, {'name':'baz'}]

# @app.get('/items/')
# async def read_items(skip: int = 0, limit: int = 10):
#     return db_items[skip : skip + limit]

@app.get("/users/{user_id}/items/{item_id}")
async def read_item(item_id: str, user_id: str, needy: str, q: Annotated[list[str] | None, AfterValidator(custom_validator), Query(max_length=50)] = None, short: bool = False):
    item = {"item_id": item_id, "user_id": user_id, "needy": needy}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get('/files{file_path:path}')
async def read_file(file_path: str):
    return {"file_path" : file_path}

@app.post('/items/{item_id}')
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result