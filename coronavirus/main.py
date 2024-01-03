# -*- coding: utf-8 -*-
"""
@Author: llf
@Email:
@Time: 2023/09/12
@desc: 
"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from coronavirus import crud, schemas
from utils.database import get_db

router_obj = APIRouter()
templates = Jinja2Templates(directory='./coronavirus/templates')


@router_obj.post('/create_city', response_model=schemas.ReadCity)
def create_city(city: schemas.CreateCity, db: Session = Depends(get_db)):
    db_city = crud.get_city_by_name(db=db, name=city.province)
    if db_city:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='city already in')
    return crud.create_city(db=db, city=city)


@router_obj.get('/get_city/{city}', response_model=schemas.ReadCity)
def get_city(city: str, db: Session = Depends(get_db)):
    db_city = crud.get_city_by_name(db=db, name=city)
    if db_city is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='City not found')
    return db_city


@router_obj.get('/get_cities', response_model=List[schemas.ReadCity])
def get_cities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cities = crud.get_cities(db=db, skip=skip, limit=limit)
    return cities


@router_obj.post('/create_data', response_model=schemas.ReadData)
def create_data_for_city(city: str, data: schemas.CreateData, db: Session = Depends(get_db)):
    db_city = crud.get_city_by_name(db=db, name=city)
    data = crud.create_city_data(db=db, data=data, city_id=db_city.id)
    return data


@router_obj.get('/get_data', response_model=List[schemas.ReadData])
def get_data(city: str = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_data(db=db, city=city, skip=skip, limit=limit)


@router_obj.get('/')
def coronavirus(request: Request, city: str = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    data = crud.get_data(db=db, city=city, skip=skip, limit=limit)
    return templates.TemplateResponse('home.html', {
        'request': request,
        'data': data,
        'sync_data_url': '/coronavirus/sync_coronavirus_data/jhu',
    })
