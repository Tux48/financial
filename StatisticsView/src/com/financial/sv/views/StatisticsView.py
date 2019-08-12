#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年7月26日

com.financial.statistics.views.StView -- 统计视图类

com.financial.statistics.views.StView is a 统计视图类，提供获取统计数据的http接口。接口调用统计后台的http接口，展现返回的统计数据。

It defines classes_and_methods
def st()    st统计数据的http接口
def starSt()    *st统计数据的http接口

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
import json
import urllib3
from flask import Blueprint, render_template

from com.financial.sv.cfg.StatisticsViewConfig import StatisticsViewConfig

sv = Blueprint( "sv", __name__ )


'''
@summary: st统计数据展现接口
'''
@sv.route( "/st" )
def st():
    url = StatisticsViewConfig().getStStatisticsUrl()
    http = urllib3.PoolManager()
    r = http.request( "GET",  url )
    stStatistics = json.loads( r.data )
    
    return render_template( "st.html", datas = stStatistics )


'''
@summary: *st统计数据展现接口
'''
@sv.route( "/star_st" )
def starSt():
    url = StatisticsViewConfig().getStarStStatisticsUrl()
    http = urllib3.PoolManager()
    r = http.request( "GET",  url )
    starStStatistics = json.loads( r.data )

    return render_template( "st.html", datas = starStStatistics )