# -*- coding: utf-8 -*-
"""
@Author: llf
@Email:
@Time: 2023/09/12
@desc: 
"""
from sqlalchemy import Column, String, Integer, BigInteger, Date, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from .database import Base


class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    province = Column(String(100), unique=True, nullable=False, comment='省/直辖市')
    country = Column(String(100), nullable=False, comment='国家')
    country_code = Column(String(100), nullable=False, comment='国家代码')
    country_population = Column(BigInteger, nullable=False, comment='国家人口')
    data = relationship('Data', back_populates='city')

    created_dt = Column(DateTime, server_default=func.now(), comment='创建时间')
    updated_dt = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')

    def __repr__(self):
        return f'{self.country}_{self.province}'
