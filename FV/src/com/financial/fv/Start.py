#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年5月2日

fv.Start -- shortdesc

fv.Start is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from flask import Flask

from com.financial.fv.views.Fv_View import fv
from com.financial.fv.views.IndexDay_View import indexDay
from com.financial.fv.views.KLine_View import kLine

app = Flask( __name__ )

app.register_blueprint( fv, url_prefix= "/fv" )
app.register_blueprint( kLine, url_prefix= "/kline" )
app.register_blueprint( indexDay, url_prefix= "/index_day" )

if __name__ == '__main__':
    app.run( host = "127.0.0.1", port = "8080", debug = True )