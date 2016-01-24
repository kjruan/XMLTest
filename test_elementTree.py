import xml.etree.ElementTree as ET

tree = ET.parse('/Volumes/gce/Client/2423 - PMFA/APX Reports/E2423SA/E2423SA_WMR.rdl')
root = tree.getroot()

ns = {'report_definition': 'http://schemas.microsoft.com/sqlserver/reporting/2008/01/reportdefinition',
			'report_design': 'http://schemas.microsoft.com/SQLServer/reporting/reportdesigner'}

for child in root:
	for c in child:
		if c.tag == '{http://schemas.microsoft.com/sqlserver/reporting/2008/01/reportdefinition}DataSet':
			print(c.attrib['Name'])
			queries = c.findall('{http://schemas.microsoft.com/sqlserver/reporting/2008/01/reportdefinition}Query')
			for query in queries:
				for elem in query:
					if elem.tag == '{http://schemas.microsoft.com/sqlserver/reporting/2008/01/reportdefinition}CommandText':
						print(elem.text)
