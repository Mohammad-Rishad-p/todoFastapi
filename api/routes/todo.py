from fastapi import APIRouter, HTTPException, status
from api.models.todo import ToDo
from api.schema.todo import PostToDo, PutToDo, GetToDo

todo_router = APIRouter(prefix = "/api", tags = ["Todo"])


########################## GET REQUEST 1 ###############################
# defining a get endpoint to retrive all tasks in todo list
@todo_router.get("/")
async def all_toDos():
    # to get all todo items from database
    data = ToDo.all()
    # converting the database result into a Pydantic model and returning it
    return await GetToDo.from_queryset(data)

########################## GET REQUEST 2 ###############################
# defining a GET endpoint to retrieve a specific to-do item by its id
@todo_router.get("/{key}")
async def get_todo_item(key: int):
    # Check if the ToDo item with the specified ID exists
    exists = await ToDo.filter(id=key).exists()
    if not exists:
        # If it doesn't exist, raise a 404 error
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TODO not found")
    # Retrieve the to-do item from the database
    todo_item = await ToDo.get(id=key)
    # Return the to-do item in a Pydantic model format
    return await GetToDo.from_tortoise_orm(todo_item)


########################## POST REQUEST ###############################
# defining a Post endpoint to create new todo item
@todo_router.post("/")
async def all_toDos(body: PostToDo):
    # creating a new ToDo item using data from the request body
    row = await ToDo.create(**body.dict(exclude_unset=True))
     # Returning the newly created item in a Pydantic model format
    return await GetToDo.from_tortoise_orm(row)


########################## PUT REQUEST ###############################
# defining a Put endpoint to update a todo item using it's id
@todo_router.put("/{key}")
async def all_toDos(key: int, body: PutToDo):
     # preparing the update data from the request body
    data = body.dict(exclude_unset=True)
    # checking if a ToDo item with the specified ID exists
    exists = await ToDo.filter(id=key).exists()
    if not exists:
        # if it doesn't exist, raise a 404 error
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "TODO not found")
    # updating the ToDo item with the new data
    await ToDo.filter(id=key).update(**data)
    # returning the updated item in a Pydantic model format
    return await GetToDo.from_queryset_single(ToDo.get(id=key))


########################## DELTE REQUEST ###############################
# defining a Delete endpoint to delete a todo item using it's id
@todo_router.delete("/{key}")
async def all_toDos(key: int):
    # checking if a ToDo item with the specified ID exists
    exists = await ToDo.filter(id=key).exists()
    if not exists:
         # if it doesn't exist, raise a 404 error
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TODO not found")
    # deleting the todo item
    await ToDo.filter(id=key).delete()
    return "ToDO deleted successfully"

