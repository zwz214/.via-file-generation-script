# -*- coding: UTF-8 -*-
import os
path=os.path.abspath('.')
def get_filelist(dir):
	Filelist=[]
	home1=None
	#汉字
	for home, dirs, files in os.walk(path):
		for filename in files:
			if filename.endswith('.h'):        #test 汉字
				if home!=home1:
					Filelist.append('-i "'+os.path.join(home)+'"')
					home1=home					
			# Filelist.append( filename)
	return Filelist

if __name__ =="__main__":
	Filelist = get_filelist(path)	
	with open('./headerfiles.via', 'w') as f:
		for list_mem in Filelist:
			f.write(list_mem+"\n")
