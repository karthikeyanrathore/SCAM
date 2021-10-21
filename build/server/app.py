#!/usr/bin/env python3
from fastapi import FastAPI
from server.routes.student import router as StudentRouter 

app = FastAPI()


app.include_router(StudentRouter, tags=["Student"], prefix="/student")


@app.get("/", tags=['ROOT'])
async def read_root():
  return {"message": "Hello World"}



