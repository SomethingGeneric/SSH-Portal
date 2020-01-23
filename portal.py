import os
import colorama
from termcolor import colored, cprint

# START CONFIG

project_path = "/home/guest/SSH-Portal"
banner_path = "banner"
server_name = "Matt's Server"
admin_email = "matt@mattcompton.me"

# END CONFIG

colorama.init()

r = colorama.Fore.RED
res = colorama.Style.RESET_ALL

if os.getcwd() != project_path:
	os.chdir(project_path)

with open(banner_path) as f:
	mb = f.read()

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
	print(r + "No commands file. Please email " + admin_email + res)
	exit()

while 1==1:

	print('\033[2J')
	print('\033[0;0H')

	#print("Welcome to " + server_name)
	print(mb)
	print("Here's your choice of actions!")
	for command in commands:
		if command != "cs":
			print("- " + command + " : " + desc[command])
		else:
			cprint("- cs : " + desc[command], 'red', attrs=['blink'])
	print("- exit")
	print()
	choice = input("> ")
	if choice in commands:
		do = commands[choice]
		ds = do.split(" ")
		if ds[0] == "python3" and "wr" not in do:
			if os.path.exists(ds[1]):
				os.system(do)
			else:
				print(r + "No such script file: " + do + ". This is an error. Please email " + admin_email + res)
				input("Press enter to return to home screen.")
		else:
			#print("Non-python")
			os.system(do)
	elif choice == "exit":
		print(colorama.Fore.GREEN + "Bye!" + res)
		exit()
	else:
		print(r + "No such option " + choice + res)
		input("Press enter to return to home screen.")
