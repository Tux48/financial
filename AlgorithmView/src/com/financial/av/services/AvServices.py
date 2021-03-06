#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年5月3日

com.financial.fv.services.CommonServices -- shortdesc

com.financial.fv.services.CommonServices is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

import json

import com.financial.av.dao.AvDao as avDao

def buildStockCodeToJson():
    datas = avDao.getAllStock()
    return json.dumps( datas )


def buildIndexCodeToJson():
    sseIndexs = avDao.getAllSSEIndex()
    szseIndexs = avDao.getAllSZSEIndex()
    
    return json.dumps( { "sse": sseIndexs, "szse": szseIndexs } )