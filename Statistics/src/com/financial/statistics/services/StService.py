#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年7月26日

com.financial.statistics.services.StService -- shortdesc

com.financial.statistics.services.StService is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
import json

from com.financial.statistics.count.st.StType import NO_STAR_ST_TYPE, STAR_ST_TYPE
from com.financial.statistics.count.st.StatisticsDao import StatisticsDao
from com.financial.statistics.count.st.StUtil import StUtil

class StService:
    
    '''
    @summary: 获取ST统计数据
    '''
    def getStStatistics( self ):
        SQL = StUtil().buildStStatisticsSQL( NO_STAR_ST_TYPE )
        datas = StatisticsDao().getStStatisticsDatas( SQL )
        
        return json.dumps( datas )
    
    
    '''
    @summar: 获取*ST统计数据
    '''
    def getStarStStatistics( self ):
        SQL = StUtil().buildStStatisticsSQL( STAR_ST_TYPE )
        datas = StatisticsDao().getStStatisticsDatas( SQL )
        
        return json.dumps( datas )