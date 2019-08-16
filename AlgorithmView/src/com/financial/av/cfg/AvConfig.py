#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.kline.cfg.KLineConfig -- 图形展示模块配置类

com.financial.kline.cfg.KLineConfig is a 图形展示模块配置类，暂时用于配置日志路径

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
from com.financial.common.cfg.BaseConfig import BaseConfig

class AvConfig( BaseConfig ):
    
    ## 配置文件所有位置，放到Linux机器上需要改路径
    configFilePath = "D:\\Projects\\financial\\Fv\\config\\fv.config"
    
    def __init__(self ):
        super( AvConfig, self ).__init__( self.configFilePath )
        
    
    '''
    @summary: 获取股票b001算法的后台http接口
    
    @return: 股票b001算法的后台http接口
    '''
    def getStock001UrlConfig( self ):
        return self.getConfigInfo()[ "stock_001_url" ]
    
    
    '''
    @summary: 获取指数b001算法的后台http接口
    
    @return: 指数b001算法的后台http接口
    '''
    def getIndex001UrlConfig( self ):
        return self.getConfigInfo()[ "index_001_url" ]