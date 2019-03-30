#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.suspend.task.SuspendTask -- shortdesc

com.financial.suspend.task.suspendTask is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.suspend.engine.SuspendEngine import SuspendEngine

class SuspendTask:
    
    __suspendEngine = SuspendEngine()
    
    def loadSuspendData( self ):
        self.__suspendEngine.start()