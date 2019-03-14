#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.ta.util.BuildTargetDayBeanUtil -- 构建要保存到数据库的每日指标bean的工具类

com.financial.kld.util.BuildTargetDayBeanUtil is a 
一个单例类，根据不同的条件构建相应要保存到数据库的每日指标bean

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
import threading
from math import isnan

from com.financial.ta.bean.TargetDay000Bean import TargetDay000Bean
from com.financial.ta.bean.TargetDay001Bean import TargetDay001Bean 
from com.financial.ta.bean.TargetDay002Bean import TargetDay002Bean
from com.financial.ta.bean.TargetDay300Bean import TargetDay300Bean
from com.financial.ta.bean.TargetDay600Bean import TargetDay600Bean
from com.financial.ta.bean.TargetDay601Bean import TargetDay601Bean
from com.financial.ta.bean.TargetDay603Bean import TargetDay603Bean

class BuildTargetDayBeanUtil:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( BuildTargetDayBeanUtil, "_instance" ):
            with BuildTargetDayBeanUtil.__instance_lock:
                if not hasattr( BuildTargetDayBeanUtil, "_instance" ):
                    BuildTargetDayBeanUtil._instance = object.__new__( cls )
                    
        return BuildTargetDayBeanUtil._instance
    
    def __init__( self  ):
        pass
    
    
    '''
    @summary: 根据不同的股票代码前缀构建并返回相应的保存到数据库bean的集合。
    
    @param stockCodePrefix: 股票代码前缀
    @param dataFormat: 格式化后的K线数据
    
    @return: 保存到数据库bean的集合
    '''
    def buildTargetDayBean( self, stockCodePrefix, dataFormat ):
       
        if stockCodePrefix == "000":
            return self.__buildTargetDay000( dataFormat )
        elif stockCodePrefix == "001":
            return self.__buildTargetDay001( dataFormat )
        elif stockCodePrefix == "002":
            return self.__buildTargetDay002( dataFormat )
        elif stockCodePrefix == "300":
            return self.__buildTargetDay300( dataFormat )
        elif stockCodePrefix == "600":
            return self.__buildTargetDay600( dataFormat )
        elif stockCodePrefix == "601":
            return self.__buildTargetDay601( dataFormat )
        elif stockCodePrefix == "603":
            return self.__buildTargetDay603( dataFormat )
        else:
            return []
        
        
    def __buildTargetDay000( self, dataFormat ):
        targetDayDatas = []
        for index, row in dataFormat.iterrows():
            targetDayBean = TargetDay000Bean()
            self.__addAttributeValue( targetDayBean, row )
            targetDayDatas.insert( index, targetDayBean )
            
        return targetDayDatas
        
    def __buildTargetDay001( self, dataFormat ):
        targetDayDatas = []
        for index, row in dataFormat.iterrows():
            targetDayBean = TargetDay001Bean()
            self.__addAttributeValue( targetDayBean, row )
            targetDayDatas.insert( index, targetDayBean )
            
        return targetDayDatas
        
    def __buildTargetDay002( self, dataFormat ):
        targetDayDatas = []
        for index, row in dataFormat.iterrows():
            targetDayBean = TargetDay002Bean()
            self.__addAttributeValue( targetDayBean, row )
            targetDayDatas.insert( index, targetDayBean )
            
        return targetDayDatas
        
    def __buildTargetDay300( self, dataFormat ):
        targetDayDatas = []
        for index, row in dataFormat.iterrows():
            targetDayBean = TargetDay300Bean()
            self.__addAttributeValue( targetDayBean, row )
            targetDayDatas.insert( index, targetDayBean )
            
        return targetDayDatas
        
    def __buildTargetDay600( self, dataFormat ):
        targetDayDatas = []
        for index, row in dataFormat.iterrows():
            targetDayBean = TargetDay600Bean()
            self.__addAttributeValue( targetDayBean, row )
            targetDayDatas.insert( index, targetDayBean )
            
        return targetDayDatas
        
    def __buildTargetDay601( self, dataFormat ):
        targetDayDatas = []
        for index, row in dataFormat.iterrows():
            targetDayBean = TargetDay601Bean()
            self.__addAttributeValue( targetDayBean, row )
            targetDayDatas.insert( index, targetDayBean )
            
        return targetDayDatas
        
    def __buildTargetDay603( self, dataFormat ):
        targetDayDatas = []
        for index, row in dataFormat.iterrows():
            targetDayBean = TargetDay603Bean()
            self.__addAttributeValue( targetDayBean, row )
            targetDayDatas.insert( index, targetDayBean )
            
        return targetDayDatas
    
    def __addAttributeValue(self, bean, row):
        bean.tsCode = row[ "ts_code" ]
        bean.tsDate = row[ "trade_date" ]
        
        if row[ "close" ] == None or isnan( row[ "close" ] ):
            bean.close = 0.0
        else:
            bean.close = row[ "close" ]
        
        if row[ "turnover_rate" ] == None or isnan(  row[ "turnover_rate" ] ):
            bean.turnoverRate = 0.0
        else:
            bean.turnoverRate = row[ "turnover_rate" ]
            
        if row[ "turnover_rate_f" ] == None or isnan( row[ "turnover_rate_f" ] ):
            bean.turnoverRateF = 0.0
        else:
            bean.turnoverRateF = row[ "turnover_rate_f" ]
            
        if row[ "volume_ratio" ] == None or isnan( row[ "volume_ratio" ] ):
            bean.volumeRatio = 0.0
        else:
            bean.volumeRatio = row[ "volume_ratio" ]
            
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
            
        if row[ "ps" ] == None or isnan( row[ "ps" ] ):
            bean.ps  =0.0
        else:
            bean.ps = row[ "ps" ]
        
        if row[ "ps_ttm" ] == None or isnan( row[ "ps_ttm" ] ):
            bean.psTtm = 0.0
        else:
            bean.psTtm = row[ "ps_ttm" ]
            
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
            
        if row[ "total_mv" ] == None or isnan( row[ "total_mv" ] ):
            bean.totalMv = 0.0
        else:
            bean.totalMv = row[ "total_mv" ]
            
        if row[ "circ_mv" ] == None or isnan( row[ "circ_mv" ] ):
            bean.circMv = 0.0
        else:
            bean.circMv = row[ "circ_mv" ]