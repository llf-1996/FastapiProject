# -*- coding: utf-8 -*-
"""
@Author: llf
@Email:
@Time: 2023/09/14
@desc: 
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

SQLALCHEMY_DATABASE_URL = "postgresql://llf:Aa11111111@localhost:15432/aibiancheng"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
