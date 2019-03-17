#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.ild.dao.IndexLineDayDao -- 指数日线行情数据库DAO工具类

com.financial.ild.dao.IndexLineDayDao is a 
数据库DAO工具类，主要用于指数日线行情表的操作

It defines classes_and_methods
def getStockBasicDict( self ):    获取股票基本数据，以 dict 形式返回
def saveIndexLineDayDatas( self, kLineDayDatas ):    保存股票指数日线行情数据
def getLastIndexLineDayDate( self , SQL, stockCode ):    获取股票的最后一条指数日线行情数据的时间
def __getMyDBSession( self ):    获取数据库连接

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.ild.log.IndexLineDayLog import IndexLineDayLog

from com.financial.common.bean.StockBasicBean import StockBasicBean
from com.financial.common.db.MySqlDBConnection import MySqlDBConnection

from sqlalchemy.sql import text

class IndexLineDayDao:
    
    '''
    @summary: 获取股票基本数据，以 dict 形式返回
    '''
    def getStockBasicDict( self ):
        
        IndexLineDayLog().getLog().info( "开始获取股票基础数据" )
        
        mySqlDBSession = self.__getMyDBSession()
        datas = mySqlDBSession.query( StockBasicBean ).all()
        mySqlDBSession.close()
        
        dataDict = dict()
        for data in datas:
            dataDict.setdefault( data.tsCode, data )
            
        IndexLineDayLog().getLog().info( "获取股票基础数据完毕" )
            
        return dataDict
    
    '''
    @summary: 保存股票指数日线行情数据
    
    @param stockBasicDatas: 所有要保存的股票指数日线行情数据的 list 
    '''
    def saveIndexLineDayDatas( self, kLineDatas ):
        
        IndexLineDayLog().getLog().info( "开始保存股票指数日线行情数据" )
        mySqlDBSession = self.__getMyDBSession()
      
        for data in kLineDatas:
            mySqlDBSession.add( data )
              
        mySqlDBSession.commit()
        mySqlDBSession.close()
        IndexLineDayLog().getLog().info( "保存股票指数日线行情数据完毕" )
        
    '''
    @summary: 获取股票的最后一条指数日线行情数据的时间
    
    @param SQL: 执行查询的SQL语句
    @param stockCode: 股票代码
    
    @return: 最后一条指数日线行情数据的时间
    '''
    def getLastIndexLineDayDate( self , SQL, stockCode ):
        IndexLineDayLog().getLog().info( "开始获取指数日线行情最后一条数据的交易时间" )
        mySqlDBSession = self.__getMyDBSession()
        result = mySqlDBSession.execute( text(SQL), {"tsCode" : stockCode}  )
        date = result.first()[ 0 ]
        IndexLineDayLog().getLog().info( "获取到指数日线行情最后一条数据的交易时间" )
        
        result.close()
        mySqlDBSession.close()
        
        return date
        
    '''
    @summary: 获取数据库连接
    
    @return: 数据库连接
    '''
    def __getMyDBSession( self ):
        
        IndexLineDayLog().getLog().info( "获取数据库连接会话" )
        mySqlDB = MySqlDBConnection()
        mySqlDBSession = mySqlDB.getMysqlDBSession()
        IndexLineDayLog().getLog().info( "已获取数据库连接会话" )
        
        return mySqlDBSession