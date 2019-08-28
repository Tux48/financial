#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年7月26日

com.financial.statistics.st.ST -- ST统计基础类

com.financial.statistics.st.ST is a ST统计基础类，包含了所有数据统计方法

It defines classes_and_methods
def getStockDatas( self, tsCode )    获取指定股票代码的所有交易数据
def getAllStDateRange( self, datas )    获取曾用名期间的所有ST时间段

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import time
import datetime

from com.financial.statistics.count.st.StatisticsDao import StatisticsDao
from com.financial.statistics.count.st.FinancialDao import FinancialDao
from com.financial.common.util.CommonUtil import CommonUtil
from com.financial.statistics.count.st.StUtil import StUtil


class ST:
    
    '''
    @summary: 数据统计入口
    
    @param datas: st数据
    @param stType: st类型，带*或是不带* 
    '''
    def compute( self, datas, stType ):
#         stDatas = StUtil().deleteStarSt( datas )
        stDict = self.buildSTData( datas )
        
        dataResult = []
        
        for tsCode in stDict.keys():
            
            value = stDict.get( tsCode )
            
            stockName = self.getStockName( value )
            allStDateRange = self.getAllStDateRange( value )
            allCancleStDateRange = self.getAllCancleStDateRange( value )
            self.full( allStDateRange, allCancleStDateRange )
            stockDatas = self.getStockDatas( tsCode )
            code = self.getTsCodePrefix( tsCode )
            
            for index in range( len( allStDateRange ) ):
                stDateRange = allStDateRange[ index ]
                cancleStDateRange = allCancleStDateRange[ index ]
                
                if cancleStDateRange != None:
                    # 股票的涨跌幅数据
                    stMaxDown = self.getStMaxDown( stDateRange, stockDatas )
                    stMaxUp = self.getStMaxUp( stDateRange, stockDatas )
                    stDuration = self.getStDuration( stDateRange, stockDatas )
                      
                    cancelStMaxUp = self.getCancelStMaxUp( cancleStDateRange, stockDatas )
                    cancelStMaxDown = self.getCancelStMaxDown( cancleStDateRange, stockDatas )
                    isHistoryLowest = self.isHistoryLowest( stDateRange, stockDatas )
                     
                    stDate = self.buildPeriod( stDateRange )
                    cancleStDate= self.buildPeriod( cancleStDateRange )
                    stDaysDifference = self.daysDifference( stDateRange[ 0 ], stDateRange[ 1 ] )
                    stRiseExtent = self.countRiseExtent( stMaxDown[ 0 ], cancelStMaxUp[ 0 ] )
                    
                    # 深、沪指的涨跌幅数据
                    szIndexDatas = self.getIndexDatas( "SZ" )
                    szStMaxDown = self.getStMaxDown( stDateRange, szIndexDatas )
#                     szStMaxUp = self.getStMaxUp( stDateRange, szIndexDatas )
                    szCancelStMaxUp = self.getCancelStMaxUp( cancleStDateRange, szIndexDatas )
                    szRiseExtent = self.countRiseExtent( szStMaxDown[ 0 ], szCancelStMaxUp[ 0 ] )
                    
                    szIndexDownPre = self.getStIndexMaxDown( stDateRange, stockDatas, szIndexDatas)
                    szIndexUpPre = self.getStIndexMaxUp( stDateRange, stockDatas, szIndexDatas )
                    
                    shIndexDatas = self.getIndexDatas( "SH" )
                    shStMaxDown = self.getStMaxDown( stDateRange, shIndexDatas )
#                     shStMaxUp = self.getStMaxUp( stDateRange, shIndexDatas )
                    shCancelStMaxUp = self.getCancelStMaxUp( cancleStDateRange, shIndexDatas )
                    shRiseExtent = self.countRiseExtent( shStMaxDown[ 0 ], shCancelStMaxUp[ 0 ] )
                    
                    shIndexDownPre = self.getStIndexMaxDown( stDateRange, stockDatas, shIndexDatas )
                    shIndexUpPre = self.getStIndexMaxUp( stDateRange, stockDatas, shIndexDatas )
                    
                    maxDownDifference = self.getStMaxDownDifference( stMaxDown[ 2 ], szIndexDownPre, shIndexDownPre )
                    maxUpDifference = self.getStMaxUpDifference( stMaxUp[ 1 ], szIndexUpPre, shIndexUpPre )
                    upDifference = self.getStUpDifference( stRiseExtent, szRiseExtent, shRiseExtent )
                    
                    dataResult.append( [ code, stockName, stDate, stMaxDown[ 0 ], stMaxDown[ 1 ], stMaxDown[ 2 ], stMaxUp[ 0 ], stMaxUp[ 1 ], stDuration, 
                                        cancleStDate, cancelStMaxUp[ 0 ], cancelStMaxUp[ 1 ], cancelStMaxUp[ 2 ], cancelStMaxDown[ 0 ], cancelStMaxDown[ 1 ], isHistoryLowest,
                                        stRiseExtent, stDaysDifference, szIndexDownPre, shIndexDownPre, szIndexUpPre, shIndexUpPre, szRiseExtent, shRiseExtent,
                                        maxDownDifference, maxUpDifference, upDifference ] )

        stBeans = self.transformStatisticsBean( dataResult, stType )
        self.deleteOldStStatistics( stType )
        self.saveStStatistics( stBeans )
        
    
    '''
    @summary: 获取指定股票代码的所有交易数据
    
    @param tsCode: 股票代码
    
    @return: 指定股票代码的所有交易数据
    '''
    def getStockDatas( self, tsCode ):
        tsCodePrefix = CommonUtil().getStockCodePrefix( tsCode )
        SQL = StUtil().buildStockDataSQL( tsCodePrefix )
        
        return FinancialDao().getStockDatas( SQL, tsCode )
    
    
    '''
    @summary: 获取指定股票代码所在的交易所大盘数据
    
    @param tsCode: 股票代码
    
    @return: 股票代码所在的交易所大盘数据
    '''
    def getIndexDatas( self, stockCodeSuffix ):
#         tsCodeSuffix = CommonUtil().getStockCodeSuffix( stockCode )
        SQL = StUtil().buildIndexDataSQL( stockCodeSuffix )
        
        return FinancialDao().getIndexDatas( SQL )
        
    
    '''
    @summary: 获取曾用名期间的所有ST时间段
    
    @param datas: 一支股票的所有曾用名数据
    
    @return: 曾用名期间的所有ST时间段
    '''
    def getAllStDateRange( self, datas ):
        stDateRange = []

        dataLen = len( datas )
        start = 0   # 开始下标
        end = dataLen  # 结束下标
        
        while True:
            
            stStartDate = None
            stEndDate = None
            
            for index in range( start, end ):
                
                name = datas[ index ][ 1 ]  # 变化名字
                if name.find( "ST" ) > -1:
                    if stStartDate == None:
                        stStartDate = datas[ index ][2 ]
                        
                    stEndDate = datas[ index ][ 3 ]
                    if stEndDate == None:
                        stEndDate = CommonUtil().getCurrentDate()
                        
                else:
                    start = index + 1
                    break;
                    
            if stStartDate != None and  stEndDate != None:
                stDateRange.append( [ stStartDate, stEndDate ] )
              
            if index == ( dataLen - 1 ):
                break;
            
        return stDateRange
    
    
    '''
    @summary: 获取所有撤销ST时间段
    '''
    def getAllCancleStDateRange( self, datas ):
        cancleStDateRange = []

        dataLen = len( datas )
        start = 0   # 开始下标
        end = dataLen  # 结束下标
        
        # 先找出第一次St的下标，并加1，开始遍历。以免把最开始的时间当成撤销St的时间范围
        for index in range( start, end ):
            name = datas[ index ][ 1 ]  # 变化名字
            if name.find( "ST" ) > -1:
                start = index + 1
                break
                
        while True:
            
            cancleStStartDate = None
            cancleStEndDate = None
            
            for index in range( start, end ):
                
                name = datas[ index ][ 1 ]  # 变化名字
                if name.find( "ST" ) == -1:
                    if cancleStStartDate == None:
                        cancleStStartDate = datas[ index ][2 ]
                        
                    cancleStEndDate = datas[ index ][ 3 ]
                    if cancleStEndDate == None:
                        cancleStEndDate = CommonUtil().getCurrentDate()
                        
                else:
                    start = index + 1
                    break;
                    
            if cancleStStartDate != None and  cancleStEndDate != None:
                cancleStDateRange.append( [ cancleStStartDate, cancleStEndDate ] )
              
            if index == ( dataLen - 1 ):
                break;
            
        return cancleStDateRange
    
    
    '''
    @summary: 将ST数据列表转成 tsCode为key，相同tsCode数据放入列表并为value
    '''
    def buildSTData( self, noStarStDatas ):
        stDict = {}
       
        for row in noStarStDatas:
            tsCode = row[ 0 ]
            stDatas = stDict.get( tsCode )
            
            if stDatas == None:
                stDatas = []
                stDict.setdefault( tsCode, stDatas )
                
            stDatas.append( row )
            
        return stDict
    
    
    '''
    @summary: 如果ST和撤销ST数据长度不同，将少的撤销ST填充None
    '''
    def full( self, stDateRange, cancleStDateRange ):
        stLen = len( stDateRange )
        cancleStLen = len( cancleStDateRange )
        for index in range( cancleStLen, stLen ):
            cancleStDateRange.append( None )
            index
        
        
    '''
    @summary: 当一只股票变成st之后，从st之日起，最大跌幅是多少
                        备注:起始价按变成st前的一天的收盘价计算,最低价按st期间的最低价计算
    '''
    def getStMaxDown( self, stDateRange, datas ):
        
        stStartDate = stDateRange[ 0 ]
        stEndDate = stDateRange[ 1 ]
        
        lows = []   # 最低价列表
        preClose = None # 昨收价
        for data in datas:
            tradeDate = data[ 0 ]
    
            if tradeDate >= stStartDate  and tradeDate <= stEndDate:
                if preClose == None:
                    preClose = data[ 4 ]
                    
                lows.append( data[ 2 ] )
                
            if tradeDate >= stEndDate:
                break;
                
        lows.sort()
        stMinLow = lows[ 0 ]
     
        stMaxDownPercent = round( ( preClose - stMinLow ) / preClose * 100, 2 )
#         
        return [ preClose, stMinLow, stMaxDownPercent ]
#         return stMaxDownPercent

    '''
    @summary: 返回新算法的指数最大跌幅计算值
    '''
    def getStIndexMaxDown( self, stDateRange, stockDatas, indexDatas  ):
        
        stStartDate = stDateRange[ 0 ]
        stEndDate = stDateRange[ 1 ]
        
        preClose = None # 昨收价
        stLow = 1000.0  # st期间股票最低价
        stLowDate = None    # st期间股票最低价时间
        
        for data in stockDatas:
            tradeDate = data[ 0 ]
    
            if tradeDate >= stStartDate  and tradeDate <= stEndDate:
#                 if preClose == None:
#                     preClose = data[ 4 ]
#                     
                low = data[ 2 ]
                if low < stLow:
                    stLowDate = tradeDate
                    stLow = low
                    
            if tradeDate >= stEndDate:
                break;
            
        indexLow = 0.0  # 指数最低价
        for data in indexDatas:
            tradeDate = data[ 0 ]
    
            if tradeDate >= stStartDate  and tradeDate <= stEndDate:
            
                if preClose == None:
                        preClose = data[ 4 ]
                        
                if tradeDate == stLowDate:
                    indexLow = data[ 2 ]
                    break;
                
        indexDownPercent = round( ( preClose - indexLow ) / preClose * 100, 2 )
         
        return indexDownPercent
        
    
    '''
    @summary: 当一只股票变成st之后，从st之日起，跌到最低点后,最大长幅是多少
                        备注:最低点按st期间的最低价计算，最高点按最低价之后的取消st之前的最高价计算.
    '''
    def getStMaxUp( self, stDateRange, datas ):
        
        stStartDate = stDateRange[ 0 ]
        stEndDate = stDateRange[ 1 ]
        stStockDatas = []
        
        stMinLow = 100000.0
        minLowDate = None
        
        for stock in datas:
            tradeDate = stock[ 0 ]
            if tradeDate >= stStartDate  and tradeDate <= stEndDate:
                stStockDatas.append( stock )
                
                if stock[ 2 ] < stMinLow:
                    stMinLow = stock[ 2 ]
                    minLowDate = tradeDate
                
            if tradeDate >= stEndDate:
                break
        
        stMaxHigh = 0.01
        
        for stock in stStockDatas:
            tradeDate = stock[ 0 ]
            if tradeDate >= minLowDate  and tradeDate <= stEndDate and stock[ 1 ] > stMaxHigh:
                stMaxHigh = stock[ 1 ]
                
            if tradeDate >= stEndDate:
                break;
         
        stMaxUpPercent = round( ( stMaxHigh - stMinLow ) / stMinLow * 100, 2 )
         
        return [ stMaxHigh, stMaxUpPercent ]
#         return stMaxUpPercentdef getStMaxUp( self, stDateRange, datas ):
        
#         stStartDate = stDateRange[ 0 ]
#         stEndDate = stDateRange[ 1 ]
#         stStockDatas = []
#         
#         stMinLow = 100000.0
#         minLowDate = None
#         
#         for stock in datas:
#             tradeDate = stock[ 0 ]
#             if tradeDate >= stStartDate  and tradeDate <= stEndDate:
#                 stStockDatas.append( stock )
#                 
#                 if stock[ 2 ] < stMinLow:
#                     stMinLow = stock[ 2 ]
#                     minLowDate = tradeDate
#                 
#             if tradeDate >= stEndDate:
#                 break
#         
#         stMaxHigh = 0.01
#         
#         for stock in stStockDatas:
#             tradeDate = stock[ 0 ]
#             if tradeDate >= minLowDate  and tradeDate <= stEndDate and stock[ 1 ] > stMaxHigh:
#                 stMaxHigh = stock[ 1 ]
#                 
#             if tradeDate >= stEndDate:
#                 break;
#          
#         stMaxUpPercent = round( ( stMaxHigh - stMinLow ) / stMinLow * 100, 2 )
#          
#         return [ stMaxHigh, stMaxUpPercent ]
    
    
    '''
    @summary: 返回新算法的指数最大涨幅计算值
    '''
    def getStIndexMaxUp( self, stDateRange, stockDatas, indexDatas ):
        
        stStartDate = stDateRange[ 0 ]
        stEndDate = stDateRange[ 1 ]
        
        stMinLow = 100000.0
        stLowDate = None
        
        stMaxHigh = 0.01
        stHighDate = None
        
        for stock in stockDatas:
            tradeDate = stock[ 0 ]
            if tradeDate >= stStartDate  and tradeDate <= stEndDate:
                
                if stock[ 2 ] < stMinLow:
                    stMinLow = stock[ 2 ]
                    stLowDate = tradeDate
                    
                if stock[ 1 ] > stMaxHigh:
                    stMaxHigh = stock[ 1 ]
                    stHighDate = tradeDate
                
            if tradeDate >= stEndDate:
                break
        
        indexLow = 0.0
        indexHigh = 0.0
        for data in indexDatas:
            tradeDate = data[ 0 ]
            high = data[ 1 ]
            low = data[ 2 ]
            
            if tradeDate == stLowDate:
                indexLow = low
                
            if tradeDate == stHighDate:
                indexHigh = high
                
            if tradeDate >= stEndDate:
                break
                
            
        indexUpPercent = round( ( indexHigh - indexLow ) / indexLow * 100, 2 )
         
        return indexUpPercent
    
    
    '''
    @summary: 当一支股票变成ST后，从ST之日起，跌到最低点后，用的多长时间。
                        备注:最高点为ST第一天的开盘价，最低点为ST期间的最低价
    '''
    def getStDuration( self, stDateRange, datas ):
        stStartDate = stDateRange[ 0 ]
        stEndDate = stDateRange[ 1 ]
        stMinLow = 100000.0
        minLowDate = None
        
        for stock in datas:
            tradeDate = stock[ 0 ]
            if tradeDate >= stStartDate  and tradeDate <= stEndDate and stock[ 2 ] < stMinLow:
                stMinLow = stock[ 2 ]
                minLowDate = stock[ 0 ]
                
            if tradeDate >= stEndDate:
                break
                
        stDuration = self.daysDifference( stStartDate, minLowDate )
         
#         return [ stStartDate, minLowDate, stDuration ]
        return stDuration
        
        
    '''
    @summary: 去掉st之后，平均最大长幅是多少
                        备注:起始价按去掉st之前一天的收盘价计算,最高价按取消st之后的历史最高价计算
    '''
    def getCancelStMaxUp( self, cancleStDateRange, datas ):
        if cancleStDateRange == None:
            return [ None, None, None ]
#             return None
        else:
            cancleStStartDate = cancleStDateRange[ 0 ]
            cancleStEndDate = cancleStDateRange[ 1 ]
            
            stLastClose = None
            cancleStHigh = 0.01
            
            for stock in datas:
                tradeDate = stock[ 0 ]
                    
                if tradeDate >= cancleStStartDate and tradeDate <= cancleStEndDate and stock[ 1 ] > cancleStHigh:
                    if stLastClose == None:
                        stLastClose = stock[ 4 ]
                        
                    cancleStHigh = stock[ 1 ]
                    
                if tradeDate >= cancleStEndDate:
                    break
                    
            cancelStMaxUpPercent = round( ( cancleStHigh - stLastClose ) / stLastClose * 100, 2 )
            
            return [ stLastClose, cancleStHigh, cancelStMaxUpPercent ]
#             return cancelStMaxUpPercent
        
    '''
    @summary: 去掉st之后，平均最大跌幅是多少
                        备注:起始价按去掉st之前一天的收盘价计算,最低价按取消st之后的历史最低价计算
    '''
    def getCancelStMaxDown( self, cancleStDateRange, datas ):
        if cancleStDateRange == None:
            return [ None, None ]
#             return None
        else:
            cancleStStartDate = cancleStDateRange[ 0 ]
            cancleStEndDate = cancleStDateRange[ 1 ]
            
            stLastClose = None
            cancleStLow = 100000.0
            
            for stock in datas:
                tradeDate = stock[ 0 ]
                
                if tradeDate >= cancleStStartDate and tradeDate <= cancleStEndDate and stock[ 2 ] < cancleStLow:
                    if stLastClose == None:
                        stLastClose = stock[ 4 ]
                        
                    cancleStLow = stock[ 2 ]
                    
                if tradeDate >= cancleStEndDate:
                    break;
            
            cancelStMaxDownPercent = round( ( cancleStLow - stLastClose ) / stLastClose * 100, 2 )
            
        return [ cancleStLow, cancelStMaxDownPercent ]
#         return cancelStMaxDownPercent
                    
    
    '''
    @summary: 当一只股票变成st之后，从st之日起，到摘掉st之前的最低价,是否为该股历史的最低价
    '''
    def isHistoryLowest( self, stDateRange, datas ):
        stStartDate = stDateRange[ 0 ]
        stEndDate = stDateRange[ 1 ]
        
        stLow = 100000.0
        sortedByLowAsc = sorted( datas, key=lambda stock : stock[ 2 ] )
        historyLow = sortedByLowAsc[ 0 ][ 2 ]
        
        for stock in datas:
            tradeDate = stock[ 0 ]
            low = stock[ 2 ]
                    
            if tradeDate >= stStartDate and tradeDate <= stEndDate and low < stLow:
                stLow = low
            
            if tradeDate >= stEndDate:
                break
        
        isHistoryLowest = ( stLow < historyLow )
        
#         return [ stMinLow, historyMinLow, isHistoryLowest ]
        return isHistoryLowest
    
    
    '''
    @summary: 计算涨幅，公式：（收盘价-起始价 ） / 收盘价 * 100
    
    @param preClose: ST前一天收盘价
    @param stLastClose: 撤销ST之前的收盘价
    
    @return: 涨幅
    '''
    def countRiseExtent( self, preClose, stLastClose ):
        if stLastClose == None:
            return None
        else:
            return round( ( stLastClose - preClose ) / preClose * 100, 2 )
    
    '''
    @summary: 获取股票名
    '''
    def getStockName( self, nameChanges ):
        length = len( nameChanges )
        lastIndex = length - 1
        
        return nameChanges[ lastIndex ][ 1 ]
    
    
    '''
    @summary: 获取股票代码的前6位
        
    @return: 股票代码的前6位
    '''
    def getTsCodePrefix( self, tsCode ):
        return tsCode[ 0:6 ]
        
        
#     '''
#     @summary: 股票退市的比例
#     '''
#     def __quitProportion( self, quitCount ):
#         str = ""
        
    
    '''
    @summary: 将数据转换成数据库
    '''
    def transformStatisticsBean( self, datas, stType ):
        return  StUtil().transformStatisticsBean( datas, stType )
    
    
    '''
    @summary: 保存st统计结果
    '''
    def saveStStatistics( self, stDatas ):
        StatisticsDao().saveStDatas( stDatas )
        
        
    '''
    @summary: 删除之前旧的统计结果
    '''
    def deleteOldStStatistics( self, stType ):
        StatisticsDao().deleteOldStStatistics( stType )
        
        
#     '''
#     @summary: 测试用方法
#     '''
#     def getNameChanges( self ):
#         return StDao().getAllNameChangeDatas()
   
   
    '''
    @summary: 计算两个时间的差数天
    '''
    def daysDifference( self, startDateStr, endDateStr ):
        startTime = time.strptime( startDateStr, "%Y%m%d" )
        endTime = time.strptime( endDateStr, "%Y%m%d" )
            
        startDate = datetime.datetime( startTime[ 0 ], startTime[ 1 ], startTime[ 2 ] )
        endDate = datetime.datetime( endTime[ 0 ], endTime[ 1 ], endTime[ 2 ] )
        res = endDate - startDate
            
        return res.days
    
    
    '''
    @summary: 生成时间段字符串
    
    @param dateRange: 包含开始时间、结束时间的列表
    
    @return: 开始时间 - 结束时间 格式的字符串
    '''
    def buildPeriod( self, dateRange ):
        if dateRange != None:
            return dateRange[ 0 ] + "-" + dateRange[ 1 ]
        else:
            return None
        
    
    '''
    @summary: 计算最大跌幅的差值。计算公式：st期间的最大跌幅 - (  st期间深指最大跌幅 + st期间上指最大跌幅 ) / 2
    
    @param maxDown: st期间的最大跌幅
    @param szMaxDown: st期间深指最大跌幅
    @param shMaxDown: st期间上指最大跌幅
    
    @return: 最大跌幅的差值
    '''  
    def getStMaxDownDifference( self, stMaxDown, szMaxDown, shMaxDown ):
        return round( stMaxDown - ( szMaxDown + shMaxDown ) / 2, 2 )
    
    
    '''
    @summary: 计算最大涨幅的差值。计算公式：st期间的最大涨幅 - (  st期间深指最大涨幅 + st期间上指最大涨幅 ) / 2
    
    @param maxUp: st期间的最大涨幅
    @param szMaxUp: st期间深指最大涨幅
    @param shMaxUp: st期间上指最大涨幅
    
    @return: 最大涨幅的差值
    '''  
    def getStMaxUpDifference( self, stMaxUp, szMaxUp, shMaxUp ):
        return round( stMaxUp - ( szMaxUp + shMaxUp ) / 2, 2 )
    
    
    '''
    @summary: 计算涨幅的差值。计算公式：st期间的涨幅 - (  st期间深指涨幅 + st期间上指涨幅 ) / 2
    
    @param stUp: st期间的涨幅
    @param szUp: st期间深指涨幅
    @param shUp: st期间上指涨幅
    
    @return: 最大涨幅的差值
    '''  
    def getStUpDifference( self, stUp, szUp, shUp ):
        return round( stUp - ( szUp + shUp ) / 2, 2 )