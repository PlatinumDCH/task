from fastapi import FastAPI
from src.routers import users
from src.routers import tasks
app = FastAPI()

app.include_router(users.router, prefix="", tags=["auth"])
app.include_router(tasks.router, prefix="", tags=["task"])

@app.get('/')
async def index():
    return {'message':'home page'}
