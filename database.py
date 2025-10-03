"""Database Configuartion"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# create session -> is a SQLAlchemy object that manges the conversation with database

# create a database url -> so SQLAlchemy know what type of database you are using
SQLALCHEMY_DATABASE_URL = "sqlite:///./fantasy_data.db"

# setting = allow multiple connection to the database without throwing an error
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# add more configuartion setting with session object
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class = standard SQLAlchemy template for models.py
Base = declarative_base()


def hello():
    print("hello world")
