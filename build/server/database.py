#!/usr/bin/env python3
import motor.motor_asyncio

MONGO_DETAILS= "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students
student_collection = database.get_collection("students_collection")

def student_helper(student) -> dict:
  return {
      "id": str(student["_id"]),
      "name": student["name"],
      "email": student["email"],
      "course": student["course"],
      "year": student["year"],
      "gpa": student["gpa"],
      }


# get all students
async def retrieve_students():
  students = []
  async for student in student_collection.find():
    students.append(student_helper(student))
  return students


# add a new student
async def add_student(student_data: dict) -> dict:
  student = await student_collection.insert_one(student_data)
  new_student = await student_collection.find_one({"_id": student.inserted_id})
  return student_helper(new_student)



