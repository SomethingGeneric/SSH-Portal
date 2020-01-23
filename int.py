import os
from time import sleep

def pstr(str):
	words = str.split(" ")
	for word in words:
		sp = word.split()
		for c in sp:
			print(c,end="")
			sleep(0.1)
		print(" ",end="")
		sleep(0.2)
	sleep(0.5)
	print()

rf = os.listdir()
print("Options:")
for file in rf:
	if ".mv" in file:
		print(" - " + file.replace(".mv",""))

fn = input("File choice: ") + ".mv"

print('\033[2J')
print('\033[0;0H')

if os.path.exists(fn):
	with open(fn) as f:
		lines = f.read().split("\n")
	for line in lines:
		pstr(line)
else:
	print("No such choice: " + fn)
	print("Exiting.")	
