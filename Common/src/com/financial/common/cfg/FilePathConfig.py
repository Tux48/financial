#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2018年12月28日

com.financial.common.cfg.LogConfig -- 所有配置文件路径操作类

com.financial.common.cfg.LogConfig is a 
所有配置文件路径操作类。所有配置文件的路径配轩在一个文件里，
由此类统一读取，减少作改的地方，只修改总配置文件的配置读取。

It defines classes_and_methods

@author: Administrator

@version: 0.1

@copyright:  2018 organization_name. All rights reserved.

@deffield    updated: Updated
'''
from com.financial.common.cfg.BaseConfig import BaseConfig

class FilePathConfig( BaseConfig ):
    
    ## 配置文件所有位置，放到Linux机器上需要改路径
    configFilePath = 'D:\\Projects\\financial\\common\\config\\file_path.config'
#     configFilePath = ''
    
    def __init__(self):
        super( FilePathConfig, self ).__init__( self.configFilePath )