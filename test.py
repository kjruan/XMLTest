import xml.etree.ElementTree as ET

tree = ET.parse('B29883SA.rdl')
root = tree.getroot()

ns = {'report_definition': 'http://schemas.microsoft.com/sqlserver/reporting/2008/01/reportdefinition',
			'report_design': 'http://schemas.microsoft.com/SQLServer/reporting/reportdesigner'}

for datasets in root.findall('.//report_definition:DataSet', ns):
	print(datasets.attrib['Name'])
	for dataset in datasets:
		queries = dataset.findall('report_definition:Query', ns)
		print(queries)

# for child in root:
# 	for c in child:
# 		if c.tag == '{http://schemas.microsoft.com/sqlserver/reporting/2008/01/reportdefinition}DataSet':
# 			print(c.attrib['Name'])
# 			queries = c.findall('{http://schemas.microsoft.com/sqlserver/reporting/2008/01/reportdefinition}Query')
# 			for query in queries:
# 				for elem in query:
# 					if elem.tag == '{http://schemas.microsoft.com/sqlserver/reporting/2008/01/reportdefinition}CommandText':
# 						print(elem.text)
