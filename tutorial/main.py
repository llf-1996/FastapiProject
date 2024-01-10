# -*- coding: utf-8 -*-
"""
@Author: llf
@Email: 
@Time: 2023/08/19
@desc: 
"""
from typing import Union, Optional

from fastapi import HTTPException, status, Request
from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router_obj = APIRouter()
templates = Jinja2Templates(directory="templates")


@router_obj.get('/index')
def index(request: Request):
    return templates.TemplateResponse(
        "tutorial/index.html",
        {
            'request': request,
            "name": "lisi",
            'age': 18,
        },
    )


@router_obj.get("/demo")
def demo():
    return {'message': 'hello world'}


@router_obj.get('/demo/{param}')
def demo(param: str):
    return {'message': f'hello {param}'}


@router_obj.get("/")
def hello_world():
    return {"Hello": "World"}


@router_obj.get('/http_exceptions/{id}')
async def result(id: int):
    if id == 1:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='error',
        )
    return {'id': id}


class CityInfo(BaseModel):
    province: str
    country: str
    is_affected: Optional[bool] = None


@router_obj.get('/city/{city}')
def result(city: str, query_string: Optional[str] = None):
    return {'city': city, 'query_string': query_string}


@router_obj.put('/city/{city}')
def result(city: str, city_info: CityInfo):
    return {'city': city, 'country': city_info.country, 'is_affected': city_info.is_affected}


@router_obj.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
