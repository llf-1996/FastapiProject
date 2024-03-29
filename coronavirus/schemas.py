# -*- coding: utf-8 -*-
"""
@Author: llf
@Email:
@Time: 2023/09/12
@desc: 
"""
from datetime import datetime
from datetime import date as date_
from pydantic import BaseModel


class CreateData(BaseModel):
    date: date_
    confirmed: int = 0
    deaths: int = 0
    recovered: int = 0


class CreateCity(BaseModel):
    province: str
    country: str
    country_code: str
    country_population: int


class ReadData(CreateData):
    id: int
    city_id: int
    created_dt: datetime
    updated_dt: datetime

    class Config:
        orm_mode = True


class ReadCity(CreateCity):
    id: int
    created_dt: datetime
    updated_dt: datetime

    class Config:
        orm_mode = True
