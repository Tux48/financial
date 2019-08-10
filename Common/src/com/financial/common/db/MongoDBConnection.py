#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2018-12-25

com.financial.common.db.MongoDBConnection -- MongoDB数据库边接类

com.financial.common.db.MongoDBConnection is a 
MongoDB数据库边接类，此类是一个单例类。

It defines classes_and_methods    def getMongoDBConnection( self ):    获取数据库连连，每次调用生成一个新的连接。

@author: Administrator

@version: 0.1

@copyright:  2018 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import threading
from pymongo import MongoClient

from com.financial.common.cfg.MongoDBConfig import MongoDBConfig

class MongoDBConnection( object ):
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单位下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单位下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( MongoDBConnection, "_instance" ):
            with MongoDBConnection.__instance_lock:
                if not hasattr( MongoDBConnection, "_instance" ):
                    MongoDBConnection._instance = object.__new__( cls )
                    
        return MongoDBConnection._instance
        
    def __init__( self ):
        pass
    
    '''
    @summary: 获取数据库连连，每次调用生成一个新的连接。
    '''
    def getMongoDBConnection( self ):
        dbConfig = MongoDBConfig()
        configDict = dbConfig.getConfigInfo()
        host = configDict.get( "host" )
        port = int( configDict.get( "port" ) )
        
        mongoDBClient = MongoClient( host, port )
        
        return mongoDBClient
    
    