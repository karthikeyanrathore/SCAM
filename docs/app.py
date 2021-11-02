#!/usr/bin/env python3
from fastapi import FastAPI
from route import router as UserRouter

app = FastAPI()

app.include_router(UserRouter, tags=['Student'], prefix="/student")


@app.get("/", tags=["Root"])
async def root():
  return {"message": "Hello World"}
