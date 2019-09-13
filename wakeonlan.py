import os
import subprocess
from dracclient import client
import logging
import urllib3
urllib3.disable_warnings()

logging.basicConfig()
six_ten = '10.0.14.200'
client = client.DRACClient(six_ten, 'root', 'Annkz+319331')


def check_host(host):
    args = ["ping" , "-c 1", host]
    pinganswer = subprocess.run(args, capture_output=True)
    if pinganswer.returncode != 0:
        return False
    else: 
        return True

if check_host("10.0.14.218") == False:
    print("Host is not pingable")
else:
   print(client.get_power_state())


