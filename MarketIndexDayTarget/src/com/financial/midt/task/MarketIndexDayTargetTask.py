#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.midt.task.MarketIndexDayTargetTask -- shortdesc

com.financial.midt.task.MarketIndexDayTargetTask is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.midt.engine.MarketIndexDayTargetEngine import MarketIndexDayTargetEngine

class MarketIndexDayTargetTask:
    
    __MarketIndexDayTargetEngine = MarketIndexDayTargetEngine()
    
    def loadMarketIndexDayTargetData( self ):
        self.__MarketIndexDayTargetEngine.start()