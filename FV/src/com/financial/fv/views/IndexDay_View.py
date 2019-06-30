#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年5月11日

com.financial.fv.views.IndexDay_View -- shortdesc

com.financial.fv.views.IndexDay_View is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
import urllib3
from flask import Blueprint

from com.financial.fv.cfg.FvConfig import FvConfig

indexDay = Blueprint( "indexDay", __name__ )


@indexDay.route( "/b001/<tsCode>" )
def b001( tsCode ):
    url = FvConfig().getIndexDayB001UrlConfig().format( tsCode )
    http = urllib3.PoolManager()
    r = http.request( "GET",  url )

    return r.data