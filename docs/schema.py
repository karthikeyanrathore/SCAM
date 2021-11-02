#!/usr/bin/env python3
from typing import Optional
from pydantic import BaseModel, Field

class UserModel(BaseModel):
  name: str = Field(...)
  email: str = Field(...)
  gpa: float = Field(...)

  class Config:
    schema_extra ={
    "example":{
      "name": "karthikeyan",
      "email": "xyz@x.in",
      "gpa": "3.2",
      }
    }


class UpdateUserModel(BaseModel):
  name: Optional[str]
  email: Optional[str]
  gpa: Optional[float]

  class Config:
    schema_extra ={
    "example":{
      "name": "karthikeyan",
      "email": "xyz@x.in",
      "gpa": "2.2",
      }
    }

def ResponseModel(data, message):
  return{
    "data": [data],
    "code": 200,
    "message": message,
  }

def ErrorResponseModel(error, code, message):
  return {
    "error":error,
    "code": code,
    "message": message
    }



