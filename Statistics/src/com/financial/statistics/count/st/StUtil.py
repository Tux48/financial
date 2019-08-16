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
        SQL = "select ts_code, name, st_date, pre_close, st_min_low, st_max_down, st_max_high, st_max_up, st_duration, cancle_st_date, st_last_close, cancle_st_high, cancle_st_max_up, cancle_st_low, cancle_st_max_down, is_his_low, st_up, st_days, sz_max_down, sh_max_down, sz_max_up, sh_max_up, sz_up, sh_up from st_statistics where cancle_st_date is not null and st_type=0"
        if stType == STAR_ST_TYPE:
            SQL = "select ts_code, name, st_date, pre_close, st_min_low, st_max_down, st_max_high, st_max_up, st_duration, cancle_st_date, st_last_close, cancle_st_high, cancle_st_max_up, cancle_st_low, cancle_st_max_down, is_his_low, st_up, st_days, sz_max_down, sh_max_down, sz_max_up, sh_max_up, sz_up, sh_up from st_statistics where cancle_st_date is not null and st_type=1"
            
        return SQL
        
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