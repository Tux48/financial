#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.ta.engine.TargetDayEngine -- shortdesc

com.financial.ta.engine.TargetDayEngine is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import time
import datetime

from com.financial.ta.util.BuildTargetDaySQLUtil import BuildTargetDaySQLUtil
from com.financial.ta.util.BuildTargetDayBeanUtil import BuildTargetDayBeanUtil

from com.financial.ta.api.TargetDayAPI import TargetDayAPI
from com.financial.ta.dao.TargetDayDao import TargetDayDao
from com.financial.ta.log.TargetDayLog import TargetDayLog

class TargetDayEngine:
    
    ## 存放股票基本数据的字典
    __stockBasicDatas = None
    
    
    def start( self ):
        self.__getStockBasicDict()
        for stockData in self.__stockBasicDatas.values():
            try:
                self.__targetDayDataProcess( stockData )
            except Exception:
                TargetDayLog.getLog(self).error( "{} 股票出现错误".format( stockData.tsCode ) )
    
    '''
    
    '''    
    def __targetDayDataProcess( self, stockBasicBean ):
        stockCode = stockBasicBean.tsCode
        stockCodePrefix = self.__getStockCodePrefix( stockCode )
         
        querySQL = BuildTargetDaySQLUtil().buildSQL( stockCodePrefix )
        if querySQL != None:
            startDate = self.__getLastTargetDayDate( querySQL, stockBasicBean )
            endDate = self.__getCurrentDate() ## 每日指标数据获取结束时间为当前时间
             
            targetDayDatasFormat = self.__getTargetDayDatas( stockCode, startDate, endDate )
            targetDayDatas = BuildTargetDayBeanUtil().buildTargetDayBean( stockCodePrefix, targetDayDatasFormat )
            self.__saveTargetDayData( targetDayDatas )
             
        time.sleep( 1 )
    
    
#     def __TargetHistoryDataProcess( self, stockBasicBean ):
#         stockCode = stockBasicBean.tsCode
#         stockCodePrefix = self.__getStockCodePrefix( stockCode )
#          
#         startDate = stockBasicBean.listDate
#         date = datetime.datetime.strptime( startDate, "%Y%m%d" )
#         endDate = ( date + datetime.timedelta( days = 365 ) ).strftime( "%Y%m%d"  )
#         year = startDate[ 0:4 ]
#          
#         while True:
#              
#             if year > "2019":
#                 break
#              
#             year = startDate[ 0:4 ]
#              
#             targetDatasFormat = self.__getTargetDayDatas( stockCode, startDate, endDate )
#             targetDatas = BuildTargetDayBeanUtil().buildTargetDayBean( stockCodePrefix, targetDatasFormat )
#             self.__saveTargetDayData( targetDatas )
#              
#             date = datetime.datetime.strptime( endDate, "%Y%m%d" )
#             startDate = ( date + datetime.timedelta( days = 1 ) ).strftime( "%Y%m%d"  )
#              
#             date = datetime.datetime.strptime( startDate, "%Y%m%d" )
#             endDate = ( date + datetime.timedelta( days = 365 ) ).strftime( "%Y%m%d"  )
#              
#             time.sleep( 1 )
        
        
    '''
    @summary: 获取股票基本信息
    
    @return: 所有股票基本信息列表
    '''       
    def __getStockBasicDict( self ):
        self.__stockBasicDatas = TargetDayDao().getStockBasicDict()
        
        
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
    def __getLastTargetDayDate( self, SQL, stockBasicBean ):
        
        '''
        获取该股票每日指标数据的最大交易时间，如果不为None，
        将开始时间设置为最大交易时间加一天
        '''
        stockCode = stockBasicBean.tsCode
        startDate = TargetDayDao().getLastTargetDayDate(SQL, stockCode)
        
        if startDate != None:
            startDate  =self.__getNextDayStr( startDate )
        else:
            startDate = stockBasicBean.listDate ## 默认的每日指标数据获取开始时间为股票上市时间
                
        return startDate
    
    '''
    @summary: 获取股票代码的前3位
    
    @return: 股票代码的前3位
    '''
    def __getStockCodePrefix( self, stockCode ):
        return stockCode[ 0:3 ]
    
    '''
    @summary:  获取指定时间段内股票的每日指标数据
    
    @param stockCode: 股票代码
    @param startDate: 开始时间
    @param endDate: 结束时间
    
    @return:  指定时间段内股票的每日指标数据
    '''
    def __getTargetDayDatas( self, stockCode, startDate, endDate ):
        return TargetDayAPI().getTargetDayDatas( stockCode, startDate, endDate )
    
    
    '''
     @summary: 保存每日指标数据
     
     @param TargetDatas: 每日指标数据集合   
    '''
    def __saveTargetDayData( self , TargetDayDatas ):
        TargetDayDao().saveTargetDayDatas( TargetDayDatas )