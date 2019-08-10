function splitData(rawData) {
       		
	var categoryData = [];
	var values = [];
	var volumes = [];
       		
	for (var i = 0; i < rawData.length; i++) {
		categoryData.push(rawData[i].splice(0, 1)[0]);
		values.push(rawData[i]);
		volumes.push([i, rawData[i][4], rawData[i][0] > rawData[i][1] ? 1 : -1]);
	}
    
	return {
		categoryData: categoryData,
		values: values,
		volumes: volumes
	};
}