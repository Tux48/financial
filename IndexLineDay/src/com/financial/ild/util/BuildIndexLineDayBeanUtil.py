#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.ild.util.BuildIndexLineDayBeanUtil -- 构建要保存到数据库的指数日线行情bean的工具类

com.financial.ild.util.BuildIndexLineDayBeanUtil is a 
一个单例类，根据不同的条件构建相应要保存到数据库的指数日线行情bean

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
import threading
from math import isnan

from com.financial.ild.bean.IndexLineDaySSEBean import IndexLineDaySSEBean
from com.financial.ild.bean.IndexLineDaySZSEBean import IndexLineDaySZSEBean 

class BuildIndexLineDayBeanUtil:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( BuildIndexLineDayBeanUtil, "_instance" ):
            with BuildIndexLineDayBeanUtil.__instance_lock:
                if not hasattr( BuildIndexLineDayBeanUtil, "_instance" ):
                    BuildIndexLineDayBeanUtil._instance = object.__new__( cls )
                    
        return BuildIndexLineDayBeanUtil._instance
    
    def __init__( self  ):
        pass
    
    
    '''
    @summary: 根据不同的股票代码前缀构建并返回相应的保存到数据库bean的集合。
    
    @param stockCodePrefix: 股票代码前缀
    @param dataFormat: 格式化后的K线数据
    
    @return: 保存到数据库bean的集合
    '''
    def buildIndexLineDaySSEBean( self, dataFormat ):
       
        IndexLineDayDatas = []
        for index, row in dataFormat.iterrows():
            IndexLineDayBean = IndexLineDaySSEBean()
            self.__addAttributeValue( IndexLineDayBean, row )
            IndexLineDayDatas.insert( index, IndexLineDayBean )
            
        return IndexLineDayDatas
    
    
    '''
    @summary: 根据不同的股票代码前缀构建并返回相应的保存到数据库bean的集合。
    
    @param stockCodePrefix: 股票代码前缀
    @param dataFormat: 格式化后的K线数据
    
    @return: 保存到数据库bean的集合
    '''
    def buildIndexLineDaySZSEBean( self, dataFormat ):
       
        IndexLineDayDatas = []
        for index, row in dataFormat.iterrows():
            IndexLineDayBean = IndexLineDaySZSEBean()
            self.__addAttributeValue( IndexLineDayBean, row )
            IndexLineDayDatas.insert( index, IndexLineDayBean )
            
        return IndexLineDayDatas
        
        
    def __addAttributeValue(self, bean, row):
        bean.tsCode = row[ "ts_code" ]
        bean.tsDate = row[ "trade_date" ]
        
        if row[ "close" ] == None or isnan( row[ "close" ] ):
            bean.close = 0.0
        else:
            bean.close = row[ "close" ]
            
        if row[ "open" ] == None or isnan(  row[ "open" ] ):
            bean.open = 0.0
        else:
            bean.open = row[ "open" ]
            
        if row[ "high" ] == None or isnan( row[ "high" ] ):
            bean.high = 0.0
        else:
            bean.high = row[ "high" ]
            
        if row[ "low" ] == None or isnan( row[ "low" ] ):
            bean.low = 0.0
        else:
            bean.low = row[ "low" ]
            
        if row[ "pre_close" ] == None or isnan( row[ "pre_close" ] ):
            bean.preClose  =0.0
        else:
            bean.preClose = row[ "pre_close" ]
            
        if row[ "change" ] == None or isnan( row[ "change" ] ):
            bean.change = 0.0
        else:
            bean.change = row[ "change" ]
            
        if row[ "pct_chg" ] == None or isnan( row[ "pct_chg" ] ):
            bean.pctChg = 0.0
        else:
            bean.pctChg = row[ "pct_chg" ]
            
        if row[ "vol" ] == None or isnan( row[ "vol" ] ):
            bean.vol  =0.0
        else:
            bean.vol = row[ "vol" ]
        
        if row[ "amount" ] == None or isnan( row[ "amount" ] ):
            bean.amount = 0.0
        else:
            bean.amount = row[ "amount" ]