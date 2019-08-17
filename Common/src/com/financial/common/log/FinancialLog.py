#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2018-12-25

com.financial.common.log.FinancialLog -- 日志工具类

com.financial.common.log.FinancialLog is a 日志工具类，实例化日志目录、文件。添加日志内容。

It defines classes_and_methods:   
def getLogger( self ):    返回日志实例

@author: Administrator

@version: 0.1

@copyright:  2018 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import os
import logging
from logging.handlers import TimedRotatingFileHandler


class FinancialLog:
    
    ## 日志内容格式 时间-日志等级-模块名-方法名-行号-信息
    LOGGING_MSG_FORMAT  = '[%(asctime)s] [%(levelname)s] [%(pathname)s] [%(filename)s] [%(lineno)d] %(message)s'
    
    ## 日志时间格式
    LOGGING_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    
    def __init__( self, logFilePath, logFileName ):
        
        ## 如果目录不存在，创建设目录
        if not os.path.exists( logFilePath ):
            os.makedirs( logFilePath )
        
        logFile = os.path.join( logFilePath, logFileName )
        
        '''
        设置日志文件内容格式
        '''
        logging.basicConfig( level = logging.DEBUG, format = self.LOGGING_MSG_FORMAT, datefmt = self.LOGGING_DATE_FORMAT )
        self.__log = logging.getLogger()
        handler = TimedRotatingFileHandler( logFile, "midnight", 1, encoding = "UTF-8" )    ## 每天凌晨生成一个新日志文件
        formatter = logging.Formatter(self.LOGGING_MSG_FORMAT )
        handler.setFormatter( formatter )
        self.__log.addHandler( handler )

        '''
        设轩控制台输出格式
        '''
        console = logging.StreamHandler()
        console.setLevel( logging.INFO )
        console.setFormatter( logging.Formatter( self.LOGGING_MSG_FORMAT ) )
        self.__log.addHandler( console )
        
    '''
    @summary: 返回日志实例
    '''
    def getLogger( self ):
        return self.__log