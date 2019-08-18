import sys, subprocess
import wakeonlan

pinganswer = subprocess.check_output("ping -c 1 8.8.8.8")
print(pinganswer)
