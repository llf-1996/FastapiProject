# -*- coding: utf-8 -*-
"""
@Author: llf
@Email:
@Time: 2023/09/12
@desc: 
"""
from sqlalchemy.orm import Session

from coronavirus import models, schemas


def get_city(db: Session, city_id: int):
    return db.query(models.City).filter(models.City.id == city_id).first()


def get_city_by_name(db: Session, name: str):
    return db.query(models.City).filter(models.City.province == name).first()


def get_cities(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.City).offset(skip).limit(limit).all()


def create_city(db: Session, city: schemas.CreateCity):
    db_city = models.City(**city.model_dump())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


def get_data(db: Session, city: str = None, skip: int = 0, limit: int = 10):
    if city:
        return db.query(models.Data).filter(models.Data.city.has(province=city))
    return db.query(models.Data).offset(skip).limit(limit).all()


def create_city_data(db: Session, data: schemas.CreateData, city_id: int):
    db_data = models.Data(**data.model_dump(), city_id=city_id)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data
