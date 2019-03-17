#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.midt.engine.MarketIndexDayTargetEngine -- shortdesc

com.financial.midt.engine.MarketIndexDayTargetEngine is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import time
import datetime

from com.financial.midt.util.BuildMarketIndexDayTargetBeanUtil import BuildMarketIndexDayTargetBeanUtil

from com.financial.midt.api.MarketIndexDayTargetAPI import MarketIndexDayTargetAPI
from com.financial.midt.dao.MarketIndexDayTargetDao import MarketIndexDayTargetDao
from com.financial.midt.log.MarketIndexDayTargetLog import MarketIndexDayTargetLog

class MarketIndexDayTargetEngine:
    
    __TS_CODE_AND_LISTDATE = { '000001.SH': '20040101', '000016.SH': '20040101', '399001.SZ': '20040101', '399005.SZ': '20040101', '399006.SZ': '20040101' }
    
    def start( self ):
        for key in self.__TS_CODE_AND_LISTDATE.keys():
            try:
                listDate = self.__TS_CODE_AND_LISTDATE.get( key )
                self.__MarketIndexDayTargetDataProcess( key, listDate )
            except Exception:
                MarketIndexDayTargetLog.getLog(self).error( "{} 大盘指数出现错误".format( key ) )
    
    '''
    
    '''    
    def __MarketIndexDayTargetDataProcess( self, tsCode, listDate ):
         
        startDate = self.__getLastMarketIndexDayTargetDate( "select max(trade_date) from market_index_day_target where ts_code=:tsCode", tsCode, listDate )
        endDate = self.__getCurrentDate() ## 大盘指数每日指标数据获取结束时间为当前时间
             
        marketIndexDayTargetDatasFormat = self.__getMarketIndexDayTargetDatas( tsCode, startDate, endDate )
        marketIndexDayTargetDatas = BuildMarketIndexDayTargetBeanUtil().buildMarketIndexDayTargetBean( marketIndexDayTargetDatasFormat )
        self.__saveMarketIndexDayTargetData( marketIndexDayTargetDatas )
             
        time.sleep( 1 )
    
    
#     def __marketIndexDayTargetHistoryDataProcess( self, tsCode, listDate ):
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
#             matketIndexDayTargetDatasFormat = self.__getMarketIndexDayTargetDatas( tsCode, startDate, endDate )
#             matketIndexDayTargetDatas = BuildMarketIndexDayTargetBeanUtil().buildMarketIndexDayTargetBean( matketIndexDayTargetDatasFormat )
#             self.__saveMarketIndexDayTargetData( matketIndexDayTargetDatas )
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
    @summary: 获取股票的大盘指数每日指标数据的最后一条交易时间
    
    @param SQL: 执行查询的SQL
    @param listDate: 指数发布日期
    
    @return:  大盘指数每日指标数据的最后一条交易时间
    '''
    def __getLastMarketIndexDayTargetDate( self, SQL, tsCode, listDate ):
        
        '''
        获取该股票大盘指数每日指标数据的最大交易时间，如果不为None，
        将开始时间设置为最大交易时间加一天
        '''
        startDate = MarketIndexDayTargetDao().getLastMarketIndexDayTargetDate(SQL, tsCode)
        
        if startDate != None:
            startDate  =self.__getNextDayStr( startDate )
        else:
            startDate = listDate ## 默认的大盘指数每日指标数据获取开始时间为股票上市时间
                
        return startDate
    
    
    '''
    @summary:  获取指定时间段内股票的大盘指数每日指标数据
    
    @param stockCode: 指数代码
    @param startDate: 开始时间
    @param endDate: 结束时间
    
    @return:  指定时间段内股票的大盘指数每日指标数据
    '''
    def __getMarketIndexDayTargetDatas( self, tsCode, startDate, endDate ):
        return MarketIndexDayTargetAPI().getMarketIndexDayTargetDatas( tsCode, startDate, endDate )
    
    
    '''
     @summary: 保存大盘指数每日指标数据
     
     @param TargetDatas: 大盘指数每日指标数据集合   
    '''
    def __saveMarketIndexDayTargetData( self , marketIndexDayTargetDatas ):
        MarketIndexDayTargetDao().saveMarketIndexDayTargetDatas( marketIndexDayTargetDatas )