import os
import sys

import fnmatch
import shutil

matches = []
for root, dirnames, filenames in os.walk('.'):
    for filename in fnmatch.filter(filenames, '*.mp4'):
    	root1 = root.split('\\')[-1]
    	print(root1)
    	matches.append(os.path.join(root, filename))
    	os.rename(os.path.join(root, filename), root1+'.mp4')
    	# shutil.move(os.path.join(root, root1+'.mp4'), os.getcwd())