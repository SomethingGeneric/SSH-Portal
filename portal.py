import os

import colorama

from termcolor import colored, cprint

colorama.init()

r = colorama.Fore.RED
res = colorama.Style.RESET_ALL

if os.getcwd() != "/home/guest/SSH-Portal":
	os.chdir("/home/guest/SSH-Portal")

commands = {}
desc = {}

if os.path.exists("commands.txt"):
	with open("commands.txt") as f:
		raw = f.read()
	lines = raw.split("\n")
	for line in lines:
		data = line.split(":")
		commands[data[0]] = data[1]
		desc[data[0]] = data[2]
else:
	print(r + "No commands file. Please email matt@mattcompton.me" + res)
	exit()

while 1==1:

	print('\033[2J')
	print('\033[0;0H')

	print("Welcome to Matt's server!")
	print("Here's your choice of actions!")
	for command in commands:
		if command != "cs":
			print("- " + command + " : " + desc[command])
		else:
			cprint("- cs : " + desc[command], 'red', attrs=['blink'])
	print("- exit")
	choice = input("> ")
	if choice in commands:
		do = commands[choice]
		ds = do.split(" ")
		if ds[0] == "python3" and "wr" not in do:
			if os.path.exists(ds[1]):
				os.system(do)
			else:
				print(r + "No such script file: " + do + ". This is an error. Please email matt@mattcompton.me" + res)
				input("Press enter to return to home screen.")
		else:
			#print("Non-python")
			os.system(do)
	elif choice == "exit":
		exit()
	else:
		print(r + "No such option " + choice + res)
		input("Press enter to return to home screen.")
