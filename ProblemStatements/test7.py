"""
THe code creates a file, that tells the size of all the folders within the python script location.

"""
import os
from collections import defaultdict

base_directory = os.getcwd()
out_fl_path = os.path.join(os.getcwd(),'myoutput.csv')

fldrs = defaultdict(lambda : 0)
for i in os.walk( base_directory, topdown=True ):
	fldrs[ root ] += sum([os.path.getsize(os.path.join(i[0],j)) for j in i[2]])

with open( out_fl_path, 'w' ) as f:
	f.write('FolderName,SizeInBytes\n')
	for i in fldrs:
		f.write('%s,%s\n' %(i,fldrs[i]))
