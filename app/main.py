from fastapi import FastAPI
from app.routes import character

app = FastAPI()

app.include_router(character.router)


@app.get("/")
async def root():
    return {"message": "Welcome, please go to the Swagger UI"}
