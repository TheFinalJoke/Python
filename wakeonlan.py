import os
import subprocess
from dracclient import client
import logging
import urllib3
import datetime

urllib3.disable_warnings()

logging.basicConfig(filename='/home/ubuntu/onoff.log', level=logging.INFO)
six_ten = 'ip'
seven_ten = 'ip'
sixten = client.DRACClient(six_ten,'user','password')
seventen = client.DRACClient(seven_ten, 'user', 'password')

def check_server(server):
    test = server.get_power_state()
    if test == 'POWER_ON':
        logging.info("Servers are powered on")
        return True
    elif test == 'POWER_OFF':
        logging.info("Servers are powered off")
        return False
current_hour = datetime.datetime.now().hour
current_min = datetime.datetime.now().minute
logging.info("The Time is " + str(current_hour) + ":" + str(current_min))
if current_hour == 0 and current_min == 30:
    if check_server(sixten) == True:
        logging.info("Turning off Servers")
        sixten.set_power_state("POWER_OFF")
    if check_server(seventen) == True:
        seventen.set_power_state("POWER_OFF")
if current_hour == 17 and current_min == 0:
    if check_server(sixten) == False:
        logging.info("Turning on Servers")
        sixten.set_power_state("POWER_ON")
    if check_server(seventen) == False:
        seventen.set_power_state("POWER_ON")
