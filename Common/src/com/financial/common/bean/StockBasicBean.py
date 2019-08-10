#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-4

com.financial.stockbasic.bean.StockBaseBean -- 数据bean

com.financial.stockbasic.bean.StockBaseBean is a 
数据bean，对数据库中stock_basic表的映射

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class StockBasicBean( Base ):
    
    ## 映身的数据库表名
    __tablename__ = "stock_basic"
    
    id = Column( Integer, name="id", primary_key=True, autoincrement=True )
    
    ## 股票TS代码
    tsCode = Column( String( 9 ), name = "ts_code", unique = True, nullable = True)
    
    ## 股票代码
    symbol = Column( String( 6 ), name = "symbol", unique = True, nullable = True )
    
    ## 股票名称
    name = Column( String( 45 ), name = "name", nullable = True )
    
    ## 所在地域
    area  = Column( String( 45 ), name = "area" )

    ## 所属行业 
    industry = Column( String( 45 ), name = "industry" )
    
    ## 股票全称
    fullname = Column( String( 45 ), name = "fullname", nullable = True )
    
    ## 英文全称
    enname = Column( String( 45 ), name = "enname", nullable = True )
    
    ## 市场类型 （主板/中小板/创业板）
    market = Column( String( 10 ), name = "market", nullable = True )
    
    ## 交易所代码
    exchange = Column( String( 45 ), name = "exchange", nullable = True )
    
    ## 交易货币
    currType = Column( String( 45), name = "curr_type", nullable = True )
    
    ## 上市状态： L上市 D退市 P暂停上市
    listStatus = Column( String( 10 ), name = "list_status", nullable = True )
    
    ## 上市日期
    listDate = Column( String( 8 ), name = "list_date", nullable = True )
    
    ## 退市日期
    deListDate = Column( String( 8 ), name = "delist_date" )
    
    ## 是否沪深港通标的，N否 H沪股通 S深股通
    isHZ = Column( String( 5), name = "is_hs", nullable = True )