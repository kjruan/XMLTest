import os
for dirpath, dirs, files in os.walk("/Volumes/gce/Client"):
	for file in files:
		if file.endswith(".rdl"):
			print(file)