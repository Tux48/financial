#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2018-12-29

com.financial.common.cfg.NoLoadTimeConfig -- shortdesc

com.financial.common.cfg.NoLoadTimeConfig is a description

It defines classes_and_methods

@author: Administrator

@version: 0.1

@copyright:  2018 organization_name. All rights reserved.

@deffield    updated: Updated
'''
from com.financial.common.cfg.BaseConfig import BaseConfig
from com.financial.common.cfg.FilePathConfig import FilePathConfig


class NoLoadTimeConfig( BaseConfig ):
    
    ## 配置文件所有位置，放到Linux机器上需要改路径
    configFilePath = FilePathConfig().getConfigInfo().get( "no_load_time_config_path" )
    
    def __init__( self ):
        super( NoLoadTimeConfig, self ).__init__( self.configFilePath )
        
    '''
    
    '''
    def getNoLoadTimes( self ):
        configInfoDictionary = self.getConfigInfo()
        noLoadTime = configInfoDictionary.get("no_load_time" )
        
        return noLoadTime.split( "," )