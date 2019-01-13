#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.kline.dao.KLineDao -- shortdesc

com.financial.kline.dao.KLineDao is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.kline.log.KLineLog import KLineLog

from com.financial.common.bean.StockBasicBean import StockBasicBean
from com.financial.common.db.MySqlDBConnection import MySqlDBConnection

from sqlalchemy.sql import text

class KLineDao:
    
    '''
    @summary: 获取股票基本数据，以 dict 形式返回
    '''
    def getStockBasicDict( self ):
        
        KLineLog().getLog().info( "开始获取股票基础数据" )
        
        mySqlDBSession = self.__getMyDBSession()
        datas = mySqlDBSession.query( StockBasicBean ).all()
        mySqlDBSession.close()
        
        dataDict = dict()
        for data in datas:
            dataDict.setdefault( data.tsCode, data )
            
        KLineLog().getLog().info( "获取股票基础数据完毕" )
            
        return dataDict
    
    '''
    @summary: 保存股票K线数据
    
    @param stockBasicDatas: 所有要保存的股票K线数据的 list 
    '''
    def saveKLineDatas( self, kLineDatas ):
        
        KLineLog().getLog().info( "开始保存股票K线数据" )
        mySqlDBSession = self.__getMyDBSession()
      
        for data in kLineDatas:
            mySqlDBSession.add( data )
              
        mySqlDBSession.commit()
        mySqlDBSession.close()
        KLineLog().getLog().info( "保存股票K线数据完毕" )
        
    '''
    
    '''
    def getLastKLineDate( self , SQL, stockCode ):
        KLineLog().getLog().info( "开始获取K线最后一条数据的交易时间" )
        mySqlDBSession = self.__getMyDBSession()
        result = mySqlDBSession.execute( text(SQL), {"tsCode" : stockCode}  )
        date = result.first()[ 0 ]
        KLineLog().getLog().info( "获取到K线最后一条数据的交易时间为: " )
        
        result.close()
        mySqlDBSession.close()
        
        return date
        
    '''
    @summary: 获取数据库连接
    '''
    def __getMyDBSession( self ):
        
        KLineLog().getLog().info( "获取数据库连接会话" )
        mySqlDB = MySqlDBConnection()
        mySqlDBSession = mySqlDB.getMysqlDBSession()
        KLineLog().getLog().info( "已获取数据库连接会话" )
        
        return mySqlDBSession