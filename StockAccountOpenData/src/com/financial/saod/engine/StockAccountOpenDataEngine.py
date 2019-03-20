#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.saod.engine.StockAccountOpenDataEngine -- shortdesc

com.financial.saod.engine.StockAccountOpenDataEngine is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import time
import datetime

from com.financial.saod.util.BuildStockAccountOpenDataBeanUtil import BuildStockAccountOpenDataBeanUtil

from com.financial.saod.api.StockAccountOpenDataAPI import StockAccountOpenDataAPI
from com.financial.saod.dao.StockAccountOpenDataDao import StockAccountOpenDataDao
from com.financial.saod.log.StockAccountOpenDataLog import StockAccountOpenDataLog

class StockAccountOpenDataEngine:
    
    ## 存放股票基本数据的字典
    __stockBasicDatas = None
    
    
    def start( self ):
        self.__stockAccountOpenDataProcess()

    
    '''
    
    '''    
    def __stockAccountOpenDataProcess( self ):
        
        startDate = self.__getLastStockAccountOpenDate( "select max(date) from stock_account_open_data" )
        endDate = self.__getCurrentDate() ## 每日指标数据获取结束时间为当前时间
              
        stockAccountOpenDataDatasFormat = self.__getStockAccountOpenDatas( startDate, endDate )
        stockAccountOpenDataDatas = BuildStockAccountOpenDataBeanUtil().buildStockAccountOpenDataBean( stockAccountOpenDataDatasFormat )
        self.__saveStockAccountOpenData( stockAccountOpenDataDatas )

        
    '''
    @summary: 获取股票基本信息
    
    @return: 所有股票基本信息列表
    '''       
    def __getStockBasicDict( self ):
        self.__stockBasicDatas = StockAccountOpenDataDao().getStockBasicDict()
        
        
    '''
    返回yyyymmdd的时间格式的字符串
    
    @return: yyyymmdd的时间格式的字符串
    '''
    def __getCurrentDate( self ):
        return datetime.datetime.now().strftime( "%Y%m%d" )
        
    '''
    指定的时间加一天，并返回yyyymmdd的时间格式的字符串
    
    @return: yyyymmdd的下一天时间格式的字符串
    '''
    def __getNextDayStr( self, dateStr ):
        date = datetime.datetime.strptime( dateStr, "%Y%m%d" )
        nextDay = date + datetime.timedelta( days = 1 )

        return nextDay.strftime( "%Y%m%d"  )
    
    '''
    @summary: 获取股票的每日指标数据的最后一条交易时间
    
    @param SQL: 执行查询的SQL
    @param stockBasicBean: 股票基本数据
    
    @return:  每日指标数据的最后一条交易时间
    '''
    def __getLastStockAccountOpenDate( self, SQL,  ):
        
        '''
        获取该股票每日指标数据的最大交易时间，如果不为None，
        将开始时间设置为最大交易时间加一天
        '''
        startDate = StockAccountOpenDataDao().getLastStockAccountOpenDate( SQL )
        
        if startDate != None:
            startDate  =self.__getNextDayStr( startDate )
        else:
            startDate = self.__getCurrentDate()
                
        return startDate
    
    
    '''
    @summary:  获取指定时间段内股票的每日指标数据
    
    @param stockCode: 股票代码
    @param startDate: 开始时间
    @param endDate: 结束时间
    
    @return:  指定时间段内股票的每日指标数据
    '''
    def __getStockAccountOpenDatas( self, startDate, endDate ):
        return StockAccountOpenDataAPI().getStockAccountOpenDatas( startDate, endDate )
    
    
    '''
     @summary: 保存每日指标数据
     
     @param TargetDatas: 每日指标数据集合   
    '''
    def __saveStockAccountOpenData( self , stockAccountOpenDataDatas ):
        StockAccountOpenDataDao().saveStockAccountOpenDatas( stockAccountOpenDataDatas )