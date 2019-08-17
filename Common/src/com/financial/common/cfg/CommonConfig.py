#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2018-12-25

com.financial.common.db.MySqlConfig -- Mysql数据库配置信息获取工具类

com.financial.common.db.MySqlConfig is a Mysql数据库配置信息获取工具类

@author: Administrator

@version: 0.1

@copyright:  2018 organization_name. All rights reserved.

@deffield    updated: Updated
'''
from com.financial.common.cfg.BaseConfig import BaseConfig

class CommonConfig( BaseConfig ):
    
    ## 配置文件所有位置，放到Linux机器上需要改路径
    configFilePath = "D:\\Projects\\financial\\common\\config\\common.config"
    
    def __init__(self):
        super( CommonConfig, self ).__init__( self.configFilePath )