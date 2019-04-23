#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年4月11日

com.financial.algorithm.B_001 -- 第一个买入算法

com.financial.algorithm.B_001 is a 
2019-04-09提出的第一个买入算法，参考doc目录下的 "买入算法一.docx"

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
import numpy as np
import pandas as pd

from com.financial.algorithm.dao.AlgorithmDao import AlgorithmDao
from com.financial.algorithm.util.BuildSQLUtil import BuildSQLUtil

from com.financial.graphics.GraphicsForKLine import GraphicsForKLine

class B_001:
    
    '''
    '''
    def compute( self, stockCode ):
        stockCodePrefix = self.__getStockCodePrefix( stockCode )
        SQL = self.__genSQLByStockCode( stockCodePrefix )
        stockDatas = self.__getStockDatas( SQL, stockCode )
        stockDataFrame = self.__transformToDataFrame( stockDatas )
        
        kLineXAxis = self.__getKLineXAxis( stockDataFrame )
        kLineYAxis = self.__getKLineYAxis( stockDataFrame )
        ( allDownPoint, buyPoints ) = self.__algorithmStep1( stockDataFrame )  # 连续跌的点
#         downPoints = self.__getDownPoints( allDataBlock )
#         buyPoints = self.__algorithmStep2( allDataBlock )   # 可以买的点
        
        graphicsForKLine = GraphicsForKLine( stockCode )
        graphicsForKLine.addKLine( kLineXAxis, kLineYAxis )  # 画K线
        graphicsForKLine.addDownPoints( allDownPoint ) # 画连跌点
        graphicsForKLine.addBuyPoints( buyPoints )   # 画可以买入点
        graphicsForKLine.draw()

    
    '''
    @summary: 算法第一步  第一个条件  
                        连续出现九根日K线，并且这些日K线的收盘价都比各自前面的第四根日K线的收盘价低,在其日K线下方标记相应的数字第1根标注1，
                        第2根标注2，依次类推。如果某一根的日K线的收盘价不小于前面第四根的日K线的收盘价，则原计数清零,需重新开始计算。
    
    @param stockDataFrame: DataFrame格式的股票数据
    '''
    def __algorithmStep1( self, stockDataFrame ):
        
        startIndex = 0
        length = len( stockDataFrame )
        
        allDownPoint = []   # 存放所有符合第一步计算条件的数据块
        allBuyPoint = []    # 所可以买入的点
        dataBlock = []  # 某一单独数据块
        
        for endIndex in range( 4, length ):
            startPoint = stockDataFrame.iloc[ startIndex ]  # 比较的开始点
            endPoint = stockDataFrame.iloc[ endIndex ]    # 比较的结束点
            
            startPointClose = startPoint[ "close" ] # 开始点收盘价
            endPointClose = endPoint[ "close" ] # 结束点收盘价
            
            ## 日K线的收盘价都比各自前面的第四根日K线的收盘价低
            if endPointClose < startPointClose:
                
                tradeDate = self.__transformDate( endPoint[ "trade_date" ] )
                open1 = endPoint[ "open" ]  # 不知为啥，open会有警告，所以改成open1
                high = endPoint[ "high" ]
                low = endPoint[ "low" ]
                close = endPoint[ "close" ]
                
                dataBlock.append( [ tradeDate, open1, close, low, high ] )
            else:
                dataBlock.clear()
                
            dataBlockLen = len( dataBlock )
            if dataBlockLen >= 9:
#                   allDataBlock.append( dataBlock.copy() )
                ( downDataBlock, buyPoint ) = self.__algorithmStep2( dataBlock.copy() )
                buyPointLen = len( buyPoint )
                    
                if buyPointLen > 0:
                    allDownPoint.extend( downDataBlock )
                    allBuyPoint.extend( buyPoint )
                    
                dataBlock.clear()
                                
            startIndex += 1
            
        return ( allDownPoint, allBuyPoint )
    
    
    '''
    @summary: 算法第二步
    
    @param allDataBlock: 算法第一步的计算结果
    '''
    def __algorithmStep2( self, dataBlock ):
                    
        dataBlockTuple = tuple( dataBlock ) # 将列表转换为元组。便于下标取值
        dataBlock0_9 = dataBlockTuple[ 0 : 9 ]
        
        ## 取出第6、7、8、9节点数据。第9对比7，8对比6
        data6 = dataBlock0_9[ 5 ]
        data7 = dataBlock0_9[ 6 ]
        data8 = dataBlock0_9[ 7 ]
        data9 = dataBlock0_9[ 8 ]
        
        # 取出各结点的最低价
        dataLow6 = data6[ 3 ]
        dataLow7 = data7[ 3 ]
        dataLow8 = data8[ 3 ]
        dataLow9 = data9[ 3 ]
        
        buyPoint = []
        
        if dataLow9 < dataLow7:
            tradeDate = data9[ 0 ]
            buyPoint.append( [ tradeDate, dataLow9 ] )
            
        if dataLow8 < dataLow6:
            tradeDate = data8[ 0 ]
            buyPoint.append( [ tradeDate, dataLow8 ] )

        return ( list( dataBlock0_9 ), buyPoint )

    
#     '''
#     @summary: 算法第二步
#     
#     @param allDataBlock: 算法第一步的计算结果
#     '''
#     def __algorithmStep2( self, allDataBlock ):
#         
# #         buyPoint = []
# #         
# #         for dataBlock in allDataBlock:
# #             
# #             dataBlockTuple = tuple( dataBlock ) # 将列表转换为元组。便于下标取值
# #             blockLen = len( dataBlockTuple )
# #             
# #             ## 第8个点与第6个点比较，9个点与第7个点进行比较，依次类推
# #             for endIndex in range( 7, blockLen ):
# #                 startIndex = endIndex - 2
# #                 
# #                 startData = dataBlockTuple[ startIndex ]
# #                 endData = dataBlockTuple[ endIndex ]
# #                 
# #                 startLow = startData[ 2 ]
# #                 endLow = endData[ 2 ]
# #                 if endLow < startLow:
# #                     tradeDate = endData[ 0 ]
# #                     buyPoint.append( [ tradeDate, endLow ] )
#                     
#         buyPoint = []
#         buyPointTemp = []
#         allDataBlockTemp = allDataBlock.copy()
# 
#         for dataBlock in allDataBlockTemp:
#             
#             dataBlockTuple = tuple( dataBlock ) # 将列表转换为元组。便于下标取值
#             blockLen = len( dataBlockTuple )
#             
#             ## 第8个点与第6个点比较，9个点与第7个点进行比较，依次类推
#             for endIndex in range( 7, blockLen ):
#                 startIndex = endIndex - 2
#                 
#                 startData = dataBlockTuple[ startIndex ]
#                 endData = dataBlockTuple[ endIndex ]
#                 
#                 startLow = startData[ 2 ]
#                 endLow = endData[ 2 ]
#                 if endLow < startLow:
#                     tradeDate = endData[ 0 ]
#                     buyPointTemp.append( [ tradeDate, endLow ] )
#                     
#             # 删除没有买点的连跌数据
#             if len( buyPointTemp ) > 0:
#                 buyPoint.extend( buyPointTemp.copy() )
#                 buyPointTemp.clear()
#             else:
#                 allDataBlock.remove( dataBlock )
#         
#         return buyPoint
    
    
    '''
    @summary: 获取连续跌的点的X和Y轴数据
    
    @param allDataBlock: 连续跌的点的数据
    '''
    def __getDownPoints( self, allDataBlock ):
        
        downPoints = []
        
        for dataBlock in allDataBlock:
            for data in dataBlock:
                downPoints.append( [ data[ 0 ], data[ 1 ] ] )
            
        return downPoints
        
    '''
    @summary: 计算图形X轴数据（交易时间为X轴）
    
    @param stockDataFrame: DataFrame格式的股票数据
    '''
    def __getKLineXAxis(self, stockDataFrame ):

        xAxis = []
        index = 0
        
        for data in np.array( stockDataFrame[ [ "trade_date" ] ] ):
            tradeDate = data[ 0 ]
            xAxis.insert( index, "{}/{}/{}".format( tradeDate[0:4], tradeDate[4:6], tradeDate[6:8] ) )
            index += 1
            
        return xAxis
    
    
    '''
    @summary: 计算图形Y轴数据
    
    @param stockDataFrame: DataFrame格式的股票数据
    '''
    def __getKLineYAxis(self, stockDataFrame ):
        return  np.array( stockDataFrame[ [ "open", "close", "low", "high" ] ] )
    
    
    '''
    @summary: 将list转换为DataFrame
    
    @param stockDatas: list格式的股票数据
    '''
    def __transformToDataFrame( self, stockDatas ):
        return pd.DataFrame( stockDatas, columns = [ "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount" ] )
    
    
    '''
    @summary: 将yyyymmdd时间格式转换为yyyy/mm/dd
    
    @param tradeDate: yyyymmdd时间格式
    '''
    def __transformDate( self, tradeDate ):
        return "{}/{}/{}".format( tradeDate[0:4], tradeDate[4:6], tradeDate[6:8] ) 
        
        
    '''
    @summary: 根据SQL和股票代码获取相关数据
    
    @param SQL: 执行SQL
    @param stockCode: 股票代码
    '''
    def __getStockDatas( self, SQL, stockCode ):
        return AlgorithmDao().getAlgorithmDate( SQL, stockCode )
    
        
    '''
    @summary: 根据股票代码前缀，生成相应的SQL
    
    @param stockCodePrefix: 股票代码前缀
    '''    
    def __genSQLByStockCode( self, stockCodePrefix ):
        SQL = BuildSQLUtil().buildKLineSQL( stockCodePrefix )
        
        return SQL
    
        
    '''
    @summary: 获取股票代码的前3位
    
    @return: 股票代码的前3位
    '''
    def __getStockCodePrefix( self, stockCode ):
        return stockCode[ 0:3 ]