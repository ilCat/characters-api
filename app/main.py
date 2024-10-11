from fastapi import FastAPI
from routes import character

app = FastAPI()

app.include_router(character.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
