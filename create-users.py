import os, crypt
import sys

userID = os.geteuid()

if userID != 0:
    print("Only Root can execute")
    exit(1)
if len(sys.argv) != 3:
    print("You must have 2 Arguments")
    exit(1)

arg1 = sys.argv[1]
arg2 = sys.argv[2]
path = "/home/" + arg1

checking = os.path.isdir(path)

if checking == False:
    os.system("mkdir -p " + path)

for var in range(1, int(arg2)):
	os.system("useradd -d " + path + " " + arg1)
exit(0)
