#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.kline.cfg.KLineConfig -- shortdesc

com.financial.kline.cfg.KLineConfig is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
from com.financial.common.cfg.BaseConfig import BaseConfig

class KLineConfig( BaseConfig ):
    
    ## 配置文件所有位置，放到Linux机器上需要改路径
    configFilePath = "D:\\Projects\\financial\\KLine\\config\\k_line.config"
    
    def __init__(self ):
        super( KLineConfig, self ).__init__( self.configFilePath )