from typing import Annotated, List, Literal, Union
from fastapi import FastAPI
from pydantic import BaseModel, Extra, Field

app = FastAPI()

class BaseColumn(BaseModel):
    name: str
    type: str

class FoodColumn(BaseColumn, extra=Extra.forbid):
    type: Literal["food"]

class RecipeColumn(BaseColumn, extra=Extra.forbid):
    type: Literal["recipe"]

class CustomColumn(BaseColumn, extra=Extra.allow):
    type: Literal["custom"]


class FoodMetadata(BaseModel):
    columns: List[Annotated[FoodColumn | RecipeColumn | CustomColumn, Field(discriminator='type')]]

@app.put("/metadata")
def put_metadata(metadata: FoodMetadata):
    return
