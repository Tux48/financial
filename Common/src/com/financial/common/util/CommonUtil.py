#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年5月30日

com.financial.common.util.CommonUtil -- shortdesc

com.financial.common.util.CommonUtil is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

# import time
import datetime
import threading


class CommonUtil:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( CommonUtil, "_instance" ):
            with CommonUtil.__instance_lock:
                if not hasattr( CommonUtil, "_instance" ):
                    CommonUtil._instance = object.__new__( cls )
                    
        return CommonUtil._instance
    
    def __init__( self  ):
        pass
    
    '''
    @summary: 获取股票代码的前3位
        
    @return: 股票代码的前3位
    '''
    def getStockCodePrefix( self, tsCode ):
        return tsCode[ 0:3 ]
    
    
    '''
    @summary: 获取股票代码的后缀
    
    @return: 股票代码的后缀
    '''
    def getStockCodeSuffix( self, tsCode ):
        return tsCode[ 7:9 ]
    
    
    '''
    返回yyyymmdd的时间格式的字符串
        
    @return: yyyymmdd的时间格式的字符串
    '''
    def getCurrentDate( self ):
        return datetime.datetime.now().strftime( "%Y%m%d" )