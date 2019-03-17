#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.ild.engine.IndexLineDayEngine -- shortdesc

com.financial.ild.engine.IndexLineDayEngine is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import time
import datetime

from com.financial.ild.util.BuildIndexLineDayBeanUtil import BuildIndexLineDayBeanUtil

from com.financial.ild.api.IndexLineDayAPI import IndexLineDayAPI
from com.financial.ild.dao.IndexLineDayDao import IndexLineDayDao

class IndexLineDayEngine:
    
    def start( self ):
        self.__SSE()
        self.__SZSE()
                
    def __SSE( self ):
        indexBasicDatas = self.__getIndexBasicDatas( "SSE" )
        for index, row in indexBasicDatas.iterrows():
            self.__indexLineDaySSEDataProcess( row[ "ts_code" ], row[ "base_date" ] )
                
            index
        
    def __SZSE( self ):
        indexBasicDatas = self.__getIndexBasicDatas( "SZSE" )
        for index, row in indexBasicDatas.iterrows():
            self.__indexLineDaySZSEDataProcess( row[ "ts_code" ], row[ "base_date" ] )
                
            index
        
    
    '''
    
    '''    
    def __indexLineDaySSEDataProcess( self, tsCode, baseDate ):
         
        startDate = self.__getLastIndexLineDayDate( "select max(trade_date) from index_line_day_sse where ts_code=:tsCode", tsCode, baseDate )
        endDate = self.__getCurrentDate() ## 指数日线行情数据获取结束时间为当前时间
             
        indexLineDayDatasFormat = self.__getIndexLineDayDatas( tsCode, startDate, endDate )
        indexLineDayDatas = BuildIndexLineDayBeanUtil().buildIndexLineDaySSEBean( indexLineDayDatasFormat )
        self.__saveIndexLineDayData( indexLineDayDatas )
             
        time.sleep( 1 )
        
    def __indexLineDaySZSEDataProcess( self, tsCode, baseDate ):
         
        startDate = self.__getLastIndexLineDayDate( "select max(trade_date) from index_line_day_szse where ts_code=:tsCode", tsCode, baseDate )
        endDate = self.__getCurrentDate() ## 指数日线行情数据获取结束时间为当前时间
             
        indexLineDayDatasFormat = self.__getIndexLineDayDatas( tsCode, startDate, endDate )
        indexLineDayDatas = BuildIndexLineDayBeanUtil().buildIndexLineDaySSEBean( indexLineDayDatasFormat )
        self.__saveIndexLineDayData( indexLineDayDatas )
             
        time.sleep( 1 )
    
    
#     def __IndexLineDaySSEHistoryDataProcess( self, tsCode, listDate ):
#          
#         startDate = listDate
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
#             indexLineDayDatasFormat = self.__getIndexLineDayDatas( tsCode, startDate, endDate )
#             indexLineDayDatas = BuildIndexLineDayBeanUtil().buildIndexLineDaySSEBean( indexLineDayDatasFormat )
#             self.__saveIndexLineDayData( indexLineDayDatas )
#              
#             date = datetime.datetime.strptime( endDate, "%Y%m%d" )
#             startDate = ( date + datetime.timedelta( days = 1 ) ).strftime( "%Y%m%d"  )
#              
#             date = datetime.datetime.strptime( startDate, "%Y%m%d" )
#             endDate = ( date + datetime.timedelta( days = 365 ) ).strftime( "%Y%m%d"  )
#              
#             time.sleep( 1 )
#             
#             
#     def __IndexLineDaySZSEHistoryDataProcess( self, tsCode, listDate ):
#          
#         startDate = listDate
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
#             indexLineDayDatasFormat = self.__getIndexLineDayDatas( tsCode, startDate, endDate )
#             indexLineDayDatas = BuildIndexLineDayBeanUtil().buildIndexLineDaySZSEBean( indexLineDayDatasFormat )
#             self.__saveIndexLineDayData( indexLineDayDatas )
#              
#             date = datetime.datetime.strptime( endDate, "%Y%m%d" )
#             startDate = ( date + datetime.timedelta( days = 1 ) ).strftime( "%Y%m%d"  )
#              
#             date = datetime.datetime.strptime( startDate, "%Y%m%d" )
#             endDate = ( date + datetime.timedelta( days = 365 ) ).strftime( "%Y%m%d"  )
#              
#             time.sleep( 1 )
        
        
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
    @summary: 获取股票的指数日线行情数据的最后一条交易时间
    
    @param SQL: 执行查询的SQL
    @param stockBasicBean: 股票基本数据
    
    @return:  指数日线行情数据的最后一条交易时间
    '''
    def __getLastIndexLineDayDate( self, SQL, tsCode, listDate ):
        
        '''
        获取该股票指数日线行情数据的最大交易时间，如果不为None，
        将开始时间设置为最大交易时间加一天
        '''
        startDate = IndexLineDayDao().getLastIndexLineDayDate(SQL, tsCode)
        
        if startDate != None:
            startDate  =self.__getNextDayStr( startDate )
        else:
            startDate = listDate ## 默认的指数日线行情数据获取开始时间为股票上市时间
                
        return startDate
    
    
    '''
    @summary:  获取指定时间段内股票的指数日线行情数据
    
    @param tsCode: 指数代码
    @param startDate: 开始时间
    @param endDate: 结束时间
    
    @return:  指定时间段内股票的指数日线行情数据
    '''
    def __getIndexLineDayDatas( self, tsCode, startDate, endDate ):
        return IndexLineDayAPI().getIndexLineDayDatas( tsCode, startDate, endDate )
    
    
    '''
    @summary:  获取指数基本数据
    
    @param market: 指数代码
    
    @return:  指数基本数据
    '''
    def __getIndexBasicDatas( self, market ):
        return IndexLineDayAPI.getIndexLineDayBasicDatas( self, market )
    
    '''
     @summary: 保存指数日线行情数据
     
     @param TargetDatas: 指数日线行情数据集合   
    '''
    def __saveIndexLineDayData( self , indexLineDayDatas ):
        IndexLineDayDao().saveIndexLineDayDatas( indexLineDayDatas )