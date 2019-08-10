#!/usr/local/bin/python3.7
# encoding: utf-8
'''
Created on 2018年12月24日

com.financial.common.cfg.BaseConfig -- 读取配轩文件基类

com.financial.common.cfg.BaseConfig is a 
读取配轩文件基类，读取配文件，并将配置信息加载到内存中。
加载配置信息时，通过文件最后修改时间判断配置文件是否被
修改过，如果被修改，则重新加载。

It defines classes_and_methods

def __needReload( self ):                         判断是否需要重新加载
def __readConfigFile( self ):                     读取配置文件
def __addConfigInfo( self, key, value ):    将配置信息以key-value的方式放到字典中
def getConfigInfo( self ):                        供外部调用，返回配置信息

@author: WeiFengQing

@version: 0.1

@copyright:  2018 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import os
from configparser import ConfigParser

class BaseConfig:
    
    '''
    @summary: 初始化方法，读取配轩文件件，并获取配置信息
    
    @param fileName: 配置文件名
    '''
    def __init__( self, fileName ):
        self.__configInfoDictionary = dict()    ## 存放配置的key-value字典
        self.__fileAbsolutePath = ""    ## 配置文件绝对路径
        self.__lastModifyTime = 0   ## 配置文件的最后修改时间
        self. __fileName = ""   ## 配置文件名
        
        self.__fileName = fileName
        self.__readConfigFile()
    
    '''
    @summary: 获取配置文件的最后修改时间，并判断上一次记录的修改时间是否与最后修改时间相同。
                         如果不同，返回true，否则返回false。
                         
    @param fileName: 要读取的配置文件全路径
                         
    @return: 如果文件最后修改时间与记录最后修改时间相同返回true，否则返回false。
    '''
    def __needReload( self ):
        modifyTime = os.path.getmtime( self.__fileName )   ## 获取文件的最后修改时间
        if( modifyTime > self.__lastModifyTime ):
            self.__lastModifyTime = modifyTime
            return True
        
        return False
    
    '''
    @summary: 读取配置文件
    '''
    def __readConfigFile( self ):
        config = ConfigParser()
        config.read( self.__fileName, 'UTF-8' )
        sections = config.sections()
        
        for sec in sections:
            items = config.items( sec )
            for key, value in items:
                self.__addConfigInfo( key, value )
        
    '''
    @summary: 设置配置文件中的内容
    
    @param key:        配置内容的键
    @param value:     配置内容的值
    '''
    def __addConfigInfo( self, key, value ):
        self.__configInfoDictionary.setdefault( key, value )
        
    '''
    @summary: 获取配置信息
    
    @return: 配置信息的key-value字典
    '''
    def getConfigInfo( self ):
        if( self.__needReload() ):
            self.__readConfigFile()
        
        return self.__configInfoDictionary