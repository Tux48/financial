#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年5月3日

com.financial.fv.dao.CommonDao -- shortdesc

com.financial.fv.dao.CommonDao is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from sqlalchemy.sql import text

from com.financial.common.db.MySqlDBConnection import MySqlDBConnection


def getAllStock():
    mysqlDBSession = MySqlDBConnection().getMysqlDBSession()
    result = mysqlDBSession.execute( text( "select ts_code, name from stock_basic" ) )
    
    datas = []
    for res in result:
        datas.append( { "tsCode": res[ 0 ], "name": res[ 1 ] } )
        
    result.close()
    mysqlDBSession.close()
    
    return datas

def getAllSSEIndex( tsCode ):
    mysqlDBSession = MySqlDBConnection().getMysqlDBSession()
    result = mysqlDBSession.execute( text( "select trade_date, `open`, high, low, `close`, `vol` from index_line_day_szse where ts_code=:tsCode order by trade_date" ) )
    
    datas = []
    index = 0
    for row in result:
        tradeDate = row[ 0 ]
        open1 = row[ 1 ]    # 不知为啥，open会有警告，所以改成open1
        high = row[ 2 ]
        low = row[ 3 ]
        close = row[ 4 ]
        volume = row[ 5 ]

        datas.insert( index, [ tradeDate, open1, close, low, high, volume ] )
        index += 1
        
    result.close()
    mysqlDBSession.close()
    
    return datas


def getAllSZSEIndex():
    mysqlDBSession = MySqlDBConnection().getMysqlDBSession()
    result = mysqlDBSession.execute( text( "select trade_date, `open`, high, low, `close`, `vol` from index_line_day_szse where ts_code=:tsCode order by trade_date" ) )
    
    datas = []
    index = 0
    for row in result:
        tradeDate = row[ 0 ]
        open1 = row[ 1 ]    # 不知为啥，open会有警告，所以改成open1
        high = row[ 2 ]
        low = row[ 3 ]
        close = row[ 4 ]
        volume = row[ 5 ]

        datas.insert( index, [ tradeDate, open1, close, low, high, volume ] )
        index += 1
        
    result.close()
    mysqlDBSession.close()
    
    return datas