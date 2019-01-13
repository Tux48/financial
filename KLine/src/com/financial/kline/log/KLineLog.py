#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.kline.log.KLineLog -- shortdesc

com.financial.kline.log.KLineLog is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import threading

from com.financial.kline.cfg.KLineConfig import KLineConfig
from com.financial.common.log.FinancialLog import FinancialLog

class KLineLog:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    ## 日志
    __kLineLog = None
    
    '''
    @note: _instance 一定要是单位下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单位下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( KLineLog, "_instance" ):
            with KLineLog.__instance_lock:
                if not hasattr( KLineLog, "_instance" ):
                    KLineLog._instance = object.__new__( cls )
                    
        return KLineLog._instance
    
    def __init__( self  ):
        if self.__first_init:
            self.__initLog()
            self.__first_init = False
           
    '''
    @summary: 初始化日志
    ''' 
    def __initLog( self ):
        logFilePath = KLineConfig().getConfigInfo().get( "log_path" )    ## 日志文件路径
        logFileName = KLineConfig().getConfigInfo().get( "log_file" )    ## 日志名
        self.__kLineLog = FinancialLog( logFilePath, logFileName ).getLogger()
        
    ''''
    @summary: 返回已初始化好的日志
    ''' 
    def getLog( self ):
        return self.__kLineLog
