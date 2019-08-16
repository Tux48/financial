#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.statistics.dao.StatisticsDao -- 统计数据库DAO工具类

com.financial.statistics.dao.StatisticsDao is a 
数据库DAO工具类，主要用于统计的操作

It defines classes_and_methods
def getStockBasicDict( self ):    获取股票基本数据，以 dict 形式返回
def saveStatisticsDatas( self, StatisticsDatas ):    保存统计数据
def deleteStatisticsDatas( self ):    删除所有统计数据
def __getMyDBSession( self ):    获取数据库连接

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import threading
from sqlalchemy.sql import text

from com.financial.statistics.count.st.StBean import StBean
from com.financial.statistics.log.StatisticsLog import StatisticsLog
from com.financial.statistics.db.StatisticsDBConnection import StatisticsDBConnection


class StatisticsDao:
    
    ## 是否是第一次初始化标志
    __first_init = True
    
    ## 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__( cls, *args, **kwargs ):
        if not hasattr( StatisticsDao, "_instance" ):
            with StatisticsDao.__instance_lock:
                if not hasattr( StatisticsDao, "_instance" ):
                    StatisticsDao._instance = object.__new__( cls )
                    
        return StatisticsDao._instance
    
    def __init__( self  ):
        pass
    
    
    '''
    @summary: 查询st统计数据
    '''
    def getStStatisticsDatas( self, SQL ):
        StatisticsLog().getLog().info( "开始获取st统计数据" )
        
        statisticsDBSession = StatisticsDBConnection().getStatisticsDBSession()
        result = statisticsDBSession.execute( text( SQL ) )
        
        datas = []
        for row in result:
            datas.append( [ row[ 0 ], row[ 1 ], row[ 2 ], row[ 3 ], row[ 4 ], row[ 5 ], row[ 6 ], row[ 7 ], row[ 8 ], 
                           row[ 9 ], row[ 10 ], row[ 11 ], row[ 12 ], row[ 13 ], row[ 14 ], row[ 15 ], row[ 16 ], row[ 17 ],
                           row[ 18 ], row[ 19 ], row[ 20 ], row[ 21 ], row[ 22 ], row[ 23 ] ] )
        
        result.close()
        statisticsDBSession.close()
        
        StatisticsLog().getLog().info( "获取st统计数据完毕" )
        
        return datas
    
    
    '''
    @summary: 删除所有旧st数据
    
    '''
    def deleteOldStStatistics( self, stType ):
        StatisticsLog().getLog().info( "开始删除旧st数据" )
        
        statisticsDBSession = StatisticsDBConnection().getStatisticsDBSession()
      
        statisticsDBSession.query( StBean ).filter( StBean.stType == stType ).delete()
              
        statisticsDBSession.commit()
        statisticsDBSession.close()
        
        StatisticsLog().getLog().info( "删除旧st数据完毕" )
        
    
    '''
    @summary: 获取所有st数据
    
    @param stockBasicDatas: 所有st数据的 list 
    '''
    def saveStDatas( self, stDatas ):
        
        StatisticsLog().getLog().info( "开始保存st数据" )
        
        statisticsDBSession = StatisticsDBConnection().getStatisticsDBSession()
      
        for st in stDatas:
            statisticsDBSession.add( st )
              
        statisticsDBSession.commit()
        statisticsDBSession.close()
        
        StatisticsLog().getLog().info( "保存st数据完毕" )