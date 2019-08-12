#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019-1-7

com.financial.statistics.cfg.StatisticsConfig -- 统计模块配置类

com.financial.statistics.cfg.StatisticsConfig is a 统计模块配置类，暂时用于配置日志路径

It defines classes_and_methods
def getStStatisticsUrl( self )    获取*st统计的url配置接口
def getStarStStatisticsUrl( self )    *st统计的url配置接口

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
from com.financial.common.cfg.BaseConfig import BaseConfig

class StatisticsViewConfig( BaseConfig ):
    
    ## 配置文件所有位置，放到Linux机器上需要改路径
    configFilePath = "D:\\Projects\\financial\\\StatisticsView\\config\\statistics_view.config"
    
    def __init__(self ):
        super( StatisticsViewConfig, self ).__init__( self.configFilePath )
        
        
    '''
    @summary: 获取st统计的url配置接口
    
    @return: st统计的url接口
    '''
    def getStStatisticsUrl( self ):
        return self.getConfigInfo()[ "st_url" ]
    
    
    '''
    @summary: 获取*st统计的url配置接口
    
    @return: *st统计的url接口
    '''
    def getStarStStatisticsUrl( self ):
        return self.getConfigInfo()[ "star_st_url" ]