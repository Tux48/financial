#!/usr/local/bin/python3.7
#-*- coding: utf-8 -*-
'''
Created on 2019年4月11日

com.financial.algorithm.B_001 -- B002算法

com.financial.algorithm.B_001 is a 
2019-06-24提出的第一个卖出算法，参见doc目录下的卖出算法1_B002.docx

It defines classes_and_methods
def compute( self, datas )    算法入口
def __algorithmStep1( self, stockDataFrame )    算法第一步
def __algorithmStep2( self, dataBlock )    算法第二步

@author: Tux48

@version: 0.1

@copyright:  2019 organization_name. All rights reserved.

@deffield    updated: Updated
'''


class S001:
    
    '''
    @summary: 算法入口
    
    @datas: 股票或指数数据
    
    @return: 计算结果。包括所有连涨点数据、所有可卖出点数据
    '''
    def compute( self, datas ):
        return self.__algorithmStep1( datas )

    
    '''
    @summary: 算法第一步  第一个条件  连续出现九根日K线，并且这些日K线的收盘价都比各自前面的第四根日K线的收盘价高,
                                                            在其日K线下方标记相应的数字第1根标注1，第2根标注2，依次类推。如果某一根的日
                                                            K线的收盘价不高于前面第四根的日K线的收盘价，则原计数清零,需重新开始计算。
    
    @param datas: 股票数据
    
    @return: 计算结果。包括所有连涨点数据、所有可卖出点数据
    '''
    def __algorithmStep1( self, datas ):
        
        startIndex = 0
        length = len( datas )
        
        allUpPoint = []   # 存放所有符合第一步计算条件的数据块
        allSellPoint = []    # 所可以卖出的点
        dataBlock = []  # 某一单独数据块
        
        upData = []
        index = 1
        
        for endIndex in range( 4, length ):
            startPointClose = datas[ startIndex ][ 2 ] # 开始点收盘价
            endPointClose = datas[ endIndex ][ 2 ] # 结束点收盘价
            
            ## 日K线的收盘价都比各自前面的第四根日K线的收盘价低
            if endPointClose > startPointClose:
                endPoint = datas[ endIndex ]
                
                tradeDate = endPoint[ 0 ]
                open1 = endPoint[ 1 ]  # 不知为啥，open会有警告，所以改成open1
                close = endPoint[ 2 ]
                low = endPoint[ 3 ]
                high = endPoint[ 4 ]
                volume = endPoint[ 5 ]
                
                dataBlock.append( [ tradeDate, open1, close, low, high, volume ] )
                upData.append( { "name": index, "value": [ tradeDate, high ] } )
                index += 1
            else:
                dataBlock.clear()
                upData.clear()
                index = 1
                
            dataBlockLen = len( dataBlock )
            if dataBlockLen >= 9:
                sellPoint = self.__algorithmStep2( dataBlock.copy() )
                sellPointLen = len( sellPoint )
                    
                if sellPointLen > 0:
                    allUpPoint.extend( upData )
                    allSellPoint.extend( sellPoint )
                    
                dataBlock.clear()
                upData.clear()
                index = 1
                                
            startIndex += 1
            
        return ( allUpPoint, allSellPoint )
    
    
    '''
    @summary: 算法第二步，第8根日K线或第9根日K线的最高价大于第6根日k线或第7根日K线的最高价，在第9根日K线的下方显示△,此时符合卖出的条件..
    
    @param allDataBlock: 算法第一步的计算结果
    
    @return: 计算结果。包括所有连涨点数据、所有可卖出点数据
    '''
    def __algorithmStep2( self, dataBlock ):
                    
        dataBlock0_9 = dataBlock[ :9 ]
        
        ## 取出第6、7、8、9节点数据。第9对比7，8对比6
        data6 = dataBlock0_9[ 5 ]
        data7 = dataBlock0_9[ 6 ]
        data8 = dataBlock0_9[ 7 ]
        data9 = dataBlock0_9[ 8 ]
        
        # 取出各结点的最高价
        dataHigh6 = data6[ 4 ]
        dataHigh7 = data7[ 4 ]
        dataHigh8 = data8[ 4 ]
        dataHigh9 = data9[ 4 ]
        
        sellPoint = []
        
        if dataHigh9 > dataHigh7:
            tradeDate = data9[ 0 ]
            dataLow9 = data9[ 3 ]
            sellPoint.append( [ tradeDate, dataLow9 ] )
            
        if dataHigh8 > dataHigh6:
            tradeDate = data8[ 0 ]
            dataLow8 = data8[ 3 ]
            sellPoint.append( [ tradeDate, dataLow8 ] )

        return sellPoint