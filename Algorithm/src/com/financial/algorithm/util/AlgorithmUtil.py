#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.algorithm.util.AlgorithmUtil -- 构建查询SQL的工具类

com.financial.algorithm.util.AlgorithmUtil is a 
一个单例类，根据不同的条件构建相应的查询SQL

It defines classes_and_methods
def buildKLineSQL( self, tsCodePrefix )    根据不同的股票代码前缀返回相应的SQL语句
ef buildIndexDaySQL( self, tsCodeSuffix )    根据不同的指数代码前缀返回相应的SQL语句
def get_tsCodePrefix( self, tsCode )    `获取股票代码的前3位
get_tsCodeSuffix( self, tsCode )    获取股票代码的后缀

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import threading

class AlgorithmUtil:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( AlgorithmUtil, "_instance" ):
            with AlgorithmUtil.__instance_lock:
                if not hasattr( AlgorithmUtil, "_instance" ):
                    AlgorithmUtil._instance = object.__new__( cls )
                    
        return AlgorithmUtil._instance
    
    def __init__( self  ):
        pass
    
    
    '''
    @summary: 根据不同的股票代码前缀返回相应的SQL语句。
    
    @param tsCodePrefix: 股票代码前缀
    
    @return: 查询SQL
    '''
    def buildKLineSQL( self, tsCodePrefix ):
       
        if tsCodePrefix == "000":
            return "select trade_date, `open`, `close`,  low, high, `vol`  from k_line_day_000 where ts_code=:tsCode order by trade_date"
        elif tsCodePrefix == "001":
            return "select trade_date, `open`, `close`,  low, high, `vol`  from k_line_day_001 where ts_code=:tsCode order by trade_date"
        elif tsCodePrefix == "002":
            return "select trade_date, `open`, `close`,  low, high, `vol`  from k_line_day_002 where ts_code=:tsCode order by trade_date"
        elif tsCodePrefix == "300":
            return "select trade_date, `open`, `close`,  low, high, `vol`  from k_line_day_300 where ts_code=:tsCode order by trade_date"
        elif tsCodePrefix == "600":
            return "select trade_date, `open`, `close`,  low, high, `vol`  from k_line_day_600 where ts_code=:tsCode order by trade_date"
        elif tsCodePrefix == "601":
            return "select trade_date, `open`, `close`,  low, high, `vol`  from k_line_day_601 where ts_code=:tsCode order by trade_date"
        elif tsCodePrefix == "603":
            return "select trade_date, `open`, `close`,  low, high, `vol`  from k_line_day_603 where ts_code=:tsCode order by trade_date"
        else:
            return None
        
                
    '''
    @summary: 根据不同的指数代码前缀返回相应的SQL语句。
    
    @param tsCodeSuffix: 指数代码前缀
    
    @return: 查询SQL
    '''
    def buildIndexDaySQL( self, tsCodeSuffix ):
       
        if tsCodeSuffix == "SH":
            return "select trade_date, `open`, `close`,  low, high, `vol` from index_line_day_sse where ts_code=:tsCode order by trade_date"
        elif tsCodeSuffix == "SZ":
            return "select trade_date, `open`, `close`,  low, high, `vol` from index_line_day_szse where ts_code=:tsCode order by trade_date"
        
        
    '''
    @summary: 获取股票代码的前3位
    
    @return: 股票代码的前3位
    '''
    def get_tsCodePrefix( self, tsCode ):
        return tsCode[ 0:3 ]
    
    
        '''
    @summary: 获取股票代码的后缀
    
    @return: 股票代码的后缀
    '''
    def get_tsCodeSuffix( self, tsCode ):
        return tsCode[ 7:9 ]