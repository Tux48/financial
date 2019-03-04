#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.klw.util.BuildKLineWeekBeanUtil -- 构建要保存到数据库的周K线bean的工具类

com.financial.klw.util.BuildKLineWeekBeanUtil is a 
一个单例类，根据不同的条件构建相应要保存到数据库的周K线bean

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
import threading
from math import isnan

from com.financial.klw.bean.KLineWeek000Bean import KLineWeek000Bean
from com.financial.klw.bean.KLineWeek001Bean import KLineWeek001Bean 
from com.financial.klw.bean.KLineWeek002Bean import KLineWeek002Bean
from com.financial.klw.bean.KLineWeek300Bean import KLineWeek300Bean
from com.financial.klw.bean.KLineWeek600Bean import KLineWeek600Bean
from com.financial.klw.bean.KLineWeek601Bean import KLineWeek601Bean
from com.financial.klw.bean.KLineWeek603Bean import KLineWeek603Bean

class BuildKLineWeekBeanUtil:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( BuildKLineWeekBeanUtil, "_instance" ):
            with BuildKLineWeekBeanUtil.__instance_lock:
                if not hasattr( BuildKLineWeekBeanUtil, "_instance" ):
                    BuildKLineWeekBeanUtil._instance = object.__new__( cls )
                    
        return BuildKLineWeekBeanUtil._instance
    
    def __init__( self  ):
        pass
    
    
    '''
    @summary: 根据不同的股票代码前缀构建并返回相应的保存到数据库bean的集合。
    
    @param stockCodePrefix: 股票代码前缀
    @param dataFormat: 格式化后的K线数据
    
    @return: 保存到数据库bean的集合
    '''
    def buildKLineWeekBean( self, stockCodePrefix, dataFormat ):
       
        if stockCodePrefix == "000":
            return self.__buildKLineWeek000( dataFormat )
        elif stockCodePrefix == "001":
            return self.__buildKLineWeek001( dataFormat )
        elif stockCodePrefix == "002":
            return self.__buildKLineWeek002( dataFormat )
        elif stockCodePrefix == "300":
            return self.__buildKLineWeek300( dataFormat )
        elif stockCodePrefix == "600":
            return self.__buildKLineWeek600( dataFormat )
        elif stockCodePrefix == "601":
            return self.__buildKLineWeek601( dataFormat )
        elif stockCodePrefix == "603":
            return self.__buildKLineWeek603( dataFormat )
        else:
            return []
        
        
    def __buildKLineWeek000( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLineWeek000Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLineWeek001( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLineWeek001Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLineWeek002( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLineWeek002Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLineWeek300( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLineWeek300Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLineWeek600( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLineWeek600Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLineWeek601( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLineWeek601Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLineWeek603( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLineWeek603Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
    
    def __addAttributeValue(self, bean, row):
        bean.tsCode = row[ "ts_code" ]
        bean.tsDate = row[ "trade_date" ]
        
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
            
        if row[ "close" ] == None or isnan( row[ "close" ] ):
            bean.close = 0.0
        else:
            bean.close = row[ "close" ]
            
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