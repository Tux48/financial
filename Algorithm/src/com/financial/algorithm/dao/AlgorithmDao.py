#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.algorithm.dao.AlgorithmDao -- 日K线数据库DAO工具类

com.financial.algorithm.dao.AlgorithmDao is a 
数据库DAO工具类，主要用于日K线表的操作

It defines classes_and_methods
def getAlgorithmDate( self , SQL, stockCode ):    根据SQL、股票或指数代码获取数据
def __getMyDBSession( self ):    获取数据库连接
def __transformDate( self, tradeDate )    将yyyymmdd时间格式转换为yyyy/mm/dd

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.algorithm.log.AlgorithmLog import AlgorithmLog

from com.financial.common.db.MySqlDBConnection import MySqlDBConnection

from sqlalchemy.sql import text

class AlgorithmDao:
    
    '''
    @summary: 根据SQL、股票或指数代码获取数据
    
    @param SQL: 执行查询的SQL语句
    @param tsCode: 股票或指数代码
    
    @return: 指定股票或指数代码的所有数据
    '''
    def getAlgorithmDate( self , SQL, tsCode ):
        AlgorithmLog().getLog().info( "开始获取数据" )
        mySqlDBSession = self.__getMyDBSession()
        result = mySqlDBSession.execute( text(SQL), {"tsCode" : tsCode}  )
        
        datas = []
        index = 0
        for row in result:
            tradeDate = self.__transformDate( row[ 0 ] )
            open1 = row[ 1 ]    # 不知为啥，open会有警告，所以改成open1
            close = row[ 2 ]
            low = row[ 3 ]
            high = row[ 4 ]
            volume = row[ 5 ]

            datas.insert( index, [ tradeDate, open1, close, low, high, volume ] )
            
            index += 1
            
        AlgorithmLog().getLog().info( "获取到数据" )
        
        result.close()
        mySqlDBSession.close()
        
        return datas
        
    '''
    @summary: 获取数据库连接
    
    @return: 数据库连接
    '''
    def __getMyDBSession( self ):
        
        AlgorithmLog().getLog().info( "获取数据库连接会话" )
        mySqlDB = MySqlDBConnection()
        mySqlDBSession = mySqlDB.getMysqlDBSession()
        AlgorithmLog().getLog().info( "已获取数据库连接会话" )
        
        return mySqlDBSession
    
    
    '''
    @summary: 将yyyymmdd时间格式转换为yyyy/mm/dd
    
    @param tradeDate: yyyymmdd时间格式
    
    @return: yyyy/mm/dd格式的时间
    '''
    def __transformDate( self, tradeDate ):
        return "{}-{}-{}".format( tradeDate[0:4], tradeDate[4:6], tradeDate[6:8] ) 