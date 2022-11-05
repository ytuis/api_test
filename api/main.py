from fastapi import FastAPI

from api.routers import item

app = FastAPI()

app.include_router(item.router)


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
