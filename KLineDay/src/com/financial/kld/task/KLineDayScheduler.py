#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.kld.task.KLineDayScheduler -- 获取日K线数据的定时任务模块

com.financial.kld.task.KLineDayScheduler is a 
获取日K线数据的定时任务模块

It defines classes_and_methods
def start( self ):    启动任务调度器

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from apscheduler.schedulers.blocking import BlockingScheduler

from com.financial.kld.log.KLineDayLog import KLineDayLog
from com.financial.kld.task.KLineDayTask import KLineDayTask

class KLineDayScheduler:
    
    ## 任务调度器
    __scheduler  =BlockingScheduler()
    
    ## 任务模块
    __task = KLineDayTask()
    
    '''
    @summary: 启动任务调度器
    '''
    def start( self ):
        try:
            KLineDayLog().getLog().info( "准备开始执行任务调度" )
            self.__scheduler.add_job( func = self.__task.loadKLineDayData, trigger = "cron", 
                                      day_of_week = "mon-sun" , hour = "14", minute = "40" , 
                                      start_date = "2019-01-01", end_date = "2030-12-31" )
            self.__scheduler.start()
            KLineDayLog().getLog().info( "已经执行任务调度" )
        except Exception as ex:
            KLineDayLog().getLog().error( ex )