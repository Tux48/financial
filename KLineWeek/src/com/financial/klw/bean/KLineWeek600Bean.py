#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-4

com.financial.klw.bean.KLineWeek600Bean -- 数据bean

com.financial.klw.bean.KLineWeek600Bean is a 
数据bean，对数据库中k_line_week_600表的映射

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class KLineWeek600Bean( Base ):
    
    ## 映身的数据库表名
    __tablename__ = "k_line_week_600"
    
    id = Column( Integer, name="id", primary_key=True, autoincrement=True )
    
    ## 股票TS代码
    tsCode = Column( String( 9 ), name = "ts_code", nullable = True )
    
    ## 交易日期
    tsDate = Column( String( 8 ), name = "trade_date", nullable = True )
    
    ## 开盘价
    open = Column( Float, name = "open", nullable = True )
    
    ## 最高价
    high = Column( Float, name = "high", nullable = True )
    
    ## 最低价
    low  = Column( Float, name = "low", nullable = True )

    ## 所属行业 
    close = Column( Float, name = "close", nullable = True )
    
    ## 昨收价
    preClose = Column( Float, name = "pre_close", nullable = True )
    
    ## 涨跌额
    change = Column( Float, name = "change", nullable = True )
    
    ## 涨跌幅
    pctChg = Column( Float, name = "pct_chg", nullable = True )
    
    ## 成交量 （手）
    vol = Column( Float, name = "vol", nullable = True )
    
    ## 成交额 （千元）
    amount = Column( Float, name = "amount", nullable = True )