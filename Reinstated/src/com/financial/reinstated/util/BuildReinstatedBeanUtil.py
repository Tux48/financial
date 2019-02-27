#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.reinstated.util.BuildKLineBeanUtil -- 构建要保存到数据库的复权bean的工具类

com.financial.reinstated.util.BuildKLineBeanUtil is a 
一个单例类，根据不同的条件构建相应要保存到数据库的复权bean

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
import threading
from math import isnan

from com.financial.reinstated.bean.Reinstated000Bean import Reinstated000Bean
from com.financial.reinstated.bean.Reinstated001Bean import Reinstated001Bean 
from com.financial.reinstated.bean.Reinstated002Bean import Reinstated002Bean
from com.financial.reinstated.bean.Reinstated300Bean import Reinstated300Bean
from com.financial.reinstated.bean.Reinstated600Bean import Reinstated600Bean
from com.financial.reinstated.bean.Reinstated601Bean import Reinstated601Bean
from com.financial.reinstated.bean.Reinstated603Bean import Reinstated603Bean

class BuildReinstatedBeanUtil:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( BuildReinstatedBeanUtil, "_instance" ):
            with BuildReinstatedBeanUtil.__instance_lock:
                if not hasattr( BuildReinstatedBeanUtil, "_instance" ):
                    BuildReinstatedBeanUtil._instance = object.__new__( cls )
                    
        return BuildReinstatedBeanUtil._instance
    
    def __init__( self  ):
        pass
    
    
    '''
    @summary: 根据不同的股票代码前缀构建并返回相应的保存到数据库bean的集合。
    
    @param stockCodePrefix: 股票代码前缀
    @param dataFormat: 格式化后的K线数据
    @param reinstatedType: 复权类型
    
    @return: 保存到数据库bean的集合
    '''
    def buildReinstatedBean( self, stockCodePrefix, dataFormat, reinstatedType ):
       
        if stockCodePrefix == "000":
            return self.__buildReinstated000( dataFormat, reinstatedType )
        elif stockCodePrefix == "001":
            return self.__buildReinstated001( dataFormat, reinstatedType )
        elif stockCodePrefix == "002":
            return self.__buildReinstated002( dataFormat, reinstatedType )
        elif stockCodePrefix == "300":
            return self.__buildReinstated300( dataFormat, reinstatedType )
        elif stockCodePrefix == "600":
            return self.__buildReinstated600( dataFormat, reinstatedType )
        elif stockCodePrefix == "601":
            return self.__buildReinstated601( dataFormat, reinstatedType )
        elif stockCodePrefix == "603":
            return self.__buildReinstated603( dataFormat, reinstatedType )
        else:
            return []
        
        
    def __buildReinstated000( self, dataFormat, reinstatedType ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = Reinstated000Bean()
            self.__addAttributeValue( kLineBean, row, reinstatedType )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildReinstated001( self, dataFormat, reinstatedType ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = Reinstated001Bean()
            self.__addAttributeValue( kLineBean, row, reinstatedType )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildReinstated002( self, dataFormat, reinstatedType ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = Reinstated002Bean()
            self.__addAttributeValue( kLineBean, row, reinstatedType )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildReinstated300( self, dataFormat, reinstatedType ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = Reinstated300Bean()
            self.__addAttributeValue( kLineBean, row, reinstatedType )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildReinstated600( self, dataFormat, reinstatedType ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = Reinstated600Bean()
            self.__addAttributeValue( kLineBean, row, reinstatedType )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildReinstated601( self, dataFormat, reinstatedType ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = Reinstated601Bean()
            self.__addAttributeValue( kLineBean, row, reinstatedType )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
        
    def __buildReinstated603( self, dataFormat, reinstatedType ):
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            kLineBean = Reinstated603Bean()
            self.__addAttributeValue( kLineBean, row, reinstatedType )
            kLineDatas.insert( index, kLineBean )
            
        return kLineDatas
    
    def __addAttributeValue( self, bean, row, reinstatedType ):
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
            
        bean.type = reinstatedType