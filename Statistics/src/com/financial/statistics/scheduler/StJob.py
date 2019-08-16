#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年8月5日

com.financial.statistics.scheduler.StJob -- shortdesc

com.financial.statistics.scheduler.StJob is a description

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''

from com.financial.statistics.count.st.StarST import StarST
from com.financial.statistics.count.st.OnlyST import OnlyST
from com.financial.statistics.log.StatisticsLog import StatisticsLog
# from com.financial.statistics.count.st.FinancialDao import FinancialDao
from com.financial.statistics.count.st.NameChangeLoad import NameChangeLoad

from com.financial.statistics.scheduler import scheduler

def stStatistics():
    with scheduler.app.app_context():
        
        try:
#             datas = FinancialDao().getAllNameChangeDatas()
            datas = NameChangeLoad().load()
            OnlyST().stCount( datas )
            StarST().starStCount( datas )
        except Exception as err:
                StatisticsLog.getLog().error( err )