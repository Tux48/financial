#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年5月9日

com.financial.algorithm.services.B001_Service -- 算法接口服务类

com.financial.algorithm.services.B001_Service is a 算法接口服务类，主要用于供http接口调用，计算、封装数据，并返回

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import json

from com.financial.algorithm.a001.B001 import B001
from com.financial.algorithm.a001.S001 import S001
from com.financial.algorithm.util.AlgorithmUtil import AlgorithmUtil
from com.financial.algorithm.dao.AlgorithmDao import AlgorithmDao


'''
@summary: 计算并返回股票的b001算法数据

@param tsCode:    股票代码

@return: 计算结果。包括股票数据、所有连跌点数据、所有可买入点数据
'''
def buildKLine001ToJson( tsCode ):
    tsCodePrefix = AlgorithmUtil.get_tsCodePrefix( tsCode )
    SQL = AlgorithmUtil().buildKLineSQL( tsCodePrefix )
    
    datas = AlgorithmDao().getAlgorithmDate( SQL, tsCode )
    ( allDownPoint, allBuyPoint ) = B001().compute( datas )
    ( allUpPoint, allSellPoint ) = S001().compute( datas )
    
    return json.dumps( { "data": datas, "down": allDownPoint, "buy": allBuyPoint, "up": allUpPoint, "sell": allSellPoint }  )


'''
@summary: 计算并返回指数的b001算法数据

@param tsCode:    指数代码

@return: 计算结果。包括指数数据、所有连跌点数据、所有可买入点数据
'''
def buildIndex001ToJson( tsCode ):
    tsCodeSuffix = AlgorithmUtil().get_tsCodeSuffix( tsCode )
    SQL = AlgorithmUtil().buildIndexDaySQL( tsCodeSuffix )
    
    datas = AlgorithmDao().getAlgorithmDate( SQL, tsCode )
    ( allDownPoint, allBuyPoint ) = B001().compute( datas )
    ( allUpPoint, allSellPoint ) = S001().compute( datas )
    
    return json.dumps( { "data": datas, "down": allDownPoint, "buy": allBuyPoint, "up": allUpPoint, "sell": allSellPoint }  )