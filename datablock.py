import numpy as np 
import json
import os



clean_dir = '/home/tk/Documents/clean/'
cleanfolder = os.listdir(clean_dir)

for i in cleanfolder:
	with open(clean_dir + '{}'.format(i)) as f:
		clean_list.append((json.load(f)))


cleanblock = np.stack(clean_list)
print (cleanblock.shape)
