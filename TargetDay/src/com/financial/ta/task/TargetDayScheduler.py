#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.ta.task.TargetDayScheduler -- 获取每日指标数据的定时任务模块

com.financial.ta.task.TargetDayScheduler is a 
获取每日指标数据的定时任务模块

It defines classes_and_methods
def start( self ):    启动任务调度器

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from apscheduler.schedulers.blocking import BlockingScheduler

from com.financial.ta.log.TargetDayLog import TargetDayLog
from com.financial.ta.task.TargetDayTask import TargetDayTask

class TargetDayScheduler:
    
    ## 任务调度器
    __scheduler  =BlockingScheduler()
    
    ## 任务模块
    __task = TargetDayTask()
    
    '''
    @summary: 启动任务调度器
    '''
    def start( self ):
        try:
            TargetDayLog().getLog().info( "准备开始执行任务调度" )
            self.__scheduler.add_job( func = self.__task.loadTargetDayData, trigger = "cron", 
                                      day_of_week = "mon-fri" , hour = "18", minute = "00" , 
                                      start_date = "2019-01-01", end_date = "2030-12-31" )
            self.__scheduler.start()
            TargetDayLog().getLog().info( "已经执行任务调度" )
        except Exception as ex:
            TargetDayLog().getLog().error( ex )