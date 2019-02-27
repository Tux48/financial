#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.kline.task.KLineTask -- 复权任务

com.financial.kline.task.KLineTask is a 复权任务

It defines classes_and_methods
def loadReinstatedData( self ):    加载复权数据

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.reinstated.engine.ReinstatedEngine import ReinstatedEngine

class ReinstatedTask:
    
    __reinstatedEngine = ReinstatedEngine()
    
    
    '''
    @summary: 加载复权数据
    '''
    def loadReinstatedData( self ):
        self.__reinstatedEngine.start()