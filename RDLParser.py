import re, json, os, time
from xml.dom import minidom

class RDLParser(object):
	'Common base class for RDL to JSON parsing'
	def __init__(self, rdl):
		self.fileAttrs = self.GetFileAttrs(rdl)
		self.xmldoc = minidom.parse(rdl)
		self.repItems = self.xmldoc.getElementsByTagName('ReportItems')
		self.parameters = self.xmldoc.getElementsByTagName('ReportParameter')
		self.datasets = self.xmldoc.getElementsByTagName('DataSet')
		self.pattern = re.compile(r"APXUser[.\w]+", re.IGNORECASE)

	def GetReportObject(self):
		objList = []
		for item in self.repItems:
			dataSetName = item.getElementsByTagName('DataSetName')
			for child in item.childNodes:
				if (child.localName == 'Chart'): #== 'Tablix':
					objList.append(self.GetReportObjectAttrs(child))	
				if (child.localName == 'Tablix'):
					objList.append(self.GetReportObjectAttrs(child))	
		return objList

	def GetReportParameters(self):
		paramList = []
		for parameter in self.parameters:
			pName = parameter.attributes['Name'].value
			paramList.append(pName)
		return paramList

	def GetDatasetAttributes(self):
		datasetObjs = {}
		for dataset in self.datasets:
			dsName = dataset.attributes['Name'].value	
			query = dataset.getElementsByTagName('Query')
			fields = dataset.getElementsByTagName('Fields')

			datasetObjs[dsName] = {}
			for field in fields:
				datasetObjs[dsName]["Fields"] = []
				for f in field.childNodes:
					if (f.nodeType == 1): # note type 1 = element
						datasetObjs[dsName]["Fields"].append(f.attributes['Name'].value)

			for node in query:
				commandText = node.getElementsByTagName('CommandText').item(0).firstChild.data
				datasetObjs[dsName]["StoredProcedures"] = list(set(re.findall(self.pattern, commandText)))
		return datasetObjs

	def GetOuputfromRDL(self, fileType=None):
		rdl = {}
		rdl["FileName"] = self.fileAttrs["Name"].replace(".rdl","")
		rdl["DateCreated"] = self.fileAttrs["DateCreated"]
		rdl["LastUpdated"] = self.fileAttrs["LastUpdated"]
		rdl["ReportOjects"] = self.GetReportObject()
		rdl["Parameters"] = self.GetReportParameters()
		rdl["DataSets"] = self.GetDatasetAttributes()
		rdl["TotalHours"] = 0
		return json.dumps(rdl, indent=4) if fileType == "json" else rdl

	@staticmethod
	def GetReportObjectAttrs(node):
		objSet = {}
		for c in node.childNodes:
			if (c.nodeType == 1 and c.tagName == 'DataSetName'): # note type 1 = element
				objSet["DataSet"] = c.firstChild.data
		objSet["Type"] = node.localName
		objSet["Name"] = node.attributes['Name'].value
		return objSet

	@staticmethod 
	def GetFileAttrs(filePath):
		obj = {}
		info = os.stat(filePath)
		obj["Name"] = os.path.split(filePath)[1] #tail
		obj["LastUpdated"] = time.strftime("%m/%d/%y", time.localtime(info.st_ctime))
		obj["DateCreated"] = time.strftime("%m/%d/%y", time.localtime(info.st_mtime))
		return obj


