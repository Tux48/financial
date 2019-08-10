// macd 值
function macd( deaValue, diffValue ) {
	macdValue = ( diffValue - deaValue ) * 2
	return macdValue.toFixed( 2 )
}

// 当前的 ema值
function todayEma( yesterdayEma12, yesterdayEma26, todayClose ) {
    ema12 = yesterdayEma12 * 11 / 13 + todayClose * 2 / 13
    ema26 = yesterdayEma26 * 25 / 27 + todayClose * 2 / 27
    
    return {
    	ema12: ema12,
    	ema26: ema26
    }
}

// 开盘的第一个ema值
function openEma( yesterdayClose, todayClose ) {
    ema12 = yesterdayClose * 11 / 13 + todayClose * 2 / 13
    ema26 = yesterdayClose * 25 / 27 + todayClose * 2 / 27
    
    return {
    	ema12: ema12,
    	ema26: ema26
    }
}

// 计算diff
function diff( ema12, ema26 ) {
    diffValue = ema12 - ema26
    
    return diffValue.toFixed( 2 )
}

// 计算dea数据
function dea( diffValue, yesterdayDea ) {
    deaValue = ( yesterdayDea * 8 / 10 ) + ( diffValue * 2 / 10 )
 
    return deaValue.toFixed( 2 )
}

// 计算
function computeMacd( datas ) {
    allMacd = [ 0.0 ]
	allDiff = [ 0.0 ]
	allDea = [ 0.0 ]
	
	//第一天:    由于刚上市所以5个参数均为0.
	//第二天:    EMA(12)=今天收盘价*2/13 + 前天收盘价*11/13
	//              EMA(26)=今天收盘价*2/27 + 前天收盘价*25/27
	
    yesterdayClose = datas[ 0 ][ 1 ]	// 昨天收盘价
    todayClose = datas[ 1 ][ 1 ]	// 今天收盘价
	
    yesterdayEmaData = openEma( yesterdayClose, todayClose )
	yesterdayEma12 = yesterdayEmaData.ema12
	yesterdayEma26 = yesterdayEmaData.ema26
	
	yesterdayDiff = diff( yesterdayEma12, yesterdayEma26 )
	allDiff.push( yesterdayDiff )
	
	yesterdayDea = dea( yesterdayDiff, 0 )
	allDea.push( yesterdayDea )
	
	yesterdayMacd = macd( yesterdayDiff, yesterdayDea )
	allMacd.push( yesterdayMacd )
	
	for( var i = 2; i < datas.length; i++ ) {
	    
	    todayClose = datas[ i ][ 1 ]
	    
	    todayEmaData = todayEma( yesterdayEma12, yesterdayEma26, todayClose )
	    
	    diffValue = diff( todayEmaData.ema12, todayEmaData.ema26 )
	    deaValue = dea( diffValue, yesterdayDea )
	    macdValue = macd( deaValue, diffValue )
	    
	    allMacd.push( macdValue )
	    allDiff.push( diffValue )
	    allDea.push( deaValue )
	    
	    yesterdayEma12 = ema12
	    yesterdayEma26 = ema26
	    yesterdayDea = deaValue
	}

    return {
		allMacd: allMacd,
		allDiff: allDiff,
		allDea: allDea
	}
    
}