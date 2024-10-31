from fastapi import FastAPI
from api.routes.todo import todo_router
from tortoise.contrib.fastapi import register_tortoise

# creating an instance of the FastAPI application
app = FastAPI()

# including the to-do router to register the routes
app.include_router(todo_router)

# registering Tortoise ORM with FastAPI
register_tortoise(
    app=app,  # The FastAPI app instance
    db_url="sqlite://todo.db",  # URL for the SQLite database
    add_exception_handlers=True,  # Enables automatic exception handling
    generate_schemas=True,  # Automatically creates database schemas based on the models
    modules={"models": ["api.models.todo"]}  # Specifying the models to use
)

# a simple get request for health check
@app.get("/")
async def index():
    return {"status todo-api is running"}