#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-4

com.financial.midt.bean.MarketIndexDayTargetBean -- 数据bean

com.financial.midt.bean.MarketIndexDayTargetBean is a 
数据bean，对数据库中mark_index_day_target表的映射

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class MarketIndexDayTargetBean( Base ):
    
    ## 映身的数据库表名
    __tablename__ = "market_index_day_target"
    
    id = Column( Integer, name="id", primary_key=True, autoincrement=True )
    
    ## 股票TS代码
    tsCode = Column( String( 9 ), name = "ts_code", nullable = True )
    
    ## 交易日期
    tsDate = Column( String( 8 ), name = "trade_date", nullable = True )
    
    ## 当日总市值（元）
    totalMv = Column( Float, name = "total_mv", nullable = True )
    
    ## 当日流通市值（元）
    floatMv = Column( Float, name = "float_mv", nullable = True )
    
    ## 当日总股本（股）
    totalShare = Column( Float, name = "total_share", nullable = True )
    
    ## 当日流通股本（股）
    floatShare = Column( Float, name = "float_share", nullable = True )
    
    ## 当日自由流通股本（股）
    freeShare = Column( Float, name = "free_share", nullable = True )
    
    ## 换手率（%）
    turnoverRate = Column( Float, name = "turnover_rate", nullable = True )
    
    ## 换手率（基于自由流通股本）
    turnoverRateF  = Column( Float, name = "turnover_rate_f", nullable = True )
    
    ## 市盈率
    pe = Column( Float, name = "pe", nullable = True )
    
    ## 市盈率（TTM）
    peTtm = Column( Float, name = "pe_ttm", nullable = True )
    
    ## 市净率
    pb = Column( Float, name = "pb", nullable = True )