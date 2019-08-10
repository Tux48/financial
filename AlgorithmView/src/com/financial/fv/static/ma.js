function calculateMA(dayCount, data) {
	var result = [];
    
	for (var i = 0, len = data.values.length; i < len; i++) {
		if (i < dayCount) {
			result.push('-');
			continue;
		}
       		    
		var sum = 0;
		for (var j = 0; j < dayCount; j++) {
			sum += data.values[i - j][1];
		}
       	
		result.push(+(sum / dayCount).toFixed(3));
	}

	return result;
}