def search(x):
	users = [] # All the filenames that include 
	direc = '.'
	import os
	filenames = os.listdir(direc)
	for name in filenames:
		if x in name:
			users.append(name)
	return users
print(search("y"))