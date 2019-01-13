#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-8

com.financial.kline.sm.KLineStateBase -- shortdesc

com.financial.kline.sm.KLineStateBase is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import datetime

from com.financial.kline.api.KLineAPI import KLineAPI
from com.financial.kline.dao.KLineDao import KLineDao

class KLineStateBase:
    
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
    
    '''
    def __getLastKLineDate( self, SQL, stockCode ):
        return KLineDao().getLastKLineDate(SQL, stockCode)
    
    '''
    
    '''
    def __getKLineDatas( self, stockCode, startDate, endDate ):
        return KLineAPI().getKLineDatas( stockCode, startDate, endDate )
   
    '''
        
    '''
    def __buildKLineDataBeans( self , dataFormat ):
        pass
        
    '''
        
    '''
    def __saveKLineData( self , kLineDatas ):
        KLineDao().saveKLineDatas( kLineDatas )
    
    '''
   
    '''
    def match( self, stockBasicBean ):
        pass