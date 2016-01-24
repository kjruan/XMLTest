import re, json
from xml.dom import minidom

fileName = '/Volumes/gce/Client/2423 - PMFA/APX Reports/E2423SA/E2423SA_WMR.rdl'
xmldoc = minidom.parse(fileName)
datasets = xmldoc.getElementsByTagName('DataSet')
pattern = re.compile(r"APXUser[.\w]+", re.IGNORECASE)
rdl = {}
datasetObj = {}

for dataset in datasets:
	dsName = dataset.attributes['Name'].value	
	query = dataset.getElementsByTagName('Query')
	for node in query:
		commandText = node.getElementsByTagName('CommandText').item(0).firstChild.data
		datasetObj[dsName] = list(set(re.findall(pattern, commandText)))

rdl["FileName"] = 'Test'
rdl["DataSets"] = datasetObj

data_string = json.dumps(rdl, indent=4)

print(data_string)
