#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年7月26日

com.financial.statistics.views.StView -- shortdesc

com.financial.statistics.views.StView is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from flask import Blueprint

from com.financial.statistics.services.StService import StService

sv = Blueprint( "sv", __name__ )

@sv.route( "/st" )
def st():
#     stStatistics = StService().getStStatistics()
#     return render_template( "st.html", datas = stStatistics )

    return StService().getStStatistics()

@sv.route( "/star_st" )
def starSt():
#     starStStatistics = StService().getStarStStatistics()
#     return render_template( "st.html", datas = starStStatistics )

    return StService().getStarStStatistics()