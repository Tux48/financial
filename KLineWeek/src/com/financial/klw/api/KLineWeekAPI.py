#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.klw.api.KLineAPI -- 获取股票数据的API接口

com.financial.klw.api.KLineAPI is a 
获取股票数据的API接口。此类是一个单例，只初始化一次API。

It defines classes_and_methods
def getKLineWeekDatas( self, stockCode, startDate, endDate ):    获取股票周K线数据

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import threading
import pandas as pd

from com.financial.common.api.TushareAPI import TushareAPI

class KLineWeekAPI:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( KLineWeekAPI, "_instance" ):
            with KLineWeekAPI.__instance_lock:
                if not hasattr( KLineWeekAPI, "_instance" ):
                    KLineWeekAPI._instance = object.__new__( cls )
                    
        return KLineWeekAPI._instance
    
    def __init__( self  ):
        pass
    
    '''
    @summary: 获取股票周K线数据
    
    @param stockCode: 股票代码
    @param startDate: 获取的开始时间
    @param endDate: 获取的结束时间
    
    @return: 指定股票代码、开始、结束时间段内的周K线数据
    '''
    def getKLineWeekDatas( self, stockCode, startDate, endDate ):
        tsPro = TushareAPI().getTushareAPI()
        data = tsPro.weekly( ts_code= stockCode, start_date = startDate, end_date = endDate )
        
        return pd.DataFrame( data )