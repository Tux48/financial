#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.kls.task.KLineWeekScheduler -- 获取月K线数据的定时任务模块

com.financial.klw.task.KLineWeekScheduler is a 
获取月K线数据的定时任务模块

It defines classes_and_methods
def start( self ):    启动任务调度器

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from apscheduler.schedulers.blocking import BlockingScheduler

from com.financial.klm.log.KLineWeekLog import KLineMonthLog
from com.financial.klm.task.KLineMonthTask import KLineMonthTask

class KLineWeekScheduler:
    
    ## 任务调度器
    __scheduler  =BlockingScheduler()
    
    ## 任务模块
    __task = KLineMonthTask()
    
    '''
    @summary: 启动任务调度器
    '''
    def start( self ):
        try:
            KLineMonthLog().getLog().info( "准备开始执行任务调度" )
            self.__scheduler.add_job( func = self.__task.loadKLineMonthData, trigger = "cron", 
                                      day_of_week = "mon-fri" , hour = "18", minute = "00" , 
                                      start_date = "2019-01-01", end_date = "2030-12-31" )
            self.__scheduler.start()
            KLineMonthLog().getLog().info( "已经执行任务调度" )
        except Exception as ex:
            KLineMonthLog().getLog().error( ex )