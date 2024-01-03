# -*- coding: utf-8 -*-
"""
@Author: llf
@Email:
@Time: 2023/09/12
@desc: 
"""
from datetime import datetime
from pydantic import BaseModel


class CreateCity(BaseModel):
    province: str
    country: str
    country_code: str
    country_population: int


class ReadCity(CreateCity):
    id: int
    created_dt: datetime
    updated_dt: datetime

    class Config:
        orm_mode = True
