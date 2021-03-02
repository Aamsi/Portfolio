import hashlib

from fastapi import APIRouter, Response, Form
from fastapi_sqlalchemy import db

from models import User


router = APIRouter(
    prefix='/admin',
    tags=['admin'],
    responses={404: { 'description': 'Not found' }},
)

@router.post('/login', status_code=200)
def login(response: Response, email: str = Form(...), password: str = Form(...)):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user = db.session.query(User).filter(User.email == email).first()

    if not user or user.password_hash != hashed_password:
        response.status_code == 401
        return "Mauvais identifiants"

    return user
