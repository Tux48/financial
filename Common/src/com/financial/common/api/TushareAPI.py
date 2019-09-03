#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年1月7日

com.financial.common.api.TushareAPI -- 初始化股票API

com.financial.common.api.TushareAPI is a 
初始化股票API，这是一个单例。

It defines classes_and_methods
def getTushareAPI( self )    获取股票API

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
import tushare as ts

import threading

class TushareAPI:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    ## 股票接口 token
    __TS_TOKEN = "ba9b75382e295fb2074d4c8530a3fafeff5d88f3381604102c"

    ## 股票接口
    __tsPro = None
    
    '''
    @note: _instance 一定要是单位下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单位下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( TushareAPI, "_instance" ):
            with TushareAPI.__instance_lock:
                if not hasattr( TushareAPI, "_instance" ):
                    TushareAPI._instance = object.__new__( cls )
                    
        return TushareAPI._instance
    
    def __init__( self  ):
        if self.__first_init:
            self.__initAPI()
            self.__first_init = False
    
    '''
    @summary: 初始化获取股票数据API接口
    '''
    def __initAPI( self ):
        '''
        初始化股票API接口
        '''
        ts.set_token( self.__TS_TOKEN )
        self.__tsPro =ts.pro_api()
        
    '''
    获取股票API
    '''
    def getTushareAPI( self ):
        return self.__tsPro