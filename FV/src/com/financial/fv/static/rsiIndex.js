function computeRsi( datas, periods1 = 6, periods2 = 12, periods3 = 24 ) {
    var rsi1 = RSI( datas, periods1 )
    var rsi2 = RSI( datas, periods2 )
    var rsi3 = RSI( datas, periods3 )

    return {
    	rsi1: rsi1,
    	rsi2: rsi2,
    	rsi3: rsi3
    }
}

function RSI( datas, periods ) {
    
    var rsies = new Array()
    // 数据长度不超过周期，无法计算；
    if( datas.length <= periods ) {
        return rsies
    }
    
    for( var index = 0; index < datas.length; index++ ) {
        rsies.push( 0.0 )
    }
        
    // 用于快速计算；
    var up_avg = 0
    var down_avg = 0

    // 首先计算第一个RSI，用前periods+1个数据，构成periods个价差序列;
    for( var i = 1; i <= periods; i++ ) {
        // 价格上涨;
        if( datas[ i ][ 1 ] >= datas[ i-1 ][ 1 ] ) {
            up_avg += datas[ i ][ 1 ] - datas[ i-1 ][ 1 ]
        // 价格下跌;
        } else {
            down_avg += datas[ i-1 ][ 1 ] - datas[ i ][ 1 ]
    	}
	}
            
    up_avg = up_avg / periods
    down_avg = down_avg / periods
    rs = up_avg / down_avg
    rsies[ periods ] = ( 100 - 100 / ( 1 + rs ) ).toFixed( 2 )

    // 后面的将使用快速计算；
    for( var j = periods+1; j < datas.length; j++ ) {
        var up = 0
        var down = 0
        if( datas[ j ][ 1 ] >= datas[ j-1 ][ 1 ] ) {
            up = datas[ j ][ 1 ] - datas[ j-1 ][ 1 ]
            down = 0
        } else {
            up = 0
            down = datas[ j-1 ][ 1 ] - datas[ j ][ 1 ]
        }
        
        // 类似移动平均的计算公式;
        up_avg = ( up_avg * ( periods - 1 ) + up ) / periods
        down_avg = ( down_avg * ( periods - 1 ) + down ) / periods
        rs = up_avg / down_avg
        rsies[ j ] = ( 100 - 100 / ( 1 + rs ) ).toFixed( 2 )
    }
        
    return rsies
}