var fs = require('fs');
var xml2js = require('xml2js');
var output = '';
var parser = new xml2js.Parser(); 

var getDataSetCommandText = function (rdl) {
	var datasets = rdl.Report.DataSets[0].DataSet;
	var output = datasets.map(function (dataset) {
		var dic = {};
		var name = dataset['$'].Name;

		dic[name] = getSpecifcAPXFunctions(dataset.Query[0].CommandText);
		return dic;
	})
	return output;
}

var getSpecifcAPXFunctions = function (query) {
	var regex = /APXUser(.\w+)(.\w+)(?!..\s)/gi;
	var output = query.map(function (str) {
		return str.match(regex);
	})
	return output
}

function print(collection) {
	for (var i in item) {
		console.log(i + " " + item[i]);
	}
}

function analyzeDataSet(collection, callback) {
	for (var i = 0; i < collection.length; i++) {
		callback(collection[i]);
	}
}

fs.readFile(__dirname + '/B29883SASubreport.rdl', function (err, data) {
	parser.parseString(data, function (err, result) {
		var collection = getDataSetCommandText(result);
		//output = result.Report.DataSets[0].DataSet[0].Query[0].CommandText; 
		analyzeDataSet(collection, print);
	});
});


