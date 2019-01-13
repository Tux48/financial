#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.kline.task.KLineScheduler -- shortdesc

com.financial.kline.task.KLineScheduler is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from apscheduler.schedulers.blocking import BlockingScheduler

from com.financial.kline.log.KLineLog import KLineLog
from com.financial.kline.task.KLineTask import KLineTask

class KLineScheduler:
    
    ## 任务调度器
    __scheduler  =BlockingScheduler()
    
    __task = KLineTask()
    
    '''
    @summary: 启动任务调度器
    '''
    def start( self ):
        try:
            KLineLog().getLog().info( "准备开始执行任务调度" )
            self.__scheduler.add_job( func = self.__task.loadingKLineData, trigger = "cron", 
                                      day_of_week = "mon-fri" , hour = "20", minute = "00" , 
                                      start_date = "2019-01-01", end_date = "2030-12-31" )
            self.__scheduler.start()
            KLineLog().getLog().info( "已经执行任务调度" )
        except Exception as ex:
            KLineLog().getLog().error( ex )