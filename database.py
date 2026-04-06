from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

pwd = os.getenv("pwd_db")

DB_URL = f"mssql+pyodbc://sa:{pwd}@localhost/USER_DB?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    Id = Column(Integer, primary_key=True)
    Ten = Column(String)
    DiaChi = Column(String)
    Email = Column(String)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()