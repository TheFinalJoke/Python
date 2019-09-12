import os
import subprocess
from dracclient import client
import logging
#from wakeonlan import send_magic_packet
logging.basicConfig()
six_ten = '10.0.14.200'
client = client.DRACClient(six_ten, 'root', 'Annkz+319331')


def check_host(host):
    args = ["ping" , "-c 1", host]
    pinganswer = subprocess.run(args, strout=devnull)
    print(pinganswer.returncode)
    #if pinganswer != 0:
    #    print(pinganswer)
  #      return False
  #  else: 
  #      return True

check_host('0.0.0.0')
#if check_host("1.1.1.1") == True:
  #  print(client.get_power_state())
#else:
   # print("host not in pingable")


