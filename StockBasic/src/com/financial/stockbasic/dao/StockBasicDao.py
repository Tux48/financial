#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-4

com.financial.stockbasic.db.StockBasicDao -- shortdesc

com.financial.stockbasic.db.StockBasicDao is a description

It defines classes_and_methods

def saveStockBasicData( self, stockBasicDatas )    保存股票基本数据
def getStockBasicDatas( self )    获取股票基本数据，以 list 形式返回
def getStockBasicDict( self )    获取股票基本数据，以 dict 形式返回
def __getMyDBSession( self )    获取数据库连接

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.stockbasic.log.StockBasicLog import StockBasicLog
from com.financial.common.bean.StockBasicBean import StockBasicBean
from com.financial.common.db.MySqlDBConnection import MySqlDBConnection

class StockBasicDao:
   
    '''
    @summary: 保存股票基本数据
    
    @param stockBasicDatas: 所有要保存的股票基本数据的 list 
    '''
    def saveStockBasicData( self, stockBasicDatas ):
        
        StockBasicLog().getLog().info( "开始保存股票基本数据" )
        mySqlDBSession = self.__getMyDBSession()
      
        for data in stockBasicDatas:
            mySqlDBSession.add( data )
              
        mySqlDBSession.commit()
        mySqlDBSession.close()
        StockBasicLog().getLog().info( "保存股票基本数据完毕" )
        
    '''
    @summary: 获取股票基本数据，以 list 形式返回
    '''
    def getStockBasicDatas( self ):
        
        StockBasicLog().getLog().info( "开始获取股票基本数据" )
        mySqlDBSession = self.__getMyDBSession()
        stockBasicDatas = mySqlDBSession.query( StockBasicBean ).all()
        mySqlDBSession.close()
        StockBasicLog().getLog().info( "获取股票基本数据完毕" )
        
        return stockBasicDatas
    
    '''
    @summary: 获取股票基本数据，以 dict 形式返回
    '''
    def getStockBasicDict( self ):
        datas = self.getStockBasicDatas()
        dataDict = dict()
        
        for data in datas:
            dataDict.setdefault( data.tsCode, data )
            
        return dataDict
        
    '''
    @summary: 获取数据库连接
    '''
    def __getMyDBSession( self ):
        
        StockBasicLog().getLog().info( "获取数据库连接会话" )
        mySqlDB = MySqlDBConnection()
        mySqlDBSession = mySqlDB.getMysqlDBSession()
        StockBasicLog().getLog().info( "已获取数据库连接会话" )
        
        return mySqlDBSession