from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator
from typing import Optional
from api.models.todo import ToDo

# Automatically generates a Pydantic model for the ToDo model to be used in GET requests
GetToDo = pydantic_model_creator(ToDo, name= "Todo")

# Defining a Pydantic model for POST requests to create new to-do items
class PostToDo(BaseModel):
    title: str = Field(..., max_length=100)
    description: str = Field(..., max_length=100)
    done: bool
  
# Defining a Pydantic model for PUT requests to update existing to-do items   
class PutToDo(BaseModel):
    title: Optional[str] = Field(..., max_length=100)
    description: Optional[str] = Field(..., max_length=100)
    done: Optional[bool]