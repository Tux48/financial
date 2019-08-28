#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年8月5日

com.financial.statistics.scheduler.SchedulerConfig -- shortdesc

com.financial.statistics.scheduler.SchedulerConfig is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

class SchedulerJobConfig(object):
    JOBS = [
        {
            'id': 'autoStStatistics',
            'func': 'com.financial.statistics.scheduler.StJob:stStatistics', # 路径：job函数名
            'args': None,
            'trigger': {
                'type': 'cron',
                'day_of_week':"mon-sun",
                'hour': '14',
                'minute': '38'
            }
        }
    ]
    SCHEDULER_API_ENABLED = True
    SQLALCHEMY_ECHO = True