import os
import dracclient
client = dracclient.wsman.Client(idrac610.homelab,root,Annkz+319331,port=443)


def check_host(host):
    pinganswer = os.system("ping -c 1 > /dev/null " + host)
    if pinganswer != 0:
        return False
    else: 
        return True


if check_host("1.1.1.1") == True:
    print(client.get_power_state())

