#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年7月13日

com.financial.statistics.st.ST -- *st数据统计类

com.financial.statistics.st.ST is a *st数据统计类

It defines classes_and_methods
def compute( self, datas ):    统计入口

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.statistics.count.st.StType import STAR_ST_TYPE
from com.financial.statistics.count.st.StUtil import StUtil
from com.financial.statistics.count.st.ST import ST
 
 
class StarST( ST ):
    
    '''
    @summary: 数据统计入口
     
    @param datas: 所有st数据
    '''
    def starStCount(self, datas ):
        stDatas = StUtil().deleteSt( datas )
        self.compute( stDatas, STAR_ST_TYPE )