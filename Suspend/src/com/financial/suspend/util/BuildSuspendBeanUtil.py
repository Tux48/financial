#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
'''
Created on 2019-2-3

com.financial.suspend.util.BuildSuspendBeanUtil -- 构建要保存到数据库的停复牌信息bean的工具类

com.financial.suspend.util.BuildSuspendBeanUtil is a 
一个单例类，根据不同的条件构建相应要保存到数据库的停复牌信息bean

It defines classes_and_methods

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''
import threading

from com.financial.suspend.bean.SuspendBean import SuspendBean


class BuildSuspendBeanUtil:
    
    # # 是否是第一次初始化标志
    __first_init = True
    
    # # 线程锁，用于处于多线程序时的单例不同问题
    __instance_lock = threading.Lock()
    
    '''
    @note: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    @todo: _instance 一定要是单下划线，如果双下划线，无法实现单例。原因？？？
    '''
    def __new__(cls, *args, **kwargs):
        if not hasattr(BuildSuspendBeanUtil, "_instance"):
            with BuildSuspendBeanUtil.__instance_lock:
                if not hasattr(BuildSuspendBeanUtil, "_instance"):
                    BuildSuspendBeanUtil._instance = object.__new__(cls)
                    
        return BuildSuspendBeanUtil._instance
    
    def __init__(self):
        pass
    
    '''
    @summary: 根据不同的股票代码前缀构建并返回相应的保存到数据库bean的集合。
    
    @param dataFormat: 格式化后的停复牌信息数据
    
    @return: 保存到数据库bean的集合
    '''

    def buildSuspendBean(self, dataFormat):
       
        suspendDatas = []
        for index, row in dataFormat.iterrows():
            suspendBean = SuspendBean()
            self.__addAttributeValue(suspendBean, row)
            suspendDatas.insert(index, suspendBean)
            
        return suspendDatas
    
    def __addAttributeValue(self, bean, row):
        bean.tsCode = row[ "ts_code" ]
        bean.suspendDate = row[ "suspend_date" ]
        bean.resumeDate = row[ "resume_date" ]
        bean.suspendReason = row[ "suspend_reason" ]