import subprocess
import random
import os

path=""
try:
	temp = raw_input("Drive(C,E,F) : ")
except:
	print "No such drive or drive not ready..."
#print '\n' #2 new lines, one by print and other by '\n'
print #new line itself
path += (temp + ":/")
found = False
while found == False: 
	print "Path : " + path
	print
	list = os.listdir(path)
	for file in list:
		#if os.path.isdir(os.path.join(path, file)):
		print file
	print 
	flag = False
	while flag == False:
		temp = raw_input("Folder : ")
		if os.path.isdir(os.path.join(path, temp)):
			flag = True
			temp2 = raw_input("Target Folder(y/n) : ")
			if temp2 == "y":
				found = True
			path += (temp + "/")
		else:
			print "No such folder in " + path
base = path
while True:
	video = random.choice(os.listdir(path))
	path += video
	p = subprocess.Popen(["C:/Program Files/VideoLAN/VLC/vlc.exe","file:///"+path])
	raw_input("Shuffle...")
	p.terminate()
	path = base
'''while flag == False:
	temp = raw_input("Folder : ")
	if os.path.isdir(os.path.join(path, temp)):
		path += (temp + "/")
		flag = True
	elif os.path.isfile(os.path.join(path, temp)):
		flag = True
		found = True
		path += temp
		print path
		p = subprocess.call(["C:/Program Files/VideoLAN/VLC/vlc.exe","file:///"+path])
	else:
		print "No such folder in " + path'''


	