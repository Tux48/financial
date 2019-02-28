#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.klw.dao.KLineWeekDao -- 日K线数据库DAO工具类

com.financial.klw.dao.KLineWeekDao is a 
数据库DAO工具类，主要用于日K线表的操作

It defines classes_and_methods
def getStockBasicDict( self ):    获取股票基本数据，以 dict 形式返回
def saveKLineWeekDatas( self, kLineWeekDatas ):    保存股票周K线数据
def getLastKLineWeekDate( self , SQL, stockCode ):    获取股票的最后一条周K线数据的时间
def __getMyDBSession( self ):    获取数据库连接

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.klw.log.KLineWeekLog import KLineWeekLog

from com.financial.common.bean.StockBasicBean import StockBasicBean
from com.financial.common.db.MySqlDBConnection import MySqlDBConnection

from sqlalchemy.sql import text

class KLineWeekDao:
    
    '''
    @summary: 获取股票基本数据，以 dict 形式返回
    '''
    def getStockBasicDict( self ):
        
        KLineWeekLog().getLog().info( "开始获取股票基础数据" )
        
        mySqlDBSession = self.__getMyDBSession()
        datas = mySqlDBSession.query( StockBasicBean ).all()
        mySqlDBSession.close()
        
        dataDict = dict()
        for data in datas:
            dataDict.setdefault( data.tsCode, data )
            
        KLineWeekLog().getLog().info( "获取股票基础数据完毕" )
            
        return dataDict
    
    '''
    @summary: 保存股票周K线数据
    
    @param stockBasicDatas: 所有要保存的股票K线数据的 list 
    '''
    def saveKLineWeekDatas( self, kLineWeekDatas ):
        
        KLineWeekLog().getLog().info( "开始保存股票周K线数据" )
        mySqlDBSession = self.__getMyDBSession()
      
        for data in kLineWeekDatas:
            mySqlDBSession.add( data )
              
        mySqlDBSession.commit()
        mySqlDBSession.close()
        KLineWeekLog().getLog().info( "保存股票周K线数据完毕" )
        
    '''
    @summary: 获取股票的最后一条周K线数据的时间
    
    @param SQL: 执行查询的SQL语句
    @param stockCode: 股票代码
    
    @return: 最后一条日K线数据的时间
    '''
    def getLastKLineWeekDate( self , SQL, stockCode ):
        KLineWeekLog().getLog().info( "开始获取周K线最后一条数据的交易时间" )
        mySqlDBSession = self.__getMyDBSession()
        result = mySqlDBSession.execute( text(SQL), {"tsCode" : stockCode}  )
        date = result.first()[ 0 ]
        KLineWeekLog().getLog().info( "获取到周K线最后一条数据的交易时间" )
        
        result.close()
        mySqlDBSession.close()
        
        return date
        
    '''
    @summary: 获取数据库连接
    
    @return: 数据库连接
    '''
    def __getMyDBSession( self ):
        
        KLineWeekLog().getLog().info( "获取数据库连接会话" )
        mySqlDB = MySqlDBConnection()
        mySqlDBSession = mySqlDB.getMysqlDBSession()
        KLineWeekLog().getLog().info( "已获取数据库连接会话" )
        
        return mySqlDBSession