#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.ta.cfg.TargetDayConfig -- 每日指标模块配置类

com.financial.ta.cfg.TargetDayConfig is a 每日指标模块配置类，暂时用于配置日志路径

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
from com.financial.common.cfg.BaseConfig import BaseConfig

class TargetDayConfig( BaseConfig ):
    
    ## 配置文件所有位置，放到Linux机器上需要改路径
    configFilePath = "D:\\Projects\\financial\\TargetDay\\config\\target_day.config"
    
    def __init__(self ):
        super( TargetDayConfig, self ).__init__( self.configFilePath )