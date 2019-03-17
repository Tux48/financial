#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.ild.task.IndexLineDayScheduler -- 获取指数日线行情数据的定时任务模块

com.financial.ild.task.IndexLineDayScheduler is a 
获取指数日线行情数据的定时任务模块

It defines classes_and_methods
def start( self ):    启动任务调度器

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from apscheduler.schedulers.blocking import BlockingScheduler

from com.financial.ild.log.IndexLineDayLog import IndexLineDayLog
from com.financial.ild.task.IndexLineDayTask import IndexLineDayTask

class IndexLineDayScheduler:
    
    ## 任务调度器
    __scheduler  =BlockingScheduler()
    
    ## 任务模块
    __task = IndexLineDayTask()
    
    '''
    @summary: 启动任务调度器
    '''
    def start( self ):
        try:
            IndexLineDayLog().getLog().info( "准备开始执行任务调度" )
            self.__scheduler.add_job( func = self.__task.loadIndexLineDayData, trigger = "cron", 
                                      day_of_week = "mon-sun" , hour = "09", minute = "35" , 
                                      start_date = "2019-01-01", end_date = "2030-12-31" )
            self.__scheduler.start()
            IndexLineDayLog().getLog().info( "已经执行任务调度" )
        except Exception as ex:
            IndexLineDayLog().getLog().error( ex )