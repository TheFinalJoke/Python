import os
from dracclient import client
#from wakeonlan import send_magic_packet

six_ten = '10.0.14.200'
client = client.DRACClient(six_ten, 'root', 'Annkz+319331')


def check_host(host):
    pinganswer = os.system("ping -c 1 > /dev/null " + host)
    if pinganswer != 0:
        print(pinganswer)
        return False
    else: 
        return True


if check_host("1.1.1.2") == True:
    print(client.get_power_state())
else:
    print("host not in pingable")


