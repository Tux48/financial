#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-4

com.financial.saod.bean.StockAccountOpenDataBean -- 数据bean

com.financial.saod.bean.StockAccountOpenDataBean is a 
数据bean，对数据库中stock_account_open_data表的映射

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class StockAccountOpenDataBean( Base ):
    
    ## 映身的数据库表名
    __tablename__ = "stock_account_open_data"
    
    id = Column( Integer, name="id", primary_key=True, autoincrement=True )
    
    ## 统计周期
    date = Column( String( 8 ), name = "date" )
    
    ## 本周新增（万）
    weeklyNew = Column( Float, name = "weekly_new" )
    
    ## 期末总账户数（万）
    total = Column( Float, name = "total" )
    
    ## 本周持仓账户数（万）
    weeklyHold  = Column( Float, name = "weekly_hold", nullable = True )

    ## 本周参与交易账户数（万）
    weeklyTrade = Column( Float, name = "weekly_trade", nullable = True )