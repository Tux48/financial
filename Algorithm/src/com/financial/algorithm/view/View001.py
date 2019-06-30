#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年5月2日

com.financial.fv.views.View001 -- http接口

com.financial.fv.views.View001 is a http接口，提供b001算法的数据接口，包括股票、指数

It defines classes_and_methods
def buildKLine001ToJson( tsCode )    http接口方法，返回股票的b001算法数据
def buildIndexDay001ToJson( tsCode )    http接口方法，返回指数的b001算法数据

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
from flask import Blueprint

import com.financial.algorithm.services.Service001 as service001

view001 = Blueprint( "view001", __name__ )

'''
@summary: http接口方法，返回股票的b001算法数据

@param tsCode:    股票代码

@return: 计算结果。包括股票数据、所有连跌点数据、所有可买入点数据
'''
@view001.route( "/stock/<tsCode>" )
def buildStock001ToJson( tsCode ):
    return service001.buildKLine001ToJson( tsCode )


'''
@summary: http接口方法，返回指数的b001算法数据

@param tsCode:    指数代码

@return: 计算结果。包括指数数据、所有连跌点数据、所有可买入点数据
'''
@view001.route( "/index/<tsCode>" )
def buildIndexDay001ToJson( tsCode ):
    return service001.buildIndex001ToJson( tsCode )