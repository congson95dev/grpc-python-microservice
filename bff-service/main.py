import uvicorn
from fastapi import FastAPI

from service import UserService

app = FastAPI()


@app.get("/users")
async def get_users():
    response = UserService.get_users()
    return response


@app.get("/user")
async def get_user():
    response = UserService.get_user()
    return response

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
