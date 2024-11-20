from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


user = 'angelo_souza'
password = '1234'
host = 'localhost'
database = 'blog'

DATABASE_URI = f'postgresql://{user}:{password}@{host}/{database}'


engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
