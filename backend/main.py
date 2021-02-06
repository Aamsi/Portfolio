from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi.middleware.cors import CORSMiddleware

from models import Category, Project
from schema import PydanticProject, PydanticCategory
from dotenv import load_dotenv
from routers import projects, categories

import uvicorn
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:8080"])
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

app.include_router(projects.router)
app.include_router(categories.router)

@app.get('/')
async def get_test():
    return ({ "message": "Hello World" })

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3080, reload=True)
