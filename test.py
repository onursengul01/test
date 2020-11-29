import os.path
import sys
path = '/usr/bin/TheFatRat'
gitRepo = 'https://github.com/Screetsec/TheFatRat'

if os.getuid() != 0:
	print("Sorry, this script requires sudo privledges")
	sys.exit()

#if os.path.exists(path):
 	#print("settolkit is ready to use")
#else:
	#while True:
print("TheFatRat is not found in the system...")
option = input("Would you like to install TheFatRat? 'y' or 'n': ")
if option == "y":
	os.system(f"git clone {gitRepo} /usr/bin/" )
	os.system(f"cd {path}")
	os.system("sudo bash setup.sh")


if option == "n":
	print("bye")
	
