import sys, os
import wakeonlan

def check_host(host):
    pinganswer = os.system("ping -c 1 > /dev/null " + host)
    if pinganswer != 0:
        return False
    else: 
        return True


if check_host("1.1.1.1") == True:
    
