#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.klm.log.KLineMonthLog -- 月K线模块日志类

com.financial.klm.log.KLineMonthLog is a 
月K线模块日志类，是一个单例工具类。

It defines classes_and_methods
def __initLog( self ):    初始化日志
def getLog( self ):    返回已初始化好的日志

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import threading

from com.financial.klm.cfg.KLineMonthConfig import KLineMonthConfig
from com.financial.common.log.FinancialLog import FinancialLog

class KLineMonthLog:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    ## 日志
    __kLineMonthLog = None
    
    '''
    @note: _instance 一定要是单位下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单位下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( KLineMonthLog, "_instance" ):
            with KLineMonthLog.__instance_lock:
                if not hasattr( KLineMonthLog, "_instance" ):
                    KLineMonthLog._instance = object.__new__( cls )
                    
        return KLineMonthLog._instance
    
    def __init__( self  ):
        if self.__first_init:
            self.__initLog()
            self.__first_init = False
           
    '''
    @summary: 初始化日志
    ''' 
    def __initLog( self ):
        logFilePath = KLineMonthConfig().getConfigInfo().get( "log_path" )    ## 日志文件路径
        logFileName = KLineMonthConfig().getConfigInfo().get( "log_file" )    ## 日志名
        self.__kLineMonthLog = FinancialLog( logFilePath, logFileName ).getLogger()
        
    ''''
    @summary: 返回已初始化好的日志
    ''' 
    def getLog( self ):
        return self.__kLineMonthLog
