#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.reinstated.api.ReinstatedAPI -- 获取股票数据的API接口

com.financial.reinstated.api.ReinstatedAPI is a 
获取股票数据的API接口。此类是一个单例，只初始化一次API。

It defines classes_and_methods
def getKLineDatas( self, stockCode, adj, startDate, endDate ):    获取股票复权数据

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import threading
import pandas as pd
import tushare as ts

from com.financial.common.api.TushareAPI import TushareAPI

class ReinstatedAPI:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( ReinstatedAPI, "_instance" ):
            with ReinstatedAPI.__instance_lock:
                if not hasattr( ReinstatedAPI, "_instance" ):
                    ReinstatedAPI._instance = object.__new__( cls )
                    
        return ReinstatedAPI._instance
    
    def __init__( self  ):
        pass
    
    '''
    @summary: 获取股票日K线数据
    
    @param stockCode: 股票代码
    @param adj: 复权类型
    @param startDate: 获取的开始时间
    @param endDate: 获取的结束时间
    
    @return: 指定股票代码、开始、结束时间段内的日K线数据
    '''
    def getReinstatedDatas( self, stockCode, adj, startDate, endDate ):
        api = TushareAPI().getTushareAPI()
        data = ts.pro_bar( pro_api=api, ts_code= stockCode, adj=adj, start_date = startDate, end_date = endDate )
        
        return pd.DataFrame( data )