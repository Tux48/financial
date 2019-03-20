#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.saod.util.BuildStockAccountOpenDataBeanUtil -- 构建要保存到数据库的股票账户开户数据bean的工具类

com.financial.saod.util.BuildStockAccountOpenDataBeanUtil is a 
一个单例类，根据不同的条件构建相应要保存到数据库的股票账户开户数据bean

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
import threading
from math import isnan

from com.financial.saod.bean.StockAccountOpenDataBean import StockAccountOpenDataBean

class BuildStockAccountOpenDataBeanUtil:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( BuildStockAccountOpenDataBeanUtil, "_instance" ):
            with BuildStockAccountOpenDataBeanUtil.__instance_lock:
                if not hasattr( BuildStockAccountOpenDataBeanUtil, "_instance" ):
                    BuildStockAccountOpenDataBeanUtil._instance = object.__new__( cls )
                    
        return BuildStockAccountOpenDataBeanUtil._instance
    
    def __init__( self  ):
        pass
    
    
    '''
    @summary: 根据不同的股票代码前缀构建并返回相应的保存到数据库bean的集合。
    
    @param stockCodePrefix: 股票代码前缀
    @param dataFormat: 格式化后的K线数据
    
    @return: 保存到数据库bean的集合
    '''
    def buildStockAccountOpenDataBean( self, dataFormat ):
       
        stockAccountOpenDataDatas = []
        for index, row in dataFormat.iterrows():
            stockAccountOpenDataBean = StockAccountOpenDataBean()
            self.__addAttributeValue( stockAccountOpenDataBean, row )
            stockAccountOpenDataDatas.insert( index, stockAccountOpenDataBean )
            
        return stockAccountOpenDataDatas
        
        
    def __addAttributeValue(self, bean, row):
        
        bean.date = row[ "date" ]

        if row[ "weekly_new" ] == None or isnan( row[ "weekly_new" ] ):
            bean.weeklyNew  = None
        else:
            bean.weeklyNew = row[ "weekly_new" ]
            
        if row[ "total" ] == None or isnan( row[ "total" ] ):
            bean.total  = None
        else:
            bean.total = row[ "total" ]
            
        if row[ "weekly_hold" ] == None or isnan( row[ "weekly_hold" ] ):
            bean.weeklyHold  = None
        else:
            bean.weeklyHold = row[ "weekly_hold" ]
            
        if row[ "weekly_trade" ] == None or isnan( row[ "weekly_trade" ] ):
            bean.weeklyTrade  = None
        else:
            bean.weeklyTrade = row[ "weekly_trade" ]