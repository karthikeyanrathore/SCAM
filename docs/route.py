#!/usr/bin/env python3
from schema import UserModel, UpdateUserModel, ResponseModel, ErrorResponseModel
from db import add_user, retrieve_users, retrieve_user
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body

router = APIRouter()
@router.post("/", response_description="User data added")
async def add_user_data(user: UserModel = Body(...)):
  user = jsonable_encoder(user)
  new_user = await add_user(user)
  return ResponseModel(new_user, "success: added")

@router.get("/")
async def get_users():
  users = await retrieve_users()
  if users:
    return ResponseModel(users, "sucess")
  return ResponseModel(users, "empty")


@router.get("/{id}", response_description="User data retrieved")
async def get_user(id):
  user = await retrieve_user(id)
  if user:
    return ResponseModel(user, "sucess")
  return ResponseModel(user, "empty")





