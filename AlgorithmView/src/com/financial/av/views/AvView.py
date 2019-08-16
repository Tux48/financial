#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年5月3日

com.financial.fv.views.Common_View -- shortdesc

com.financial.fv.views.Common_View is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from flask import Blueprint, render_template

import com.financial.av.services.AvServices as avServices


# from flask.templating import render_template
fv = Blueprint( "fv", __name__ )

@fv.route( "/stock" )
def stock():
    return render_template( "stock.html" )

@fv.route( "/index" )
def index():
    return render_template( "index.html" )

@fv.route( "/allStockCode" )
def allStockCode():
    return avServices.buildStockCodeToJson()

@fv.route( "/allIndexCode" )
def allIndexCode():
    return avServices.buildIndexCodeToJson()