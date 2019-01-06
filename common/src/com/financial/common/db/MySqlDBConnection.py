#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2018-12-25

com.financial.common.db.MySqlDBConnection -- Mysql数据库连接类

com.financial.common.db.MySqlDBConnection is a 
Mysql数据库连接类，此类是一个单例类。

It defines classes_and_methods     def __initDB( self ):                    初始化数据库连接池
                                                    def getMysqlDBSession( self ):    从数据库连接池中返加一个连接

@author: Administrator

@version: 0.1

@copyright:  2018 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import threading

from com.financial.common.cfg.MySqlConfig import MySqlConfig
from builtins import int

class MySqlDBConnection( object ):
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    ## 数据库引擎
    mysqlDBSession = None
    
    DB_CONNECTION_URI = "mysql+pymysql://%s:%s@%s:%d/%s"
    
    '''
    @note: _instance 一定要是单位下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单位下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( MySqlDBConnection, "_instance" ):
            with MySqlDBConnection.__instance_lock:
                if not hasattr( MySqlDBConnection, "_instance" ):
                    MySqlDBConnection._instance = object.__new__( cls )
                    
        return MySqlDBConnection._instance
    
    def __init__( self  ):
        if self.__first_init:
            self.__initDB()
            self.__first_init = False
            
    '''
    @note: 配置文件的KEY是大写，程序序代码中必须要用小写获取value ？？？
    
    @summary: 初始化数据库连接池
    '''
    def __initDB( self ):
        dbConfig = MySqlConfig()
        configDict = dbConfig.getConfigInfo()
        
        dbUser = configDict.get( "username" )
        dbPassword = configDict.get( "password" )
        dbHost = configDict.get( "host" )
        dbPort = int( configDict.get( "port" ) )
        dbName = configDict.get( "database" )
        dbEncoding = configDict.get( "encoding" )
        dbEcho = ( True if configDict.get( "echo" ).lower() == "true" else False )
        
        poolSize = int( configDict.get( "pool_size" ) )
        poolRecycle = int( configDict.get( "pool_recycle" ) )
        maxOverflow = int( configDict.get( "max_overflow" ) )
        poolTimeOut = int( configDict.get( "pool_timeout" ) )
        
        isAutoComit = ( True if configDict.get( "autocomit" ).lower() == "true" else False )
        isAutoFlush = ( True if configDict.get( "autoflush" ).lower() == "true" else False )
        isExpireOnComit = ( True if configDict.get( "expire_on_commit" ).lower() == "true" else False )
        
        mysqlDBEngine = create_engine( self.DB_CONNECTION_URI % ( dbUser, dbPassword, dbHost, dbPort, dbName ),
                                            encoding = dbEncoding, echo = dbEcho, pool_size = poolSize, pool_recycle = poolRecycle,
                                            max_overflow = maxOverflow, pool_timeout = poolTimeOut, connect_args = {'charset': 'utf8'} )
        
        self.mysqlDBSession  = scoped_session( sessionmaker( bind = mysqlDBEngine, autocommit = isAutoComit, autoflush = isAutoFlush, 
                                                             expire_on_commit = isExpireOnComit ) )
        
    '''
    @summary: 从数据库连接池中返加一个连接
    '''
    def getMysqlDBSession( self ):
        dbSession = self.mysqlDBSession()
        
        return dbSession