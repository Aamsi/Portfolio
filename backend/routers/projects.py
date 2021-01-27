from fastapi import APIRouter, Response
from models import Project, Category
from schema import PydanticCategory, PydanticProject
from sqlalchemy.orm import Session
from fastapi_sqlalchemy import db

router = APIRouter(
    prefix='/projects',
    tags=['projects'],
    responses={404: { 'description': 'Not found' }}
)

@router.post('/create', response_model=PydanticProject, status_code=201)
async def create_project(project: PydanticProject, response: Response):
    existing_project = db.session.query(Project).filter(Project.url == project.url).first()
    if existing_project:
        response.status_code = 409
        return existing_project

    categories = db.session.query(Category).filter(Category.name.in_(project.categories)).all()
    new_project = Project(
        title=project.title,
        description=project.description,
        picture=project.picture,
        url=project.url,
        category=categories,
    )
    db.session.add(new_project)
    db.session.commit()
    return new_project