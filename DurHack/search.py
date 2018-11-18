import os
def search(x):
	users = [] # All the filenames that include 
	direc = '.'
	filenames = os.listdir(direc)
	for name in filenames:
		if x in name:
			users.append(name)
	return users