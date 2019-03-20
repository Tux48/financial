#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.saod.task.StockAccountOpenDataScheduler -- 获取股票账户开户数据数据的定时任务模块

com.financial.saod.task.StockAccountOpenDataScheduler is a 
获取股票账户开户数据数据的定时任务模块

It defines classes_and_methods
def start( self ):    启动任务调度器

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from apscheduler.schedulers.blocking import BlockingScheduler

from com.financial.saod.log.StockAccountOpenDataLog import StockAccountOpenDataLog
from com.financial.saod.task.StockAccountOpenDataTask import StockAccountOpenDataTask

class StockAccountOpenDataScheduler:
    
    ## 任务调度器
    __scheduler  =BlockingScheduler()
    
    ## 任务模块
    __task = StockAccountOpenDataTask()
    
    '''
    @summary: 启动任务调度器
    '''
    def start( self ):
        try:
            StockAccountOpenDataLog().getLog().info( "准备开始执行任务调度" )
            self.__scheduler.add_job( func = self.__task.loadStockAccountOpenDataData, trigger = "cron", 
                                      day_of_week = "mon-fri" , hour = "18", minute = "00" , 
                                      start_date = "2019-01-01", end_date = "2030-12-31" )
            self.__scheduler.start()
            StockAccountOpenDataLog().getLog().info( "已经执行任务调度" )
        except Exception as ex:
            StockAccountOpenDataLog().getLog().error( ex )