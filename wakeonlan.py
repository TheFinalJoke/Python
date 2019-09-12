import os
from dracclient import client

six_ten = "10.0.14.100"
client = client.DRACClient(six_ten, 'root', 'Annkz+319331', port=443)


def check_host(host):
    pinganswer = os.system("ping -c 1 > /dev/null " + host)
    if pinganswer != 0:
        return False
    else: 
        return True


if check_host("1.1.1.1") == True:
    print(client.get_power_state())

