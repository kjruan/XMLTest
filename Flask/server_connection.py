import pymssql

server = "vmsfgce"
user = "advent\kruan"
password = "Advent66"

conn = pymssql.connect(server, user, password, "repdb")

cursor = conn.cursor(as_dict=True)

cursor.execute(""" select * from dbo.engineers """)

for row in cursor:
	print("Active: %s" % row["active"], row["NetworkID"])

conn.close()