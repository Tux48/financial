#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-4

com.financial.suspend.bean.SuspendBean -- 数据bean

com.financial.suspend.bean.SuspendBean is a 
数据bean，对数据库中suspend表的映射

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class SuspendBean( Base ):
    
    ## 映身的数据库表名
    __tablename__ = "suspend"
    
    id = Column( Integer, name="id", primary_key=True, autoincrement=True )
    
    ## 股票TS代码
    tsCode = Column( String( 9 ), name = "ts_code" )
    
    ## 停牌日期
    suspendDate = Column( String( 8 ), name = "suspend_date" )
    
    ## 复牌日期
    resumeDate = Column( String( 8 ), name = "resume_date" )
    
    ## 停牌原因
    suspendReason = Column( String( 255 ), name = "suspend_reason" )