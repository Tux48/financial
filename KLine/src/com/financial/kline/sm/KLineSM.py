#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-8

com.financial.kline.sm.KLineSM -- shortdesc

com.financial.kline.sm.KLineSM is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import threading

from com.financial.kline.sm.KLineState000 import KLineState000
from com.financial.kline.sm.KLineState000 import KLineState001
from com.financial.kline.sm.KLineState000 import KLineState002
from com.financial.kline.sm.KLineState000 import KLineState300
from com.financial.kline.sm.KLineState000 import KLineState600
from com.financial.kline.sm.KLineState000 import KLineState601
from com.financial.kline.sm.KLineState000 import KLineState603

from com.financial.kline.dao.KLineDao import KLineDao

class KLineSM:
    
## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    ## 存放各种状态计算类的集合
    __kLineStats = []
    
    ## 存放股票基本数据的字典
    __stockBasicDatas = None
    
    '''
    @note: _instance 一定要是单位下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单位下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( KLineSM, "_instance" ):
            with KLineSM.__instance_lock:
                if not hasattr( KLineSM, "_instance" ):
                    KLineSM._instance = object.__new__( cls )
                    
        return KLineSM._instance
    
    def __init__( self  ):
        if self.__first_init:
            self.__initKLineSM()
            self.__first_init = False
           
    '''
    @summary: 初始化日志
    ''' 
    def __initKLineSM( self ):
        self.__kLineStats.insert( KLineState000() )
        self.__kLineStats.insert( KLineState001() )
        self.__kLineStats.insert( KLineState002() )
        self.__kLineStats.insert( KLineState300() )
        self.__kLineStats.insert( KLineState600() )
        self.__kLineStats.insert( KLineState601() )
        self.__kLineStats.insert( KLineState603() )
        
        self.__stockBasicDatas = KLineDao().getStockBasicDict()
        
    def match( self ):
        for stockData in self.__stockBasicDatas:
            for state in self.__kLineStats:
                state.match( stockData )