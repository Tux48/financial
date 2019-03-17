#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.ta.util.BuildMarketIndexDayTargetBeanUtil -- 构建要保存到数据库的大盘指数每日指标bean的工具类

com.financial.kld.util.BuildMarketIndexDayTargetBeanUtil is a 
一个单例类，根据不同的条件构建相应要保存到数据库的大盘指数每日指标bean

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
import threading
from math import isnan

from com.financial.midt.bean.MarketIndexDayTargetBean import MarketIndexDayTargetBean

class BuildMarketIndexDayTargetBeanUtil:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( BuildMarketIndexDayTargetBeanUtil, "_instance" ):
            with BuildMarketIndexDayTargetBeanUtil.__instance_lock:
                if not hasattr( BuildMarketIndexDayTargetBeanUtil, "_instance" ):
                    BuildMarketIndexDayTargetBeanUtil._instance = object.__new__( cls )
                    
        return BuildMarketIndexDayTargetBeanUtil._instance
    
    def __init__( self  ):
        pass
    
    
    '''
    @summary: 根据不同的股票代码前缀构建并返回相应的保存到数据库bean的集合。
    
    @param dataFormat: 格式化后的K线数据
    
    @return: 保存到数据库bean的集合
    '''
    def buildMarketIndexDayTargetBean( self, dataFormat ):
       
        marketIndexDayTargetDatas = []
        for index, row in dataFormat.iterrows():
            marketIndexDayTargetBean = MarketIndexDayTargetBean()
            self.__addAttributeValue( marketIndexDayTargetBean, row )
            marketIndexDayTargetDatas.insert( index, marketIndexDayTargetBean )
            
        return marketIndexDayTargetDatas
        
        
    def __addAttributeValue(self, bean, row):
        bean.tsCode = row[ "ts_code" ]
        bean.tsDate = row[ "trade_date" ]
        
        if row[ "total_mv" ] == None or isnan( row[ "total_mv" ] ):
            bean.totalMv = 0.0
        else:
            bean.totalMv = row[ "total_mv" ]
            
        if row[ "float_mv" ] == None or isnan( row[ "float_mv" ] ):
            bean.floatMv = 0.0
        else:
            bean.floatMv = row[ "float_mv" ]
            
        if row[ "total_share" ] == None or isnan( row[ "total_share" ] ):
            bean.totalShare = 0.0
        else:
            bean.totalShare = row[ "total_share" ]
            
        if row[ "float_share" ] == None or isnan( row[ "float_share" ] ):
            bean.floatShare = 0.0
        else:
            bean.floatShare = row[ "float_share" ]
            
        if row[ "free_share" ] == None or isnan( row[ "free_share" ] ):
            bean.freeShare = 0.0
        else:
            bean.freeShare = row[ "free_share" ]
        
        if row[ "turnover_rate" ] == None or isnan(  row[ "turnover_rate" ] ):
            bean.turnoverRate = 0.0
        else:
            bean.turnoverRate = row[ "turnover_rate" ]
            
        if row[ "turnover_rate_f" ] == None or isnan( row[ "turnover_rate_f" ] ):
            bean.turnoverRateF = 0.0
        else:
            bean.turnoverRateF = row[ "turnover_rate_f" ]
            
        if row[ "pe" ] == None or isnan( row[ "pe" ] ):
            bean.pe  =0.0
        else:
            bean.pe = row[ "pe" ]
            
        if row[ "pe_ttm" ] == None or isnan( row[ "pe_ttm" ] ):
            bean.peTtm = 0.0
        else:
            bean.peTtm = row[ "pe_ttm" ]
            
        if row[ "pb" ] == None or isnan( row[ "pb" ] ):
            bean.pb = 0.0
        else:
            bean.pb = row[ "pb" ]