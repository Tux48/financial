#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-4

com.financial.ild.bean.IndexLineDay000Bean -- 数据bean

com.financial.ild.bean.IndexLineDay000Bean is a 
数据bean，对数据库中的index_line_day_000表的映射

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class IndexLineDaySSEBean( Base ):
    
    ## 映身的数据库表名
    __tablename__ = "index_line_day_sse"
    
    id = Column( Integer, name="id", primary_key=True, autoincrement=True )
    
    ## 股票TS代码
    tsCode = Column( String( 9 ), name = "ts_code", nullable = True )
    
    ## 交易日期
    tsDate = Column( String( 8 ), name = "trade_date", nullable = True )
    
    ## 收盘点位
    close = Column( Float, name = "close", nullable = True )
    
    ## 开盘点位
    open = Column( Float, name = "open", nullable = True )
    
    ## 最高点位
    high = Column( Float, name = "high", nullable = True )
    
    ## 最低点位
    low  = Column( Float, name = "low", nullable = True )

    ## 昨日收盘点
    preClose = Column( Float, name = "pre_close", nullable = True )
    
    ## 涨跌点
    change = Column( Float, name = "change", nullable = True )
    
    ## 涨跌幅
    pctChg = Column( Float, name = "pct_chg", nullable = True )
    
    ## 成交量 （手）
    vol = Column( Float, name = "vol", nullable = True )
    
    ## 成交额 （千元）
    amount = Column( Float, name = "amount" , default = 0.0 )