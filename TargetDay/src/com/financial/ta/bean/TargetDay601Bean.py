#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-4

com.financial.ta.bean.TargetDay601Bean -- 数据bean

com.financial.ta.bean.TargetDay601Bean is a 
数据bean，对数据库中target_day_601表的映射

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class TargetDay601Bean( Base ):
    
    ## 映身的数据库表名
    __tablename__ = "target_day_601"
    
    id = Column( Integer, name="id", primary_key=True, autoincrement=True )
    
    ## 股票TS代码
    tsCode = Column( String( 9 ), name = "ts_code", nullable = True )
    
    ## 交易日期
    tsDate = Column( String( 8 ), name = "trade_date", nullable = True )
    
    ## 当日收盘价
    close = Column( Float, name = "close", nullable = True )
    
    ## 换手率（%）
    turnoverRate = Column( Float, name = "turnover_rate", nullable = True )
    
    ## 换手率（自由流通股）
    turnoverRateF  = Column( Float, name = "turnover_rate_f", nullable = True )

    ## 量比
    volumeRatio = Column( Float, name = "volume_ratio", nullable = True )
    
    ## 市盈率（总市值/净利润）
    pe = Column( Float, name = "pe", nullable = True )
    
    ## 市盈率（TTM）
    peTtm = Column( Float, name = "pe_ttm", nullable = True )
    
    ## 市净率（总市值/净资产）
    pb = Column( Float, name = "pb", nullable = True )
    
    ## 市销率
    ps = Column( Float, name = "ps", nullable = True )
    
    ## 市销率（TTM）
    psTtm = Column( Float, name = "ps_ttm" , default = 0.0 )
    
    ## 总股本 （万）
    totalShare = Column( Float, name = "total_share", nullable = True )
    
    ## 流通股本 （万）
    floatShare = Column( Float, name = "float_share", nullable = True )
    
    ## 自由流通股本 （万）
    freeShare = Column( Float, name = "free_share", nullable = True )
    
    ## 总市值 （万元）
    totalMv = Column( Float, name = "total_mv", nullable = True )
    
    ## 流通市值（万元）
    circMv = Column( Float, name = "circ_mv" , default = 0.0 )