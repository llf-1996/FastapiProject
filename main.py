# -*- coding: utf-8 -*-
"""
@Author: llf
@Email: linfeng@karboncard.com
@Time: 2023/07/28
@desc: 
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from tutorial.main import router_obj as router_tutorial
from accounts.main import router_obj as router_account
from coronavirus.main import router_obj as router_coronavirus
from utils.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title='fastapi title',
    description='fastapi description',
    version='0.0.1',
    docs_url='/docs',
    redoc_url='/redocs',
)
app.mount(path='/static', app=StaticFiles(directory='./static'), name='static')
app.include_router(router_tutorial, tags=['tutorial'])
app.include_router(router_account, prefix='/accounts', tags=['账户'])
app.include_router(router_coronavirus, prefix='/coronavirus', tags=['新冠疫情跟踪器'])


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(
        str(exc.detail), status_code=exc.status_code,
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(
        str(exc), status_code=400,
    )
