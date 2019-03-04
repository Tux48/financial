#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.klm.task.KLineMonthTask -- shortdesc

com.financial.klm.task.KLineMonthTask is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.klm.engine.KLineMonthEngine import KLineMonthEngine

class KLineMonthTask:
    
    __kLineMonthEngine = KLineMonthEngine()
    
    def loadKLineMonthData( self ):
        self.__kLineMonthEngine.start()