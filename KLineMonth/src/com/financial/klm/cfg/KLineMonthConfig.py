#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.klm.cfg.KLineMonthConfig -- 月K线模块配置类

com.financial.klm.cfg.KLineMonthConfig is a 月K线模块配置类，暂时用于配置日志路径

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
from com.financial.common.cfg.BaseConfig import BaseConfig

class KLineMonthConfig( BaseConfig ):
    
    ## 配置文件所有位置，放到Linux机器上需要改路径
    configFilePath = "D:\\Projects\\financial\\KLineMonth\\config\\k_line_month.config"
    
    def __init__(self ):
        super( KLineMonthConfig, self ).__init__( self.configFilePath )