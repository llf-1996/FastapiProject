# -*- coding: utf-8 -*-
"""
@Author: llf
@Email: 
@Time: 2023/08/19
@desc: 
"""
import uvicorn


if __name__ == '__main__':
    # uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True, workers=1)
    uvicorn.run('main:app', host='127.0.0.1', port=8000,  reload=True, workers=1, log_config='./settings/log.json')
