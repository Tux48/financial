#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.kld.util.BuildKLineDayBeanUtil -- 构建要保存到数据库的K线bean的工具类

com.financial.kld.util.BuildKLineDayBeanUtil is a 
一个单例类，根据不同的条件构建相应要保存到数据库的K线bean

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
import threading
from math import isnan

from com.financial.kld.bean.KLineDay000Bean import KLineDay000Bean
from com.financial.kld.bean.KLineDay001Bean import KLineDay001Bean 
from com.financial.kld.bean.KLineDay002Bean import KLineDay002Bean
from com.financial.kld.bean.KLineDay300Bean import KLineDay300Bean
from com.financial.kld.bean.KLineDay600Bean import KLineDay600Bean
from com.financial.kld.bean.KLineDay601Bean import KLineDay601Bean
from com.financial.kld.bean.KLineDay603Bean import KLineDay603Bean

class BuildKLineDayBeanUtil:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( BuildKLineDayBeanUtil, "_instance" ):
            with BuildKLineDayBeanUtil.__instance_lock:
                if not hasattr( BuildKLineDayBeanUtil, "_instance" ):
                    BuildKLineDayBeanUtil._instance = object.__new__( cls )
                    
        return BuildKLineDayBeanUtil._instance
    
    def __init__( self  ):
        pass
    
    
    '''
    @summary: 根据不同的股票代码前缀构建并返回相应的保存到数据库bean的集合。
    
    @param stockCodePrefix: 股票代码前缀
    @param dataFormat: 格式化后的K线数据
    
    @return: 保存到数据库bean的集合
    '''
    def buildKLineDayBean( self, stockCodePrefix, dataFormat ):
       
        if stockCodePrefix == "000":
            return self.__buildKLineDay000( dataFormat )
        elif stockCodePrefix == "001":
            return self.__buildKLineDay001( dataFormat )
        elif stockCodePrefix == "002":
            return self.__buildKLineDay002( dataFormat )
        elif stockCodePrefix == "300":
            return self.__buildKLineDay300( dataFormat )
        elif stockCodePrefix == "600":
            return self.__buildKLineDay600( dataFormat )
        elif stockCodePrefix == "601":
            return self.__buildKLineDay601( dataFormat )
        elif stockCodePrefix == "603":
            return self.__buildKLineDay603( dataFormat )
        else:
            return []
        
        
    def __buildKLineDay000( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLineDay000Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLineDay001( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLineDay001Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLineDay002( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLineDay002Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLineDay300( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLineDay300Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLineDay600( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLineDay600Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLineDay601( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLineDay601Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildKLineDay603( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = KLineDay603Bean()
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