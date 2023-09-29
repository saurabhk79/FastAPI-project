# import FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create your fastapi instance
app = FastAPI()

# Our basemodel
class User(BaseModel):
    name: str
    age: int
    is_male : bool = None

# Our sample users
userList = {}

# Define your routing

# Get all users
@app.get("/")
async def get_all_users():
    return userList

# adds a user
@app.post("/add_user")
async def add_user(user : User):
    if user.name in userList:
        raise HTTPException(status_code=404, detail="User already exists!")

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    userList[user.name] = user
    return user

# update a user
@app.put("/user/{user_name}")
async def update_user(user_name: str, user: User):
    if user_name not in userList:
        raise HTTPException(status_code=404, detail="User not found")
    
    userList.pop(user_name)
    userList[user.name] = user
    return user

# delete a user
@app.delete("/user/{user_name}")
async def delete_user(user_name: str):
    if user_name not in userList:
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = userList.pop(user_name)
    return {"message": "User deleted", "user": deleted_user}