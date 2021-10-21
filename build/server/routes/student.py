#!/usr/bin/env python3
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder


from server.database import(
    retrieve_students,
    add_student,
    )
from server.models.student import(
    StudentSchema,
    UpdateStudentModel,
    ResponseModel,
    ErrorResponseModel,
    )

router = APIRouter()

# get new Student
@router.get("/", response_description="Students retrieved")
async def get_students():
  students = await retrieve_students()
  if students:
    return ResponseModel(students, "Students data retrieved successfully")
  return ResponseModel(students, "Empty list returned")


# add new Stduent
@router.post("/", response_description="Students data added into the database")
async def get_students(student: StudentSchema = Body(...)):
  student = jsonable_encoder(student)
  new_student = await add_student(student)
  return ResponseModel(new_student,"Student Added successfully") 






