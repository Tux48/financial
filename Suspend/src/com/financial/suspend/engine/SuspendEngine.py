#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.suspend.engine.SuspendEngine -- shortdesc

com.financial.suspend.engine.SuspendEngine is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import time
import datetime

from com.financial.suspend.util.BuildSuspendBeanUtil import BuildSuspendBeanUtil

from com.financial.suspend.api.SuspendAPI import SuspendAPI
from com.financial.suspend.dao.SuspendDao import SuspendDao
from com.financial.suspend.log.SuspendLog import SuspendLog

class SuspendEngine:
    
    ## 存放股票基本数据的字典
    __stockBasicDatas = None
    
    
    def start( self ):
        self.__getStockBasicDict()
        for stockData in self.__stockBasicDatas.values():
            try:
                self.__suspendDataProcess( stockData )
            except Exception:
                SuspendLog.getLog(self).error( "{} 股票出现错误".format( stockData.tsCode ) )
    
    '''
    
    '''    
    def __suspendDataProcess( self, stockBasicBean ):
        stockCode = stockBasicBean.tsCode
        currentDate = self.__getCurrentDate()
        suspendDatasFormat = self.__getSuspendDatas( stockCode, currentDate )
        suspendDatas = BuildSuspendBeanUtil().buildSuspendBean( suspendDatasFormat )
        self.__saveSuspendData( suspendDatas )
            
        time.sleep( 1 )
    
        
    '''
    @summary: 获取股票基本信息
    
    @return: 所有股票基本信息列表
    '''       
    def __getStockBasicDict( self ):
        self.__stockBasicDatas = SuspendDao().getStockBasicDict()
        
        
    '''
    返回yyyymmdd的时间格式的字符串
    
    @return: yyyymmdd的时间格式的字符串
    '''
    def __getCurrentDate( self ):
        return datetime.datetime.now().strftime( "%Y%m%d" )
        
    
    '''
    @summary:  获取指定时间段内股票的停复牌信息数据
    
    @param stockCode: 股票代码
    @param suspendDate: 当天时间
    
    @return:  指定时间段内股票的停复牌信息数据
    '''
    def __getSuspendDatas( self, stockCode, suspendDate ):
        return SuspendAPI().getSuspendDatas( stockCode, suspendDate )
    
    
    '''
     @summary: 保存停复牌信息数据
     
     @param kLineDatas: 停复牌信息数据集合   
    '''
    def __saveSuspendData( self , suspendDatas ):
        SuspendDao().saveSuspendDatas( suspendDatas )