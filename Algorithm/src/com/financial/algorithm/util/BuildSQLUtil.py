#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.algorithm.util.BuildSQLUtil -- 构建查询SQL的工具类

com.financial.algorithm.util.BuildSQLUtil is a 
一个单例类，根据不同的条件构建相应的查询SQL

It defines classes_and_methods
def buildKLineSQL( self, stockCodePrefix ):    根据不同的股票代码前缀返回相应的SQL语句

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import threading

class BuildSQLUtil:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( BuildSQLUtil, "_instance" ):
            with BuildSQLUtil.__instance_lock:
                if not hasattr( BuildSQLUtil, "_instance" ):
                    BuildSQLUtil._instance = object.__new__( cls )
                    
        return BuildSQLUtil._instance
    
    def __init__( self  ):
        pass
    
    
    '''
    @summary: 根据不同的股票代码前缀返回相应的SQL语句。
    
    @param stockCodePrefix: 股票代码前缀
    
    @return: 查询SQL
    '''
    def buildKLineSQL( self, stockCodePrefix ):
       
        if stockCodePrefix == "000":
            return "select trade_date, `open`, high, low, `close`, pre_close, `change`, pct_chg, vol, amount from k_line_day_000 where ts_code=:tsCode order by trade_date"
        elif stockCodePrefix == "001":
            return "select trade_date, `open`, high, low, `close`, pre_close, `change`, pct_chg, vol, amount from k_line_day_001 where ts_code=:tsCode order by trade_date"
        elif stockCodePrefix == "002":
            return "select trade_date, `open`, high, low, `close`, pre_close, `change`, pct_chg, vol, amount from k_line_day_002 where ts_code=:tsCode order by trade_date"
        elif stockCodePrefix == "300":
            return "select trade_date, `open`, high, low, `close`, pre_close, `change`, pct_chg, vol, amount from k_line_day_300 where ts_code=:tsCode order by trade_date"
        elif stockCodePrefix == "600":
            return "select trade_date, `open`, high, low, `close`, pre_close, `change`, pct_chg, vol, amount from k_line_day_600 where ts_code=:tsCode order by trade_date"
        elif stockCodePrefix == "601":
            return "select trade_date, `open`, high, low, `close`, pre_close, `change`, pct_chg, vol, amount from k_line_day_601 where ts_code=:tsCode order by trade_date"
        elif stockCodePrefix == "603":
            return "select trade_date, `open`, high, low, `close`, pre_close, `change`, pct_chg, vol, amount from k_line_day_603 where ts_code=:tsCode order by trade_date"
        else:
            return None