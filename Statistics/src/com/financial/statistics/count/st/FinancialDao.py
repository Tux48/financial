#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.statistics.dao.StatisticsDao -- 统计数据库DAO工具类

com.financial.statistics.dao.StatisticsDao is a 
数据库DAO工具类，主要用于统计的操作

It defines classes_and_methods
def getStockBasicDict( self ):    获取股票基本数据，以 dict 形式返回
def saveStatisticsDatas( self, StatisticsDatas ):    保存统计数据
def deleteStatisticsDatas( self ):    删除所有统计数据
def __getMyDBSession( self ):    获取数据库连接

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import threading
from sqlalchemy.sql import text

from com.financial.statistics.log.StatisticsLog import StatisticsLog
from com.financial.common.db.MySqlDBConnection import MySqlDBConnection


class FinancialDao:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( FinancialDao, "_instance" ):
            with FinancialDao.__instance_lock:
                if not hasattr( FinancialDao, "_instance" ):
                    FinancialDao._instance = object.__new__( cls )
                    
        return FinancialDao._instance
    
    def __init__( self  ):
        pass
    
    
    '''
    @summary: 获取股票基本数据，以 list 形式返回
    '''
    def getStockDatas( self, SQL, tsCode ):
        
        StatisticsLog().getLog().info( "开始获取股票基础数据" )
        
        mySqlDBSession = MySqlDBConnection().getMysqlDBSession()
        result = mySqlDBSession.execute( text( SQL ), { "tsCode": tsCode } )
        
        datas = []
        for row in result:
            datas.append( [ row[ 0 ], row[ 1 ], row[ 2 ], row[ 3 ], row[ 4 ] ] )
            
        result.close()
        mySqlDBSession.close()
        
        StatisticsLog().getLog().info( "获取股票基础数据完毕" )
            
        return datas
    
    
    '''
    @summary: 获取股票基本数据，以 list 形式返回
    '''
    def getIndexDatas( self, SQL ):
        
        StatisticsLog().getLog().info( "开始获取指数基础数据" )
        
        mySqlDBSession = MySqlDBConnection().getMysqlDBSession()
        result = mySqlDBSession.execute( text( SQL ) )
        
        datas = []
        for row in result:
            datas.append( [ row[ 0 ], row[ 1 ], row[ 2 ], row[ 3 ], row[ 4 ] ] )
            
        result.close()
        mySqlDBSession.close()
        
        StatisticsLog().getLog().info( "获取指数数据完毕" )
            
        return datas
    
    
    '''
    @summary: 获取股票基本数据，以 dict 形式返回
    '''
    def getTsCodes( self ):
        
        StatisticsLog().getLog().info( "开始获取股票基础数据" )
        
        mySqlDBSession = MySqlDBConnection().getMysqlDBSession()
        result = mySqlDBSession.execute( text( "select ts_code from stock_basic" ) )
        mySqlDBSession.close()
        
        datas = []
        for row in result:
            datas.append( row[ 0 ] )
            
        result.close()
        mySqlDBSession.close()
        
        StatisticsLog().getLog().info( "获取股票基础数据完毕" )
            
        return datas
    
    
    '''
    @summary: 测试用方法
    '''
    def getAllNameChangeDatas( self ):
         
        StatisticsLog().getLog().info( "开始加载股票曾用名数据" )
         
        mySqlDBSession = MySqlDBConnection().getMysqlDBSession()
#         result = mySqlDBSession.execute( text( "select ts_code, name, start_date, end_date, change_reason from name_change where ts_code='600539.SH' order by ts_code, start_date asc" ) )
        result = mySqlDBSession.execute( text( "select ts_code, name, start_date, end_date, change_reason from name_change order by ts_code, start_date asc" ) )
       
        datas = []
        for row in result:
            datas.append( [ row[ 0 ], row[ 1 ], row[ 2 ], row[ 3 ], row[ 4 ] ] )
               
        result.close()
        mySqlDBSession.close()
         
        StatisticsLog().getLog().info( "股票曾用名数据加载完毕" )
         
        return datas