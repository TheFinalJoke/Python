import sys, os
from wakeonlan import send_magic_packet

def check_host(host):
    pinganswer = os.system("ping -c 1 > /dev/null " + host)
    if pinganswer != 0:
        return False
    else: 
        return True


if check_host("1.1.1.1") == True:
    send_magic_packet('B8:27:EB:E9:BB:9F')