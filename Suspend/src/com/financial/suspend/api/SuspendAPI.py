320#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.suspend.api.SuspendAPI -- 获取股票数据的API接口

com.financial.suspend.api.SuspendAPI is a 
获取股票数据的API接口。此类是一个单例，只初始化一次API。

It defines classes_and_methods
def getSuspendDatas( self, stockCode, startDate, endDate ):    获取股票停复牌信息数据

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import threading
import pandas as pd

from com.financial.common.api.TushareAPI import TushareAPI

class SuspendAPI:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( SuspendAPI, "_instance" ):
            with SuspendAPI.__instance_lock:
                if not hasattr( SuspendAPI, "_instance" ):
                    SuspendAPI._instance = object.__new__( cls )
                    
        return SuspendAPI._instance
    
    def __init__( self  ):
        pass
    
    '''
    @summary: 获取股票停复牌信息数据
    
    @param stockCode: 股票代码
    @param suspendDate: 停牌时间
    
    @return: 指定股票代码、开始、结束时间段内的停复牌信息数据
    '''
    def getSuspendDatas( self, stockCode, suspendDate ):
        tsPro = TushareAPI().getTushareAPI()
        data = tsPro.suspend( ts_code= stockCode, suspend_date = suspendDate )
        
        return pd.DataFrame( data )