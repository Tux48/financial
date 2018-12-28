#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2018-12-25

com.financial.common.db.MongoDBConfig -- MongoDB数据库配置信息获取工具类

com.financial.common.db.MongoDBConfig is a 
MongoDB数据库配置信息获取工具类

It defines classes_and_methods

@author: Administrator

@version: 0.1

@copyright:  2018 organization_name. All rights reserved.

@deffield    updated: Updated
'''
from com.financial.common.cfg.BaseConfig import BaseConfig
from com.financial.common.cfg.FilePathConfig import FilePathConfig

class MongoDBConfig( BaseConfig ):
    
    ## 配置文件所有位置，放到Linux机器上需要改路径
    configFilePath = FilePathConfig().getConfigInfo().get( "mongodb_config_path" )

    def __init__( self ):
        super( MongoDBConfig, self ).__init__( self.configFilePath )