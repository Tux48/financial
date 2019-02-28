#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.klw.task.KLineWeekTask -- shortdesc

com.financial.klw.task.KLineWeekTask is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.klw.engine.KLineWeekEngine import KLineWeekEngine

class KLineWeekTask:
    
    __kLineWeekEngine = KLineWeekEngine()
    
    def loadKLineWeekData( self ):
        self.__kLineWeekEngine.start()