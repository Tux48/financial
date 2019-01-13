#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-8

com.financial.kline.sm.KLineState000 -- shortdesc

com.financial.kline.sm.KLineState000 is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.kline.bean.KLine000Bean import KLine603Bean
from com.financial.kline.sm.KLineStateBase import KLineStateBase

class KLineState603( KLineStateBase ):
    
    __SQL = "select max(trade_date) from k_line_603 where ts_code=:tsCode"
    
    '''
    
    '''
    def match(self, stockBasicBean):
        stockCode = stockBasicBean.tsCode
        stockCodePrefix = stockCode[ 0:3 ]
        if "603" == stockCodePrefix:
            startDate = stockBasicBean.listDate ## 默认的K线数据获取开始时间为股票上市时间
            endDate = self.getCurrentDate() ## K线数据获取结束时间为当前时间
            
            '''
            获取该股票K线数据的最大交易时间，如果不为None，
            将开始时间设置为最大交易时间加一天
            '''
            lastDate = self.__getLastKLineDate( self.__SQL, stockCode )
            if lastDate != None:
                startDate  =self.__getNextDayStr( lastDate )
                
            '''
            获取数据、构建数据bean、保存数据
            '''
            kLineDatasFormat = self.__getKLineDatas( stockCode, startDate, endDate )
            kLineDatas = self.__buildKLineDataBeans( kLineDatasFormat )
            self.__saveKLineData( kLineDatas )
    
    '''
    
    '''
    def __buildKLineDataBeans( self , dataFormat ):
        
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            index   ## 这行代码没意义，为了去除警告而写。强迫症，不想看到有警告。
            kLineBean = KLine603Bean()
            kLineBean.tsCode = row[ "ts_code" ]
            kLineBean.tsDate = row[ "trade_date" ]
            kLineBean.open = row[ "open" ]
            kLineBean.high = row[ "high" ]
            kLineBean.low = row[ "low" ]
            kLineBean.close = row[ "close" ]
            kLineBean.preClose = row[ "pre_close" ]
            kLineBean.change = row[ "change" ]
            kLineBean.pctChg = row[ "pct_chg" ]
            kLineBean.vol = row[ "vol" ]
            kLineBean.amount = row[ "amount" ]
            
            kLineDatas.insert( kLineBean )
            
        return kLineDatas