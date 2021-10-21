#!/usr/bin/env python3
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class StudentSchema(BaseModel):
  name: str = Field(...)
  email: EmailStr = Field(...)
  course: str = Field(...)
  year: int = Field(..., gt=0, le=9)
  gpa: float = Field(..., le=4)

  class Config:
    schema_extra = {
        "example":{
          "name": "karthikeyan", 
          "email": "xyz@edu.in",
          "course": "Computer Science",
          "year": 3,
          "gpa": "2.3",
          }
     }

class UpdateStudentModel(BaseModel):
  name: Optional[str]
  email: Optional[EmailStr]
  course: Optional[str]
  year: Optional[int]
  gpa: Optional[float]

  class Config:
    schema_extra = {
        "example":{
          "name": "karthikeyan", 
          "email": "xyz@edu.in",
          "course": "Computer Science",
          "year": 3,
          "gpa": "2.1",
          }
     }

def ResponseModel(data, message):
  return {
      "data": [data],
      "code": 200,
      "message": message,
      }

def ErrorResponseModel(error, code, message):
  return { "error": error, "code": code, "message": message}








