#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-30

com.financial.stockbasic.Context -- 任务调试器

com.financial.stockbasic.Context is a 
任务调试器，周一至周五的早上9:10执行。

It defines classes_and_methods
def start( self )    启动任务调度器

@author: Administrator

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from apscheduler.schedulers.blocking import BlockingScheduler

from com.financial.stockbasic.log.StockBasicLog import StockBasicLog
from com.financial.stockbasic.task.StockBasicTask import StockBasicTask

class StockBasicScheduler:
    
    ## 任务调度器
    __scheduler  =BlockingScheduler()
    
    ## 任务
    __task = StockBasicTask()
    
    def __init__( self ):
        pass

    '''
    @summary: 启动任务调度器
    '''
    def start( self ):
        try:
            StockBasicLog().getLog().info( "准备开始执行任务调度" )
            self.__scheduler.add_job( func = self.__task.loadingStockBasicData, trigger = "cron", 
                                      day_of_week = "mon-fri" , hour = "20", minute = "00" , 
                                      start_date = "2019-01-01", end_date = "2030-12-31" )
            self.__scheduler.start()
            StockBasicLog().getLog().info( "已经执行任务调度" )
        except Exception as ex:
            StockBasicLog().getLog().error( ex )
            