#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年8月6日

com.financial.statistics.count.st.StBean -- st_statistics数据表映射类

com.financial.statistics.count.st.StBean is a st_statistics数据表映射类

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class StBean( Base ):
    
    ## 映身的数据库表名
    __tablename__ = "st_statistics"
    
    id = Column( Integer, name="id", primary_key=True, autoincrement=True )
    
    ## 股票代码
    tsCode = Column( String( 6 ), name = "ts_code", nullable = True )
     
    ## 股票名
    name = Column( String( 45 ), name = "name", nullable = True )
    
    ## st时间段
    stDate = Column( String( 17 ), name = "st_date", nullable = True )
     
    ## st开始时的前一天收盘价
    preClose = Column( Float, name = "pre_close", nullable = True )
     
    ## st期间的最低价
    stMinLow = Column( Float, name = "st_min_low", nullable = True )
     
    ## st期间最大跌幅
    stMaxDown = Column( Float, name = "st_max_down", nullable = True )
     
    ## st期间最高价
    stMaxHigh = Column( Float, name = "st_max_high", nullable = True )
     
    ## st期间最大涨幅
    stMaxUp = Column( Float, name = "st_max_up", nullable = True )
     
    ## st之日起，跌到最低点后，用的多长时间
    stDuration = Column( Integer, name = "st_duration", nullable = True )
     
    ## 撤销st时间段
    cancleStDate = Column( String( 17 ), name = "cancle_st_date", nullable = False )
     
    ## st期间最后一天的收盘价
    stLastClose = Column( Float, name = "st_last_close", nullable = False )
     
    ## 撤销st期间的最高价
    cancleStHigh = Column( Float, name = "cancle_st_high", nullable = False )
     
    ## 撤销st期间的最大涨幅
    cancleStMaxUp = Column( Float, name = "cancle_st_max_up", nullable = False )
     
    ## 撤销st期间的最高价
    cancleStLow = Column( Float, name = "cancle_st_low", nullable = False )
     
    ## 撤销st期间的最大跌幅
    cancleStMaxDown = Column( Float, name = "cancle_st_max_down", nullable = False )
     
    ## 从st之日起，到摘掉st之前的最低价,是否为该股历史的最低价
    isHisLow = Column( String( 2 ), name = "is_his_low", nullable = True )
    
    ## 类型：0-纯st 1带*st
    stType = Column( Integer, name = "st_type", nullable = True )
    
    ## st期间涨幅
    stUp = Column( Float, name = "st_up", nullable = True )
     
    ## st期间的天数
    stDays = Column( Integer, name = "st_days", nullable = True )
    
    ## st期间的深指最大跌幅
    szMaxDown = Column( Float, name = "sz_max_down", nullable = False )
     
    ## st期间的沪指最大跌幅
    shMaxDown = Column( Float, name = "sh_max_down", nullable = False )
     
    ## st期间的深指最大涨幅
    szMaxUp = Column( Float, name = "sz_max_up", nullable = False )
     
    ## st期间的沪指最大涨幅
    shMaxUp = Column( Float, name = "sh_max_up", nullable = False )
     
    ## st期间的深指涨幅
    szUp = Column( Float, name = "sz_up", nullable = False )
    
    ## st期间的沪指涨幅
    shUp = Column( Float, name = "sh_up", nullable = False )