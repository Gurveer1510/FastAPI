from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from .config import settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Gurveer15010@@localhost/FastAPI'
url = URL.create('postgresql', username=settings.database_username, password=settings.database_password, host=settings.database_hostname,port=settings.database_port, database=settings.database_name)

engine = create_engine(url)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
