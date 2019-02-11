#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-6

com.financial.stockbasic.Start -- 启动脚本

com.financial.stockbasic.Start is a 
启动脚本

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.stockbasic.task.StockBasicScheduler import StockBasicScheduler

scheduler = StockBasicScheduler()
scheduler.start()