from typing import Annotated, Dict, List, Literal, Union
from fastapi import FastAPI
from pydantic import BaseModel, Extra, Field

app = FastAPI()

class BaseColumn(BaseModel):
    sequence: int

class FoodColumn(BaseColumn, extra=Extra.forbid):
    type: Literal["food"]

class RecipeColumn(BaseColumn, extra=Extra.forbid):
    type: Literal["recipe"]

class CustomColumn(BaseColumn, extra=Extra.allow):
    type: Literal["custom"]
    code: str


class FoodMetadata(BaseModel):
    columns: Dict[str, Annotated[FoodColumn | RecipeColumn | CustomColumn, Field(discriminator='type')]]

@app.put("/metadata")
def put_metadata(metadata: FoodMetadata):
    return
