#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.nc.engine.NameChangeEngine -- 加载所有股票曾用名数据

com.financial.nc.engine.NameChangeEngine is a 加载所有股票曾用名数据，只保留带有st的股票数据

It defines classes_and_methods
def load( self ):    加载股票曾用名数据数据
def __getNameChangeDatas( self, tsCode ):    指定股票代码曾用名数据
def __sortByStartDateAsc( self, nameChangeDatas ):    按开始时间升序排序

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import time
import numpy as np

from com.financial.common.api.TushareAPI import TushareAPI

from com.financial.statistics.log.StatisticsLog import StatisticsLog
from com.financial.statistics.count.st.FinancialDao import FinancialDao

class NameChangeLoad:
    
    # 不保留的股票代码列表
    __NO_LOAD_TSCODE = [ "601975.SH", "000728.SZ", "000783.SZ", "600539.SH" ]
    
         
    '''
    @summary: 获取股票曾用名数据，加载过程中，只保留st相关数据，且当股票代码不在不加载列表中，则保留。
    '''
    def load( self ):
            
        dataResult = []
        tsCodes = FinancialDao().getTsCodes()
        tsCodes = [ "002194.SZ" ]
        for tsCode in tsCodes:
            if self.__NO_LOAD_TSCODE.count( tsCode ) == 0:
                
                StatisticsLog().getLog().info( "加载 {} 曾用名数据".format( tsCode ) )
                nameChangeDatas = self.__getNameChangeDatas( tsCode )
                for row in nameChangeDatas:
                        
                    name = row[ 1 ]
                    if name.find( "ST" ) > -1:
                        dataResult.extend( self.__sortByStartDateAsc( nameChangeDatas ) )
                        print( dataResult )
                        break
                        
                time.sleep( 2 )
                    
        return dataResult
        
    
    '''
    @summary: 获取股票曾用名数据
    
    @param tsCode: 股票代码
    
    @return: 指定股票代码曾用名数据
    '''
    def __getNameChangeDatas( self, tsCode ):
        tsPro = TushareAPI().getTushareAPI()
        data = tsPro.namechange( ts_code= tsCode )

        return np.array( data ).tolist()
    
    
    '''
      @summary: 按开始时间升序排序
      
      @param nameChangeDatas: 股票曾用名数据
      
      @return: 排序后的数据
    '''
    def __sortByStartDateAsc( self, nameChangeDatas ):
        return sorted( nameChangeDatas, key=lambda data:data[ 2 ] )
        