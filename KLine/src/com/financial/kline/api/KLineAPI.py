320#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.kline.api.KLineAPI -- shortdesc

com.financial.kline.api.KLineAPI is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import threading
import pandas as pd

from com.financial.common.api.TushareAPI import TushareAPI

class KLineAPI:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单位下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单位下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( KLineAPI, "_instance" ):
            with KLineAPI.__instance_lock:
                if not hasattr( KLineAPI, "_instance" ):
                    KLineAPI._instance = object.__new__( cls )
                    
        return KLineAPI._instance
    
    def __init__( self  ):
        pass
    
    '''
    
    '''
    def getKLineDatas( self, stockCode, startDate, endDate ):
        tsPro = TushareAPI().getTushareAPI()
        data = tsPro.daily( ts_code= stockCode, start_date = startDate, end_date = endDate )
        
        return pd.DataFrame( data )