#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.reinstated.util.BuildReinstatedHfqSQLUtil -- 构建查询SQL的工具类

com.financial.reinstated.util.BuildReinstatedHfqSQLUtil is a 
一个单例类，根据不同的条件构建相应的查询SQL

It defines classes_and_methods
def buildSQL( self, stockCodePrefix ):    根据不同的股票代码前缀返回相应的SQL语句

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import threading

class BuildReinstatedHfqSQLUtil:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( BuildReinstatedHfqSQLUtil, "_instance" ):
            with BuildReinstatedHfqSQLUtil.__instance_lock:
                if not hasattr( BuildReinstatedHfqSQLUtil, "_instance" ):
                    BuildReinstatedHfqSQLUtil._instance = object.__new__( cls )
                    
        return BuildReinstatedHfqSQLUtil._instance
    
    def __init__( self  ):
        pass
    
    
    '''
    @summary: 根据不同的股票代码前缀返回相应的SQL语句。
    
    @param stockCodePrefix: 股票代码前缀
    
    @return: 查询SQL
    '''
    def buildSQL( self, stockCodePrefix ):
       
        if stockCodePrefix == "000":
            return "select max(trade_date) from reinstated_hfq_000 where ts_code=:tsCode"
        elif stockCodePrefix == "001":
            return "select max(trade_date) from reinstated_hfq_001 where ts_code=:tsCode"
        elif stockCodePrefix == "002":
            return "select max(trade_date) from reinstated_hfq_002 where ts_code=:tsCode"
        elif stockCodePrefix == "300":
            return "select max(trade_date) from reinstated_hfq_300 where ts_code=:tsCode"
        elif stockCodePrefix == "600":
            return "select max(trade_date) from reinstated_hfq_600 where ts_code=:tsCode"
        elif stockCodePrefix == "601":
            return "select max(trade_date) from reinstated_hfq_601 where ts_code=:tsCode"
        elif stockCodePrefix == "603":
            return "select max(trade_date) from reinstated_hfq_603 where ts_code=:tsCode"
        else:
            return None