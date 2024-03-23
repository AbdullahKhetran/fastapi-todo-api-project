import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase

load_dotenv()

DATABASE_CONNECTION_URL = os.getenv('DATABASE_CONNECTION_URL')

if type(DATABASE_CONNECTION_URL) == str:
    engine = create_engine(DATABASE_CONNECTION_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
