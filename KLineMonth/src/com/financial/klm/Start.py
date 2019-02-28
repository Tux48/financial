#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.klm.Start -- shortdesc

com.financial.klm.Start is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.klm.task.KLineMonthScheduler import KLineMonthScheduler

scheduler = KLineMonthScheduler()
scheduler.start()