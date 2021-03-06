#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.kline.task.KLineTask -- shortdesc

com.financial.kline.task.KLineTask is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.kld.engine.KLineDayEngine import KLineDayEngine

class KLineDayTask:
    
    __kLineDayEngine = KLineDayEngine()
    
    def loadKLineDayData( self ):
        self.__kLineDayEngine.start()