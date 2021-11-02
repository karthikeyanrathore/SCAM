#!/usr/bin/env python3
from bson.objectid import ObjectId
import motor.motor_asyncio
MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.users
user_collection = database.get_collection("users_collection")

def Helper(user) -> dict:
  return{
    "id": str(user["_id"]),
    "name": user['name'],
    "email": user['email'],
    "gpa": user['gpa'],
    }

async def add_user(user_data: dict) -> dict:
  user = await user_collection.insert_one(user_data)
  new_user = await user_collection.find_one({"_id": user.inserted_id})
  return Helper(new_user)

async def retrieve_users():
  users =[]
  async for user in user_collection.find():
    users.append(Helper(user))
  return users

async def retrieve_user(id: str) -> dict:
  user = await user_collection.find_one({"_id": ObjectId(id)})
  if user:
    return Helper(user)





  


