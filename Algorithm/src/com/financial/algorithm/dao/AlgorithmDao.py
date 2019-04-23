#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.algorithm.dao.AlgorithmDao -- 日K线数据库DAO工具类

com.financial.algorithm.dao.AlgorithmDao is a 
数据库DAO工具类，主要用于日K线表的操作

It defines classes_and_methods
def getStockBasicDict( self ):    获取股票基本数据，以 dict 形式返回
def saveAlgorithmDatas( self, AlgorithmDatas ):    保存股票K线数据
def getLastAlgorithmDate( self , SQL, stockCode ):    获取股票的最后一条日K线数据的时间
def __getMyDBSession( self ):    获取数据库连接

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.algorithm.log.AlgorithmLog import AlgorithmLog

from com.financial.common.bean.StockBasicBean import StockBasicBean
from com.financial.common.db.MySqlDBConnection import MySqlDBConnection

from sqlalchemy.sql import text

class AlgorithmDao:
    
    '''
    @summary: 获取股票基本数据，以 dict 形式返回
    '''
    def getStockBasicDict( self ):
        
        AlgorithmLog().getLog().info( "开始获取股票基础数据" )
        
        mySqlDBSession = self.__getMyDBSession()
        datas = mySqlDBSession.query( StockBasicBean ).all()
        mySqlDBSession.close()
        
        dataDict = dict()
        for data in datas:
            dataDict.setdefault( data.tsCode, data )
            
        AlgorithmLog().getLog().info( "获取股票基础数据完毕" )
            
        return dataDict
    
        
    '''
    @summary: 获取股票的最后一条日K线数据的时间
    
    @param SQL: 执行查询的SQL语句
    @param stockCode: 股票代码
    
    @return: 最后一条日K线数据的时间
    '''
    def getAlgorithmDate( self , SQL, stockCode ):
        AlgorithmLog().getLog().info( "开始获取K线最后一条数据的交易时间" )
        mySqlDBSession = self.__getMyDBSession()
        result = mySqlDBSession.execute( text(SQL), {"tsCode" : stockCode}  )
        
        datas = []
        index = 0
        for row in result:
            tradeDate = row[ 0 ]
            open1 = row[ 1 ]    # 不知为啥，open会有警告，所以改成open1
            high = row[ 2 ]
            low = row[ 3 ]
            close = row[ 4 ]
            preClose = row[ 5 ]
            change = row[ 6 ]
            pctChg = row[ 7 ]
            vol = row[ 8 ]
            amount = row[ 9 ]
            datas.insert( index, [ tradeDate, open1, high, low, close, preClose, change, pctChg, vol, amount ] )
            
            index += 1
            
        AlgorithmLog().getLog().info( "获取到K线最后一条数据的交易时间" )
        
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