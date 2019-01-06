#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-4

com.financial.stockbasic.task.StockBasicTask -- shortdesc

com.financial.stockbasic.task.StockBasicTask is a description

It defines classes_and_methods
def loadingStockBasicData( self )    加载股票基本数据
def __dataCompared( self , newDataDict )    股票基本数据对比，去除重复的，只保留新的股票基本数据
def __saveData( self , dataList )    保存新的股票基本数据数据库

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.stockbasic.log.StockBasicLog import StockBasicLog
from com.financial.stockbasic.dao.StockBasicDao import StockBasicDao
from com.financial.stockbasic.api.StockBasicAPI import StockBasicAPI

class StockBasicTask:
    
    '''
    @summary: 加载股票基本数据。
    '''
    def loadingStockBasicData( self ):
        
        try:
            StockBasicLog().getLog().info( "加载任务开始" )
            newDataDict = StockBasicAPI().getStockBasicData()
            dataList = self.__dataCompared( newDataDict )
            self.__saveData( dataList )
            StockBasicLog().getLog().info( "加载任务结束" )
        except Exception as ex:
            StockBasicLog().getLog().error( ex )
    
    '''
    @summary: 股票基本数据对比，去除重复的，只保留新的股票基本数据。
    
    @param newDataDict: 新加载到的股票基本数据
    '''  
    def __dataCompared( self , newDataDict ):
        StockBasicLog().getLog().info( "数据处理开始" )
        oldDataDict = StockBasicDao().getStockBasicDict()

        for key in oldDataDict.keys():
            newDataDict.pop( key )
        
        oldDataDict.update( newDataDict )
        StockBasicLog().getLog().info( "数据处理结束" )
        
        return newDataDict.values();
    
    '''
    @summary: 保存新的股票基本数据数据库。
    
    @param newDataDict: 新上市的股票基本数据
    '''  
    def __saveData( self , dataList ):
        StockBasicDao().saveStockBasicData( dataList )