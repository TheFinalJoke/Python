import sys
import os

if(len(sys.argv) != 2):
    print("Must have 1 argument")
    exit(1)

input = str(sys.argv[1])

networking = os.system("ping -c 1 " + input)

if networking == 0:
    print("Can reach " + input)
    exit(0)
else:
    print("Can not reach" + input)
    exit(1)
