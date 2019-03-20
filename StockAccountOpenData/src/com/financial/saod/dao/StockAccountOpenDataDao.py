#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.saod.dao.StockAccountOpenDataDao -- 股票账户开户数据数据库DAO工具类

com.financial.saod.dao.StockAccountOpenDataDao is a 
数据库DAO工具类，主要用于股票账户开户数据表的操作

It defines classes_and_methods
def getStockBasicDict( self ):    获取股票基本数据，以 dict 形式返回
def saveStockAccountOpenDataDatas( self, stockAccountOpenDayDatas ):    保存股票股票账户开户数据数据
def getLastStockAccountOpenDate( self , SQL ):    获取股票的最后一条股票账户开户数据数据的时间
def __getMyDBSession( self ):    获取数据库连接

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.saod.log.StockAccountOpenDataLog import StockAccountOpenDataLog

from com.financial.common.bean.StockBasicBean import StockBasicBean
from com.financial.common.db.MySqlDBConnection import MySqlDBConnection

from sqlalchemy.sql import text

class StockAccountOpenDataDao:
    
    '''
    @summary: 获取股票基本数据，以 dict 形式返回
    '''
    def getStockBasicDict( self ):
        
        StockAccountOpenDataLog().getLog().info( "开始获取股票基础数据" )
        
        mySqlDBSession = self.__getMyDBSession()
        datas = mySqlDBSession.query( StockBasicBean ).all()
        mySqlDBSession.close()
        
        dataDict = dict()
        for data in datas:
            dataDict.setdefault( data.tsCode, data )
            
        StockAccountOpenDataLog().getLog().info( "获取股票基础数据完毕" )
            
        return dataDict
    
    '''
    @summary: 保存股票股票账户开户数据数据
    
    @param stockBasicDatas: 所有要保存的股票股票账户开户数据数据的 list 
    '''
    def saveStockAccountOpenDatas( self, stockAccountOpenDatas ):
        
        StockAccountOpenDataLog().getLog().info( "开始保存股票股票账户开户数据数据" )
        mySqlDBSession = self.__getMyDBSession()
      
        for data in stockAccountOpenDatas:
            mySqlDBSession.add( data )
              
        mySqlDBSession.commit()
        mySqlDBSession.close()
        StockAccountOpenDataLog().getLog().info( "保存股票股票账户开户数据数据完毕" )
        
    '''
    @summary: 获取股票的最后一条股票账户开户数据数据的时间
    
    @param SQL: 执行查询的SQL语句
    @param stockCode: 股票代码
    
    @return: 最后一条股票账户开户数据数据的时间
    '''
    def getLastStockAccountOpenDate( self , SQL ):
        StockAccountOpenDataLog().getLog().info( "开始获取股票账户开户数据最后一条数据的交易时间" )
        mySqlDBSession = self.__getMyDBSession()
        result = mySqlDBSession.execute( text(SQL)  )
        date = result.first()[ 0 ]
        StockAccountOpenDataLog().getLog().info( "获取到股票账户开户数据最后一条数据的交易时间" )
        
        result.close()
        mySqlDBSession.close()
        
        return date
        
    '''
    @summary: 获取数据库连接
    
    @return: 数据库连接
    '''
    def __getMyDBSession( self ):
        
        StockAccountOpenDataLog().getLog().info( "获取数据库连接会话" )
        mySqlDB = MySqlDBConnection()
        mySqlDBSession = mySqlDB.getMysqlDBSession()
        StockAccountOpenDataLog().getLog().info( "已获取数据库连接会话" )
        
        return mySqlDBSession