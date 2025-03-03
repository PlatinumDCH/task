from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def indec():
    return {'message':'home page'}
