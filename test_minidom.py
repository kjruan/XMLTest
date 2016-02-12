import re, json
from xml.dom import minidom

def GetReportObjectAttrs(node):
	objSet = {}
	for c in node.childNodes:
		if (c.nodeType == 1 and c.tagName == 'DataSetName'):
			objSet["DataSet"] = c.firstChild.data
	objSet["Type"] = node.localName
	objSet["Name"] = node.attributes['Name'].value
	return objSet


fileName = 'B29883SASubreport.rdl'
#fileName = '/Volumes/gce/Client/2423 - PMFA/APX Reports/E2423SA/E2423SA_WMR.rdl'
xmldoc = minidom.parse(fileName)

repItems = xmldoc.getElementsByTagName('ReportItems')
parameters = xmldoc.getElementsByTagName('ReportParameter')
datasets = xmldoc.getElementsByTagName('DataSet')
pattern = re.compile(r"APXUser[.\w]+", re.IGNORECASE)

rdl = {}
datasetObj = {}
paramList = []
objList = []
objSetArray = []

# Get Report Objects
for item in repItems:
	dataSetName = item.getElementsByTagName('DataSetName')
	for child in item.childNodes:
		if (child.localName == 'Chart'): #== 'Tablix':
			objList.append(GetReportObjectAttrs(child))	
		if (child.localName == 'Tablix'):
			objList.append(GetReportObjectAttrs(child))	

#Get parameters
for parameter in parameters:
	pName = parameter.attributes['Name'].value
	paramList.append(pName)

#Get Dataset names
for dataset in datasets:
	dsName = dataset.attributes['Name'].value	
	query = dataset.getElementsByTagName('Query')
	for node in query:
		commandText = node.getElementsByTagName('CommandText').item(0).firstChild.data
		datasetObj[dsName] = list(set(re.findall(pattern, commandText)))

#Get Report Object Fields 
# for obj in objList:
# 	for dataset in datasets:
# 		if (dataset.attributes['Name'].value == obj["DataSetName"]):
# 			fields = dataset.getElementsByTagName('Field')
# 			for field in fields:
# 				obj["Fields"].append(field.attributes['Name'].value)

rdl["FileName"] = 'Test'
rdl["DateCreated"] = 'Test'
rdl["LastUpdated"] = 'Test'
rdl["ReportOjects"] = objList
rdl["Parameters"] = paramList
rdl["DataSets"] = datasetObj
rdl["TotalHours"] = 0

data_string = json.dumps(rdl, indent=4)

print(data_string)
