from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



URL = "sqlite:///./App/todos.db"
engine = create_engine(URL, connect_args={"check_same_thread": False})

#URL = "postgresql+psycopg2://postgres:password@localhost:5432/my_database"
#engine = create_engine(URL)

Base = declarative_base()
SessionLocal = sessionmaker(autoflush=False, autocommit= False, bind=engine)