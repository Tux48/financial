#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.nc.util.BuildNameChangeBeanUtil -- 构建要保存到数据库的K线bean的工具类

com.financial.nc.util.BuildNameChangeBeanUtil is a 
一个单例类，根据不同的条件构建相应要保存到数据库的K线bean

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
import threading

from com.financial.statistics.count.st.StType import STAR_ST_TYPE
from com.financial.statistics.count.st.StBean import StBean

class StUtil:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( StUtil, "_instance" ):
            with StUtil.__instance_lock:
                if not hasattr( StUtil, "_instance" ):
                    StUtil._instance = object.__new__( cls )
                    
        return StUtil._instance
    
    def __init__( self  ):
        pass
    
    
    '''
    @summary: 根据不同的股票代码前缀构建并返回相应的保存到数据库bean的集合。
    
    @param stockCodePrefix: 股票代码前缀
    @param dataFormat: 格式化后的K线数据
    
    @return: 保存到数据库bean的集合
    '''
    def transformStatisticsBean( self, datas, stType ):
       
        stBeans = []
        for row in datas:
            stBean = StBean()

            stBean.tsCode = row[ 0 ]
            stBean.name = row[ 1 ]
            stBean.stDate = row[ 2 ]
            stBean.preClose = row[ 3 ]
            stBean.stMinLow = row[ 4 ]
            stBean.stMaxDown = row[ 5 ]
            stBean.stMaxHigh = row[ 6 ]
            stBean.stMaxUp = row[ 7 ]
            stBean.stDuration = row[ 8 ]
            stBean.cancleStDate = row[ 9 ]
            stBean.stLastClose = row[ 10 ]
            stBean.cancleStHigh = row[ 11 ]
            stBean.cancleStMaxUp = row[ 12 ]
            stBean.cancleStLow = row[ 13 ]
            stBean.cancleStMaxDown = row[ 14 ]
             
            if row[ 15 ] == True:
                stBean.isHisLow = "是" 
            else:
                stBean.isHisLow = "否"
                
            stBean.stType = stType
            stBean.stUp = row[ 16 ]
            stBean.stDays = row[ 17 ]
            stBean.szMaxDown = row[ 18 ]
            stBean.shMaxDown = row[ 19 ]
            stBean.szMaxUp = row[ 20 ]
            stBean.shMaxUp = row[ 21 ]
            stBean.szUp = row[ 22 ]
            stBean.shUp = row[ 23 ]
            stBean.maxDownDifference = row[ 24 ]
            stBean.maxUpDifference = row[ 25 ]
            stBean.upDifference = row[ 26 ]
            
            stBeans.append( stBean )
            
        return stBeans
    
    
    '''
    @summary: 根据不同的股票代码前缀返回相应的SQL语句。
    
    @param tsCodePrefix: 股票代码前缀
    
    @return: 查询SQL
    '''
    def buildStockDataSQL( self, tsCodePrefix ):
       
        if tsCodePrefix == "000":
            return "select trade_date, high, low, close, pre_close from k_line_day_000 where ts_code=:tsCode order by trade_date asc"
        elif tsCodePrefix == "001":
            return "select trade_date, high, low, close, pre_close from k_line_day_001 where ts_code=:tsCode order by trade_date asc"
        elif tsCodePrefix == "002":
            return "select trade_date, high, low, close, pre_close from k_line_day_002 where ts_code=:tsCode order by trade_date asc"
        elif tsCodePrefix == "300":
            return "select trade_date, high, low, close, pre_close from k_line_day_300 where ts_code=:tsCode order by trade_date asc"
        elif tsCodePrefix == "600":
            return "select trade_date, high, low, close, pre_close from k_line_day_600 where ts_code=:tsCode order by trade_date asc"
        elif tsCodePrefix == "601":
            return "select trade_date, high, low, close, pre_close from k_line_day_601 where ts_code=:tsCode order by trade_date asc"
        elif tsCodePrefix == "603":
            return "select trade_date, high, low, close, pre_close from k_line_day_603 where ts_code=:tsCode order by trade_date asc"
        else:
            return None
        
        
    '''
    @summary: 根据不同的股票代码后缀返回相应的SQL语句。
    
    @param tsCodePrefix: 股票代码前缀
    
    @return: 查询SQL
    '''
    def buildIndexDataSQL( self, tsCodeSuffix ):
       
        if tsCodeSuffix == "SH":
            return "select trade_date, high, low, close, pre_close from index_line_day_sse where ts_code='000001.SH' order by trade_date asc"
        elif tsCodeSuffix == "SZ":
            return "select trade_date, high, low, close, pre_close from index_line_day_szse where ts_code='399001.SZ' order by trade_date asc"
        else:
            return None
        
        
    '''
    @summary: 构建st统计数据查询SQL
    '''
    def buildStStatisticsSQL(self, stType ):
        SQL = "select ts_code, name, st_date, pre_close, st_min_low, st_max_down, st_max_high, st_max_up, st_duration, cancle_st_date, st_last_close, cancle_st_high, cancle_st_max_up, cancle_st_low, cancle_st_max_down, is_his_low, st_up, st_days, sz_max_down, sh_max_down, sz_max_up, sh_max_up, sz_up, sh_up, max_down_diff, max_up_diff, up_diff from st_statistics where cancle_st_date is not null and st_type=0"
        if stType == STAR_ST_TYPE:
            SQL = "select ts_code, name, st_date, pre_close, st_min_low, st_max_down, st_max_high, st_max_up, st_duration, cancle_st_date, st_last_close, cancle_st_high, cancle_st_max_up, cancle_st_low, cancle_st_max_down, is_his_low, st_up, st_days, sz_max_down, sh_max_down, sz_max_up, sh_max_up, sz_up, sh_up, max_down_diff, max_up_diff, up_diff from st_statistics where cancle_st_date is not null and st_type=1"
            
        return SQL
    
    
    '''
    @summary: 计算最大跌幅、 深最大跌、上最大跌、差值、最大涨幅、深最大涨、上最大涨、差值、涨幅、深涨、上涨、差值的平均值
    
    @param datas: 数据集合
    
    @return: 计算结果 
    '''
    def getAverage( self, stDatas ):
        
        stMaxDownSum = 0.0
        szMaxDownSum = 0.0
        shMaxDownSum = 0.0
        maxDownDiffSum = 0.0
        
        stMaxUpSum = 0.0
        szMaxUpSum = 0.0
        shMaxUpSum = 0.0
        maxUpDiffSum = 0.0
        
        stUpSum = 0.0
        szUpSum = 0.0
        shUpSum = 0.0
        upDiffSum = 0.0

        for data in stDatas:
            stMaxDownSum +=data[ 5 ]
            szMaxDownSum += data[ 18 ]
            shMaxDownSum += data[ 19 ]
            maxDownDiffSum += data[ 24 ]
            
            stMaxUpSum += data[ 7 ]
            szMaxUpSum += data[ 20 ]
            shMaxUpSum += data[ 21 ]
            maxUpDiffSum += data[ 25 ]
            
            stUpSum += data[ 16 ]
            szUpSum += data[ 22 ]
            shUpSum += data[ 23 ]
            upDiffSum += data[ 26 ]
            
        count = len( stDatas )
        stMaxDownAvg = round( stMaxDownSum / count, 2 )
        szMaxDownAvg = round( szMaxDownSum / count, 2 )
        shMaxDownAvg = round( shMaxDownSum / count, 2 )
        maxDownDiffAvg = round( maxDownDiffSum / count, 2 )
        
        stMaxUpAvg = round( stMaxUpSum / count, 2 )
        szMaxUpAvg = round( szMaxUpSum / count, 2 )
        shMaxUpAvg = round( shMaxUpSum / count, 2 )
        maxUpDiffAvg = round( maxUpDiffSum / count, 2 )
        
        stUpAvg = round( stUpSum / count, 2 )
        szUpAvg = round( szUpSum / count, 2 )
        shUpAvg = round( shUpSum / count, 2 )
        upDiffAvg = round( upDiffSum / count, 2 )
        
        return [ stMaxDownAvg, szMaxDownAvg, shMaxDownAvg, maxDownDiffAvg, stMaxUpAvg,
                    szMaxUpAvg, shMaxUpAvg, maxUpDiffAvg, stUpAvg, szUpAvg, shUpAvg, upDiffAvg ]
        
        
    '''
    @summary: 计算各统计项的最大和最小值
    
    @param datas: 数据集合
    
    @return: 各统计项的最大和最小值
    '''
    def getMaxAndMin( self, datas ):
        endIndex = len( datas ) - 1
        
        maxDownSort = sorted( datas, key=lambda data : data[ 5 ] )
        maxDownMin = maxDownSort[ 0 ][ 5 ]
        maxDownMax = maxDownSort[ endIndex ][ 5 ]
        
        szMaxDownSort = sorted( datas, key=lambda data : data[ 18 ] )
        szMaxDownMin = szMaxDownSort[ 0 ][ 18 ]
        szMaxDownMax = szMaxDownSort[ endIndex ][ 18 ]
        
        shMaxDownSort = sorted( datas, key=lambda data : data[ 19 ] )
        shMaxDownMin = shMaxDownSort[ 0 ][ 19 ]
        shMaxDownMax = shMaxDownSort[ endIndex ][ 19 ]
        
        maxDownDiffSort = sorted( datas, key=lambda data : data[ 24 ] )
        maxDownDiffMin = maxDownDiffSort[ 0 ][ 24 ]
        maxDownDiffMax = maxDownDiffSort[ endIndex ][ 24 ]
        
        maxUpSort = sorted( datas, key=lambda data : data[ 7 ] )
        maxUpMin = maxUpSort[ 0 ][ 7 ]
        maxUpMax = maxUpSort[ endIndex ][ 7 ]
        
        szMaxUpSort = sorted( datas, key=lambda data : data[ 20 ] )
        szMaxUpMin = szMaxUpSort[ 0 ][ 20 ]
        szMaxUpMax = szMaxUpSort[ endIndex ][ 20 ]
        
        shMaxUpSort = sorted( datas, key=lambda data : data[ 21 ] )
        shMaxUpMin = shMaxUpSort[ 0 ][ 21 ]
        shMaxUpMax = shMaxUpSort[ endIndex ][ 21 ]
        
        maxUpDiffSort = sorted( datas, key=lambda data : data[ 25 ] )
        maxUpDiffMin = maxUpDiffSort[ 0 ][ 25 ]
        maxUpDiffMax = maxUpDiffSort[ endIndex ][ 25 ]
        
        upSort = sorted( datas, key=lambda data : data[ 16 ] )
        upMin = upSort[ 0 ][ 16 ]
        upMax = upSort[ endIndex ][ 16 ]
        
        szUpSort = sorted( datas, key=lambda data : data[ 22 ] )
        szUpMin = szUpSort[ 0 ][ 22 ]
        szUpMax = szUpSort[ endIndex ][ 22]
        
        shUpSort = sorted( datas, key=lambda data : data[ 23 ] )
        shUpMin = shUpSort[ 0 ][ 23 ]
        shUpMax = shUpSort[ endIndex ][ 23 ]
        
        upDiffSort = sorted( datas, key=lambda data : data[ 26 ] )
        upDiffMin = upDiffSort[ 0 ][ 26 ]
        upDiffMax = upDiffSort[ endIndex ][ 26 ]
        
        minColl = [ maxDownMin, szMaxDownMin, shMaxDownMin, maxDownDiffMin, maxUpMin, szMaxUpMin, shMaxUpMin, maxUpDiffMin, upMin, szUpMin, shUpMin, upDiffMin ]
        maxColl = [ maxDownMax, szMaxDownMax, shMaxDownMax, maxDownDiffMax, maxUpMax, szMaxUpMax, shMaxUpMax, maxUpDiffMax, upMax, szUpMax, shUpMax, upDiffMax ]
        
        return ( minColl, maxColl )
    
    
    '''
    @summary: 计算小于零的差值占的百分比
    
    @param datas: 数据集合
    
    @return: 小于零的差值占的百分比
    '''
    def getDiffPre( self, datas ):
        count = len( datas )
        
        maxDownDiffSum = 0
        maxUpDiffSum = 0
        UpDiffSum = 0
        
        for data in datas:
            if data[ 24 ] <= 0.0:
                maxDownDiffSum += 1
                
            if data[ 25 ] <= 0.0:
                maxUpDiffSum += 1
                
            if data[ 26 ] <= 0.0:
                UpDiffSum += 1
                
        maxDownDiffPre = round( maxDownDiffSum / count * 100, 2 )
        maxUpDiffPre = round( maxUpDiffSum / count * 100, 2 )
        UpDiffPre = round( UpDiffSum / count * 100, 2 )
        
        return [ maxDownDiffPre, maxUpDiffPre, UpDiffPre  ]
                
            
    '''
    @summary: 删除带有纯ST股票代码数据
    '''
    def deleteSt( self, datas ):
        starStTsCode = self.__findTsCodeForStarST( datas )
        noStDatas = datas.copy()
        
        for row in datas:
            tsCode = row[ 0 ]
            if starStTsCode.count( tsCode) <= 0:
                noStDatas.remove( row )
        
        return noStDatas
    
    
    '''
    @summary: 删除带有*的ST股票代码数据
    '''
    def deleteStarSt( self, datas ):
        starStTsCode = self.__findTsCodeForStarST( datas )
        noStarStDatas = datas.copy()
        
        for row in datas:
            tsCode = row[ 0 ]
            if starStTsCode.count( tsCode) > 0:
                noStarStDatas.remove( row )
        
        return noStarStDatas
    
    
    '''
    @summary: 找出带有*号的ST的股票代码
    '''
    def __findTsCodeForStarST(self, datas ):
        starST = [] # 带有*的ST股票代码集合
        for row in datas:
            tsCode = row[ 0 ]
            name = row[ 1 ] # 曾用名
            
            if name.find( "*" ) != -1 and starST.count( tsCode) == 0 :
                starST.append( tsCode )
                
        return starST