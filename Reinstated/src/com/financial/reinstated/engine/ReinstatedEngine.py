#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.reinstated.engine.ReinstatedEngine -- 复权数据引擎

com.financial.reinstated.engine.ReinstatedEngine is a 复权数据引擎

It defines classes_and_methods
def start( self ):    启动数据加载及处理
def __reinstatedDataProcess( self, stockBasicBean ):    复权数据加载、格式化、保存
def __getStockBasicDict( self ):    获取股票基本信息
def __getCurrentDate( self ):    返回yyyymmdd的时间格式的字符串
def __getNextDayStr( self, dateStr ):    指定的时间加一天，并返回yyyymmdd的时间格式的字符串
def __getLastReinstatedDate( self, SQL, stockBasicBean ):    获取股票的复权数据的最后一条交易时间
def __getStockCodePrefix( self, stockCode ):    获取股票代码的前3位
def __getReinstatedDatas( self, stockCode, startDate, endDate ):    获取指定时间段内股票的复权数据
def __saveReinstatedData( self , kLineDatas ):    保存复权数据

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import time
import datetime

from com.financial.reinstated.util.BuildReinstatedSQLUtil import BuildReinstatedSQLUtil
from com.financial.reinstated.util.BuildReinstatedBeanUtil import BuildReinstatedBeanUtil

from com.financial.reinstated.api.ReinstatedAPI import ReinstatedAPI
from com.financial.reinstated.dao.ReinstatedDao import ReinstatedDao
from com.financial.reinstated.log.ReinstatedLog import ReinstatedLog

class ReinstatedEngine:
    
    ## 存放股票基本数据的字典
    __stockBasicDatas = None
    
    ## 复权类型-未复权
    __REINSTATED_NONE = 0
    
    ## 复权类型-前复权
    __REINSTATED_QFQ = 1
    
    ## 复权类型-后复权
    __REINSTATED_HFQ = 2
    
    
    '''
    @summary: 启动数据加载及处理
    '''
    def start( self ):
        self.__getStockBasicDict()
        for stockData in self.__stockBasicDatas.values():
            try:
                self.__reinstatedNoneHistoryDataProcess( stockData )
                self.__reinstatedQfqHistoryDataProcess( stockData )
                self.__reinstatedHfqHistoryDataProcess( stockData )
            except Exception:
                logInfo = "{} 股票出现错误".format( stockData.tsCode )
                ReinstatedLog.getLog( self ).error( logInfo )
    
    
    def __reinstatedNoneDataProcess( self, stockBasicBean ):
        self.__reinstatedDataProcess( stockBasicBean, self.__REINSTATED_NONE )
        
    def __reinstatedQfqDataProcess( self, stockBasicBean ):
        self.__reinstatedDataProcess( stockBasicBean, self.__REINSTATED_QFQ )
        
    def __reinstatedHfqDataProcess( self, stockBasicBean ):
        self.__reinstatedDataProcess( stockBasicBean, self.__REINSTATED_HFQ )
    
    
    '''
    @summary: 复权数据加载、格式化、保存
    
    @param stockBasicBean: 股票基本数据
    '''    
    def __reinstatedDataProcess( self, stockBasicBean ):
        stockCode = stockBasicBean.tsCode
        stockCodePrefix = self.__getStockCodePrefix( stockCode )
        
        querySQL = BuildReinstatedSQLUtil().buildSQL( stockCodePrefix )
        if querySQL != None:
            startDate = self.__getLastReinstatedDate( querySQL, stockBasicBean )
            endDate = self.__getCurrentDate() ## K线数据获取结束时间为当前时间
            
            reinstatedDatasFormat = self.__getReinstatedDatas( stockCode, startDate, endDate )
            reinstatedDatas = BuildReinstatedBeanUtil().buildReinstatedBean( stockCodePrefix, reinstatedDatasFormat )
            self.__saveReinstatedData( reinstatedDatas )
            
        time.sleep( 5 )
    
    
    def __reinstatedNoneHistoryDataProcess( self, stockBasicBean ):
        self.__reinstatedHistoryDataProcess( stockBasicBean, self.__REINSTATED_NONE )
        
    def __reinstatedQfqHistoryDataProcess( self, stockBasicBean ):
        self.__reinstatedHistoryDataProcess( stockBasicBean, self.__REINSTATED_QFQ )
        
    def __reinstatedHfqHistoryDataProcess( self, stockBasicBean ):
        self.__reinstatedHistoryDataProcess( stockBasicBean, self.__REINSTATED_HFQ )
        
        
    '''
    
    '''    
    def __reinstatedHistoryDataProcess( self, stockBasicBean, reinstatedType ):
        stockCode = stockBasicBean.tsCode
        stockCodePrefix = self.__getStockCodePrefix( stockCode )
        
        startDate = stockBasicBean.listDate
        date = datetime.datetime.strptime( startDate, "%Y%m%d" )
        endDate = ( date + datetime.timedelta( days = 365 ) ).strftime( "%Y%m%d"  )
        year = startDate[ 0:4 ]
        
        rtype = None
        
        if reinstatedType == 1:
            rtype = "qfq"
        elif reinstatedType == 2:
            rtype = "hfq"
            
        while True:
            
            if year > "2019":
                break
            
            year = startDate[ 0:4 ]
            
            reinstatedDatasFormat = self.__getReinstatedDatas( stockCode, rtype, startDate, endDate )
            reinstatedDatas = BuildReinstatedBeanUtil().buildReinstatedBean( stockCodePrefix, reinstatedDatasFormat, reinstatedType )
            self.__saveReinstatedData( reinstatedDatas )
            
            date = datetime.datetime.strptime( endDate, "%Y%m%d" )
            startDate = ( date + datetime.timedelta( days = 1 ) ).strftime( "%Y%m%d"  )
            
            date = datetime.datetime.strptime( startDate, "%Y%m%d" )
            endDate = ( date + datetime.timedelta( days = 365 ) ).strftime( "%Y%m%d"  )
            
            time.sleep( 5 )
        
        
    '''
    @summary: 获取股票基本信息
    
    @return: 所有股票基本信息列表
    '''       
    def __getStockBasicDict( self ):
        self.__stockBasicDatas = ReinstatedDao().getStockBasicDict()
        
        
    '''
    @summary: 返回yyyymmdd的时间格式的字符串
    
    @return: yyyymmdd的时间格式的字符串
    '''
    def __getCurrentDate( self ):
        return datetime.datetime.now().strftime( "%Y%m%d" )
        
    '''
    @summary: 指定的时间加一天，并返回yyyymmdd的时间格式的字符串
    
    @return: yyyymmdd的下一天时间格式的字符串
    '''
    def __getNextDayStr( self, dateStr ):
        date = datetime.datetime.strptime( dateStr, "%Y%m%d" )
        nextDay = date + datetime.timedelta( days = 1 )

        return nextDay.strftime( "%Y%m%d"  )
    
    '''
    @summary: 获取股票的复权数据的最后一条交易时间
    
    @param SQL: 执行查询的SQL
    @param stockBasicBean: 股票基本数据
    
    @return:  复权数据的最后一条交易时间
    '''
    def __getLastReinstatedDate( self, SQL, stockBasicBean ):
        
        '''
        获取该股票K线数据的最大交易时间，如果不为None，
        将开始时间设置为最大交易时间加一天
        '''
        stockCode = stockBasicBean.tsCode
        startDate = ReinstatedDao().getLastReinstatedDate( SQL, stockCode )
        
        if startDate != None:
            startDate  =self.__getNextDayStr( startDate )
        else:
            startDate = stockBasicBean.listDate ## 默认的K线数据获取开始时间为股票上市时间
                
        return startDate
    
    '''
    @summary: 获取股票代码的前3位
    
    @return: 股票代码的前3位
    '''
    def __getStockCodePrefix( self, stockCode ):
        return stockCode[ 0:3 ]
    
    '''
    @summary:  获取指定时间段内股票的复权数据
    
    @param stockCode: 股票代码
    @param startDate: 开始时间
    @param endDate: 结束时间
    
    @return:  指定时间段内股票的复权数据
    '''
    def __getReinstatedDatas( self, stockCode, reinstatedType, startDate, endDate ):
        return ReinstatedAPI().getReinstatedDatas( stockCode, reinstatedType, startDate, endDate )
    
    
    '''
     @summary: 保存复权数据
     
     @param kLineDatas: 复权数据集合   
    '''
    def __saveReinstatedData( self , kLineDatas ):
        ReinstatedDao().saveReinstatedDatas( kLineDatas )