from fastapi import APIRouter, Response
from models import Project, Category
from schema import PydanticCategory, PydanticProject
from fastapi_sqlalchemy import db

router = APIRouter(
    prefix='/categories',
    tags=['categories'],
    responses={404: { 'description': 'Not found' }}
)

@router.get('/', status_code=200)
def get_all_categories():
    categories = db.session.query(Category).all()
    return categories

@router.post('/create', response_model=PydanticCategory, status_code=201)
def create_category(category: PydanticCategory, response: Response):
    existing_category = db.session.query(Category).filter(Category.name == category.name).first()
    if existing_category:
        response.status_code = 409
        return existing_category

    new_category = Category(
        name=category.name,
    )
    db.session.add(new_category)
    db.session.commit()
    return new_category
