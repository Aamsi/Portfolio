from fastapi import APIRouter, Response
from models import Project, Category
from typing import List
from schema import PydanticCategory, PydanticProject
from fastapi_sqlalchemy import db

import requests


router = APIRouter(
    prefix='/projects',
    tags=['projects'],
    responses={404: { 'description': 'Not found' }}
)

@router.post('/create', response_model=PydanticProject, status_code=201)
def create_project(project: PydanticProject, response: Response):
    existing_project = db.session.query(Project).filter(Project.url == project.url).first()
    if existing_project:
        response.status_code = 409
        return existing_project

    categories_name = []
    for category in project.categories:
        categories_name.append(category.name)
    categories = db.session.query(Category).filter(Category.name.in_(categories_name)).all()

    new_project = Project(
        title=project.title,
        description=project.description,
        picture=project.picture,
        url=project.url,
        categories=categories,
    )
    db.session.add(new_project)
    db.session.commit()
    return new_project

@router.get('/', response_model=List[PydanticProject], status_code=200)
def get_projects():
    projects = db.session.query(Project).all()
    return projects

@router.get('/github', response_model=List[PydanticProject], status_code=200)
def import_from_github(response: Response):
    github_response = requests.get('https://api.github.com/users/Aamsi/repos')
    github_response.raise_for_status()

    projects = []
    for project in github_response.json():
        existing_project = db.session.query(Project).filter(Project.url == project['html_url']).first()
        if existing_project:
            continue
        new_project = Project(
            title=project['name'],
            description=project['description'],
            url=project['html_url'],
        )
        db.session.add(new_project)
        db.session.commit()
        projects.append(new_project)

    return projects

