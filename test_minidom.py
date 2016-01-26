import re, json
from xml.dom import minidom

fileName = '/Volumes/gce/Client/2423 - PMFA/APX Reports/E2423SA/E2423SA_WMR.rdl'
xmldoc = minidom.parse(fileName)

repItems = xmldoc.getElementsByTagName('ReportItems')
parameters = xmldoc.getElementsByTagName('ReportParameter')
datasets = xmldoc.getElementsByTagName('DataSet')
pattern = re.compile(r"APXUser[.\w]+", re.IGNORECASE)
rdl = {}
datasetObj = {}
paramList = []
objList = []
objSet = {}




for item in repItems:
	for child in item.childNodes:
		if child.localName == 'Tablix':
			print(child.attributes['Name'].value)
	dataSetName = item.getElementsByTagName('DataSetName')
	if(dataSetName.item(0)):
		objList.append(dataSetName.item(0).firstChild.data)

for parameter in parameters:
	pName = parameter.attributes['Name'].value
	paramList.append(pName)

for dataset in datasets:
	dsName = dataset.attributes['Name'].value	

	query = dataset.getElementsByTagName('Query')
	for node in query:
		commandText = node.getElementsByTagName('CommandText').item(0).firstChild.data
		datasetObj[dsName] = list(set(re.findall(pattern, commandText)))

for obj in objList:
	for dataset in datasets:
		if (dataset.attributes['Name'].value == obj):
			fields = dataset.getElementsByTagName('Field')
			for field in fields:
				print(field.attributes['Name'].value)

rdl["FileName"] = 'Test'
rdl["Parameters"] = paramList
rdl["DataSets"] = datasetObj
rdl["TotalHours"] = 0

data_string = json.dumps(rdl, indent=4)

print(data_string)
