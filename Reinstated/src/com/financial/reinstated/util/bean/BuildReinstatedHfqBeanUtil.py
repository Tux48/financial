#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.reinstated.util.BuildReinstatedHfqBeanUtil -- 构建要保存到数据库的复权bean的工具类

com.financial.reinstated.util.BuildReinstatedHfqBeanUtil is a 
一个单例类，根据不同的条件构建相应要保存到数据库的复权bean

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
import threading
from math import isnan

from com.financial.reinstated.bean.hfq.ReinstatedHfq000Bean import ReinstatedHfq000Bean
from com.financial.reinstated.bean.hfq.ReinstatedHfq001Bean import ReinstatedHfq001Bean 
from com.financial.reinstated.bean.hfq.ReinstatedHfq002Bean import ReinstatedHfq002Bean
from com.financial.reinstated.bean.hfq.ReinstatedHfq300Bean import ReinstatedHfq300Bean
from com.financial.reinstated.bean.hfq.ReinstatedHfq600Bean import ReinstatedHfq600Bean
from com.financial.reinstated.bean.hfq.ReinstatedHfq601Bean import ReinstatedHfq601Bean
from com.financial.reinstated.bean.hfq.ReinstatedHfq603Bean import ReinstatedHfq603Bean

class BuildReinstatedHfqBeanUtil:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( BuildReinstatedHfqBeanUtil, "_instance" ):
            with BuildReinstatedHfqBeanUtil.__instance_lock:
                if not hasattr( BuildReinstatedHfqBeanUtil, "_instance" ):
                    BuildReinstatedHfqBeanUtil._instance = object.__new__( cls )
                    
        return BuildReinstatedHfqBeanUtil._instance
    
    def __init__( self  ):
        pass
    
    
    '''
    @summary: 根据不同的股票代码前缀构建并返回相应的保存到数据库bean的集合。
    
    @param stockCodePrefix: 股票代码前缀
    @param dataFormat: 格式化后的K线数据
    @param reinstatedType: 复权类型
    
    @return: 保存到数据库bean的集合
    '''
    def buildReinstatedHfqBean( self, stockCodePrefix, dataFormat ):
       
        if stockCodePrefix == "000":
            return self.__buildReinstatedHfq000( dataFormat )
        elif stockCodePrefix == "001":
            return self.__buildReinstatedHfq001( dataFormat )
        elif stockCodePrefix == "002":
            return self.__buildReinstatedHfq002( dataFormat )
        elif stockCodePrefix == "300":
            return self.__buildReinstatedHfq300( dataFormat )
        elif stockCodePrefix == "600":
            return self.__buildReinstatedHfq600( dataFormat )
        elif stockCodePrefix == "601":
            return self.__buildReinstatedHfq601( dataFormat )
        elif stockCodePrefix == "603":
            return self.__buildReinstatedHfq603( dataFormat )
        else:
            return []
        
        
    def __buildReinstatedHfq000( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = ReinstatedHfq000Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.append( kLineBean )
            index
            
        return kLineDatas
        
    def __buildReinstatedHfq001( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = ReinstatedHfq001Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.append( kLineBean )
            index
            
        return kLineDatas
        
    def __buildReinstatedHfq002( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = ReinstatedHfq002Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.append( kLineBean )
            index
            
        return kLineDatas
        
    def __buildReinstatedHfq300( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = ReinstatedHfq300Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.append( kLineBean )
            index
            
        return kLineDatas
        
    def __buildReinstatedHfq600( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = ReinstatedHfq600Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.append( kLineBean )
            index
            
        return kLineDatas
        
    def __buildReinstatedHfq601( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = ReinstatedHfq601Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.append( kLineBean )
            index
            
        return kLineDatas
        
    def __buildReinstatedHfq603( self, dataFormat ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = ReinstatedHfq603Bean()
            self.__addAttributeValue( kLineBean, row )
            kLineDatas.append( kLineBean )
            index
            
        return kLineDatas
    
    def __addAttributeValue( self, bean, row ):
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