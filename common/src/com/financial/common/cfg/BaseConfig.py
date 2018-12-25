#!/usr/local/bin/python3.7
# encoding: utf-8
'''
Created on 2018年12月24日

com.financial.common.cfg.BaseConfig -- shortdesc

com.financial.common.cfg.BaseConfig is a description

It defines classes_and_methods

@author: WeiFengQing

@version: 0.1

@copyright:  2018 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import os
from configparser import ConfigParser

class BaseConfig:
    
    ## 存放配置的key-value字典
    __configInfoDictionary = dict()

    ## 配置文件名
    __fileName = "";
    
    ## 配置文件绝对路径
    __fileAbsolutePath = ""
    
    ## 配置文件的最后修改时间
    __lastModifyTime = 0;
    
    '''
    @summary: 初始化方法，读取配轩文件件，并获取配置信息
    
    @param fileName: 配置文件名
    '''
    def __init__( self, fileName ):
        self.__fileName = fileName
        
        if not os.path.exists( fileName ):
            s = ''  ## 抛出文件不存在异常
            
        self.__readConfigFile( fileName )
    
    '''
    @summary: 获取配置文件的最后修改时间，并判断上一次记录的修改时间是否与最后修改时间相同。
                         如果不同，返回true，否则返回false。
                         
    @param fileName: 要读取的配置文件全路径
                         
    @return: 如果文件最后修改时间与记录最后修改时间相同返回true，否则返回false。
    '''
    def __needReload( self, fileName ):
        modifyTime = os.path.getmtime( fileName )   ## 获取文件的最后修改时间
        if( modifyTime > self.__lastModifyTime ):
            self.__lastModifyTime = modifyTime
            return True
        
        return False
    
    '''
    @summary: 读取配置文件
    '''
    def __readConfigFile( self, fileName ):
        config = ConfigParser()
        config.read( fileName, 'UF-8' )
        sections = config.sections()
        
        for sec in sections:
            items = config.items( sec )
            for key, value in items:
                self.__addConfigInfo( key, value )
        
    '''
    @summary: 设置配置文件中的内容
    '''
    def __addConfigInfo( self, key, value ):
        self.__lastModifyTime = 0
        
    '''
    @summary: 获取配置信息
    
    @return: 配置信息的key-value集合
    '''
    def getConfigInfo( self, fileName ):
        if( self.__needReload( fileName ) ):
            self.__readConfigFile()
        
        return self.__configInfoDictionary