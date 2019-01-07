#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-5

com.financial.stockbasic.api.StockBasicAPI -- 获取股基本信息

com.financial.stockbasic.api.StockBasicAPI is a 
获取股基本信息工具类。加载股票基本数据后，对比数据库中已有的股票基本数据。
去除已存在的，只保存新上市的股票数据。此类为单例。

It defines classes_and_methods

@author: Tux48

@version: 0.1

@see: com.financial.common.bean.StockBasicBean

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import threading
import pandas as pd

from com.financial.common.api.TushareAPI import TushareAPI
from com.financial.common.bean.StockBasicBean import StockBasicBean

class StockBasicAPI:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单位下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单位下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( StockBasicAPI, "_instance" ):
            with StockBasicAPI.__instance_lock:
                if not hasattr( StockBasicAPI, "_instance" ):
                    StockBasicAPI._instance = object.__new__( cls )
                    
        return StockBasicAPI._instance
    
    def __init__( self  ):
        pass
    
    '''
    @summary: 加载股票基本数据，并以股票代码为key，股票数据bean为value，放入字典中
    '''
    def getStockBasicData( self ):
        tsPro = TushareAPI().getTushareAPI()
        data = tsPro.stock_basic( fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs' )
        dataFormat = pd.DataFrame( data )
        
        newDataDict = dict()
        for index, row in dataFormat.iterrows():
            index   ## 这行代码没意义，为了去除警告而写。强迫症，不想看到有警告。
            bean = StockBasicBean()
            bean.tsCode = row[ "ts_code" ]
            bean.symbol = row[ "symbol" ]
            bean.name = row[ "name" ]
            bean.area = row[ "area" ]
            bean.industry = row[ "industry" ]
            bean.fullname = row[ "fullname" ]
            bean.enname = row[ "enname" ]
            bean.market = row[ "market" ]
            bean.exchange = row[ "exchange" ]
            bean.currType = row[ "curr_type" ]
            bean.listStatus = row[ "list_status" ]
            bean.listDate = row[ "list_date" ]
            bean.deListDate = row[ "delist_date" ]
            bean.isHZ = row[ "is_hs" ]
            
            newDataDict.setdefault( row[ "ts_code" ], bean )
        
        return newDataDict