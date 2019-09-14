import os
import subprocess
from dracclient import client
import logging
import urllib3
import datetime

urllib3.disable_warnings()

logging.basicConfig()
six_ten = '10.0.14.200'
seven_ten = '10.0.14.210'
sixten = client.DRACClient(six_ten, 'root', 'Annkz+319331')
seventen = client.DRACClient(seven_ten, 'root', 'Annkz+319331')

def check_server(server):
    test = server.get_power_state()
    if test == 'POWER_ON':
        print("Servers are powered on")
        return True
    elif test == 'POWER_OFF':
        print("Servers are powered off")
        return False
current_hour = datetime.datetime.now().hour
current_min = datetime.datetime.now().minute
print("The Time is " + str(current_hour) + ":" + str(current_min))
if current_hour == 0 and current_min == 30:
    if check_server(sixten) == True:
        print("Turning off Servers")
        sixten.set_power_state("POWER_OFF")
    if check_server(seventen) == True:
        seventen.set_power_state("POWER_OFF")
if current_hour == 20:
    if check_server(sixten) == False:
        print("Turning on Servers")
        sixten.set_power_state("POWER_ON")
    if check_server(seventen) == False:
        seventen.set_power_state("POWER_ON")
