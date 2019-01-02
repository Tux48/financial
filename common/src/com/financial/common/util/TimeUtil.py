#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2018年12月30日

com.financial.common.util.TimeUtil -- shortdesc

com.financial.common.util.TimeUtil is a description

It defines classes_and_methods

@author: Administrator

@version: 0.1

@copyright:  2018 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import time

from com.financial.common.cfg.NoLoadTimeConfig import NoLoadTimeConfig

class TimeUtil:
    
    ## 星期六的一周内的第几天代码
    __SATURDAY_CODE = 6
    
    ## 星期日的一周内的第几天代码
    __SUNDAT_CODE = 0
    
    ## 周一到周五在每周的第几天
    __MONDAY_TO_FRIDAY_CODE = [ "1", "2", "3", "4", "5" ]

    ## 所有法定节假日
    NO_LOAD_TIMES = NoLoadTimeConfig().getNoLoadTimes()
    
    '''
    
    '''
    def isLoad( self ):
        dayOfWeek = time.strftime( "%w" )
        monthAndDay = time.strftime( "%m%d" )
        
        '''
        如果当前每周第几天是周六或周日，或当前月、天在不加载数据时间范围同，不加载数据
        '''
        if( ( not dayOfWeek in self.__MONDAY_TO_FRIDAY_CODE ) or 
            ( not monthAndDay in self.NO_LOAD_TIMES ) ):
            return False
        
        return True