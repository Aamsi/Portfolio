from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, LargeBinary, Table, ForeignKey
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(EmailType)
    password_hash = Column(String(64))


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    picture = Column(String(150), nullable=True)
    url = Column(String(100), nullable=False, unique=True)
    categories = relationship("Category", secondary=lambda: association_table, back_populates='projects')


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    projects = relationship("Project", secondary=lambda: association_table, back_populates='categories')

association_table = Table("projectcategory", Base.metadata,
    Column('project_id', Integer, ForeignKey('project.id')),
    Column('category_id', Integer, ForeignKey('category.id')),
)
