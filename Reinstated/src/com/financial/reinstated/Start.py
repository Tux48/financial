#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.reinstated.Start -- 启动复权模块

com.financial.reinstated.Start is a 启动复权模块

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.reinstated.task.ReinstatedScheduler import ReinstatedScheduler

scheduler = ReinstatedScheduler()
scheduler.start()