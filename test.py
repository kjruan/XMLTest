import os, time, pymongo
from RDLParser import RDLParser
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['rdltest']
collection = db['rdls']

# fileName = 'B29883SASubreport.rdl'
# output = RDLParser(fileName).GetOuputfromRDL()
# rdls_id = collection.insert_one(output).inserted_id


for dirpath, dirs, files in os.walk("C:\Test\XMLTest\Client"):
	for file in files:
		if file.endswith(".rdl"):
			info = os.stat(dirpath)
			# print(os.path.abspath(os.path.join(dirpath, file)))
			# print(time.strftime(file + " Modified Date: %m/%d/%y", time.localtime(info.st_mtime)))

			output = RDLParser(os.path.abspath(os.path.join(dirpath, file))).GetOuputfromRDL()
			collection.insert_one(output)