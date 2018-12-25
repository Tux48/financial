#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2018-12-25

com.financial.common.log.FinancialLog -- 日志工具类

com.financial.common.log.FinancialLog is a 日志工具类，实例化日志目录、文件。添加日志内容。

It defines classes_and_methods:   def addInfoLog( self, message ): 添加info级别日志内容
                                                    def addDebugLog( self, message ): 添加debug级别日志内容
                                                    def addWaringLog( self, message ): 添加waring级别日志内容
                                                    def addErrorLog( self, message ): 添加error级别日志内容
                                                    def addCriticalLog( self, message ): 添加critical级别日志内容

@author: Administrator

@version: 0.1

@copyright:  2018 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import os
import logging

class FinancialLog:
    
    ## 日志内容格式 时间-日志等级-模块名-方法名-行号-信息
    LOGGING_MSG_FORMAT  = '[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s] [%(lineno)d] %(message)s'
    
    ## 日志时间格式
    LOGGING_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    
    ## 日志对像
    log = None
    
    def __init__( self, logFilePath, logFileName ):
        
        logging.basicConfig( level = logging.DEBUG, format = self.LOGGING_MSG_FORMAT, datefmt=self.LOGGING_DATE_FORMAT )
        log = logging.getLogger( 'simple_example'  )
        
        ## 如果目录不存在，创建设目录
        if not os.path.exists( logFilePath ):
            os.makedirs( logFilePath )
        
        '''
        设置日志文件内容格式
        '''
        logFile = os.path.join( logFilePath, logFileName )
        logger = logging.handlers.TimedRotatingFileHandler( logFile, 'midnight', 1 )    ## 每天凌晨生成一个新日志文件
        logger.setFormatter( logging.Formatter( self.LOGGING_MSG_FORMAT ) )
        log.addHandler( logger )
        
        '''
        设轩控制台输出格式
        '''
        console = logging.StreamHandler()
        console.setLevel( logging.INFO )
        console.setFormatter( logging.Formatter( self.LOGGING_MSG_FORMAT ) )
        log.addHandler( console )
        
    '''
    @summary: 添加info级别日志内容
    
    @param message: 日志内容 
    '''
    def addInfoLog( self, message ):
        self.log.info( message )
        
    ''''
    @summary: 添加debug级别日志内容
    
    @param message: 日志内容 
    '''
    def addDebugLog( self, message ):
        self.log.debug( message )
        
    '''
    @summary: 添加waring级别日志内容
    
    @param message: 日志内容 
    '''
    def addWaringLog( self, message ):
        self.log.waring( message )
        
    '''
    @summary: 添加error级别日志内容
    
    @param message: 日志内容 
    '''
    def addErrorLog( self, message ):
        self.log.error( message )
        
    '''
    @summary: 添加critical级别日志内容
    
    @param message: 日志内容 
    '''
    def addCriticalLog( self, message ):
        self.log.critical( message )