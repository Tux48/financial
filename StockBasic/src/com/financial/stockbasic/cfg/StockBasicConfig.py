#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-4

com.financial.stockbasic.cfg.StockBasicConfig -- 股票基本数据模块配置类

com.financial.stockbasic.cfg.StockBasicConfig is a 
股票基本数据模块配置类，继承自  com.financial.common.cfg.BaseConfig。

It defines classes_and_methods

@see:  com.financial.common.cfg.BaseConfig

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.common.cfg.BaseConfig import BaseConfig

class StockBasicConfig( BaseConfig ):
    
    ## 配置文件所有位置，放到Linux机器上需要改路径
    configFilePath = "D:\\Projects\\financial\\StockBasic\\config\\stock_basic.config"
    
    def __init__(self ):
        super( StockBasicConfig, self ).__init__( self.configFilePath )