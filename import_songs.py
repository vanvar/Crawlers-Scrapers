import shutil
from os import path, remove, listdir
from os.path import basename

src = 'C:\Users\HP\Downloads\Music'
dst = 'C:\Users\HP\Music'

files = listdir(src)
if(files == []):
	print '\nNo new song found!\nTime to download some.'
for file in files:
	if path.isfile(path.join(dst, file)):
		remove(path.join(src, file))
		print '\n[' + basename(file) + ']' + ' already in ' + '[' + basename(dst) + ']' + '\nDeleted from ' + src
	else:
		shutil.move(path.join(src, file), path.join(dst, file))
		print '\n[' + basename(file) + ']' + ' moved to ' + '[' + basename(dst) + ']'		