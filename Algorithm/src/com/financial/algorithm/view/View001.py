#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年5月2日

com.financial.fv.views.B_001_View -- http接口

com.financial.fv.views.B_001_View is a http接口，提供b001算法的数据接口，包括股票、指数

It defines classes_and_methods
def buildKLineB001ToJson( tsCode )    http接口方法，返回股票的b001算法数据
def buildIndexDayB001ToJson( tsCode )    http接口方法，返回指数的b001算法数据

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
from flask import Blueprint

import com.financial.algorithm.services.B001_Service as b001Service 

b001 = Blueprint( "b001", __name__ )

'''
@summary: http接口方法，返回股票的b001算法数据

@param tsCode:    股票代码

@return: 计算结果。包括股票数据、所有连跌点数据、所有可买入点数据
'''
@b001.route( "/kline/<tsCode>" )
def buildKLineB001ToJson( tsCode ):
    return b001Service.buildKLineB001ToJson( tsCode )


'''
@summary: http接口方法，返回指数的b001算法数据

@param tsCode:    指数代码

@return: 计算结果。包括指数数据、所有连跌点数据、所有可买入点数据
'''
@b001.route( "/index_day/<tsCode>" )
def buildIndexDayB001ToJson( tsCode ):
    return b001Service.buildIndexDayB001ToJson( tsCode )