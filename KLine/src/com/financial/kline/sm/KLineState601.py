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

from com.financial.kline.bean.KLine000Bean import KLine601Bean
from com.financial.kline.sm.KLineStateBase import KLineStateBase

class KLineState601( KLineStateBase ):
    
    __SQL = "select max(trade_date) from k_line_601 where ts_code=:tsCode"
    
    '''
    
    '''
    def match(self, stockBasicBean):
        stockCodePrefix = stockBasicBean.tsCode[ 0:3 ]
        if "601" == stockCodePrefix:
            str = ""
    
    '''
    
    '''
    def buildKLineDataBeans( self , dataFormat ):
        
        kLineDatas = []
        for index, row in dataFormat.iterrows():
            index   ## 这行代码没意义，为了去除警告而写。强迫症，不想看到有警告。
            kLineBean = KLine601Bean()
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