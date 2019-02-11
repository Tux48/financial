#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.kline.util.BuildKLineBeanUtil -- 构建要保存到数据库的K线bean的工具类

com.financial.kline.util.BuildKLineBeanUtil is a 
一个单例类，根据不同的条件构建相应要保存到数据库的K线bean

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
import threading
from math import isnan

from com.financial.kline.bean.KLine000Bean import KLine000Bean
from com.financial.kline.bean.KLine001Bean import KLine001Bean 
from com.financial.kline.bean.KLine002Bean import KLine002Bean
from com.financial.kline.bean.KLine300Bean import KLine300Bean
from com.financial.kline.bean.KLine600Bean import KLine600Bean
from com.financial.kline.bean.KLine601Bean import KLine601Bean
from com.financial.kline.bean.KLine603Bean import KLine603Bean

class BuildKLineBeanUtil:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( BuildKLineBeanUtil, "_instance" ):
            with BuildKLineBeanUtil.__instance_lock:
                if not hasattr( BuildKLineBeanUtil, "_instance" ):
                    BuildKLineBeanUtil._instance = object.__new__( cls )
                    
        return BuildKLineBeanUtil._instance
    
    def __init__( self  ):
        pass
    
    
    '''
    @summary: 根据不同的股票代码前缀构建并返回相应的保存到数据库bean的集合。
    
    @param stockCodePrefix: 股票代码前缀
    @param dataFormat: 格式化后的K线数据
    
    @return: 保存到数据库bean的集合
    '''
    def buildKLineBean( self, stockCodePrefix, dataFormat ):
       
        if stockCodePrefix == "000":
            return self.__buildKLine000( dataFormat )
        elif stockCodePrefix == "001":
            return self.__buildKLine001( dataFormat )
        elif stockCodePrefix == "002":
            return self.__buildKLine002( dataFormat )
        elif stockCodePrefix == "300":
            return self.__buildKLine300( dataFormat )
        elif stockCodePrefix == "600":
            return self.__buildKLine600( dataFormat )
        elif stockCodePrefix == "601":
            return self.__buildKLine601( dataFormat )
        elif stockCodePrefix == "603":
            return self.__buildKLine603( dataFormat )
        else:
            return []
        
        
    def __buildKLine000( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLine000Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLine001( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLine001Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLine002( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLine002Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLine300( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLine300Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLine600( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLine600Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLine601( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLine601Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLine603( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLine603Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
    
    def __addAttributeValue(self, bean, row):
        bean.tsCode = row[ "ts_code" ]
        bean.tsDate = row[ "trade_date" ]
        
        if isnan(  row[ "open" ] ):
            bean.open = 0.0
        else:
            bean.open = row[ "open" ]
            
        if isnan( row[ "high" ] ):
            bean.high = 0.0
        else:
            bean.high = row[ "high" ]
            
        if isnan( row[ "low" ] ):
            bean.low = 0.0
        else:
            bean.low = row[ "low" ]
            
        if isnan( row[ "close" ] ):
            bean.close = 0.0
        else:
            bean.close = row[ "close" ]
            
        if isnan( row[ "pre_close" ] ):
            bean.preClose  =0.0
        else:
            bean.preClose = row[ "pre_close" ]
            
        if isnan( row[ "change" ] ):
            bean.change = 0.0
        else:
            bean.change = row[ "change" ]
            
        if isnan( row[ "pct_chg" ] ):
            bean.pctChg = 0.0
        else:
            bean.pctChg = row[ "pct_chg" ]
            
        if isnan( row[ "vol" ] ):
            bean.vol  =0.0
        else:
            bean.vol = row[ "vol" ]
        
        if isnan( row[ "amount" ] ):
            bean.amount = 0.0
        else:
            bean.amount = row[ "amount" ]