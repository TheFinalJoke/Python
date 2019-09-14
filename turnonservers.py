from dracclient import client
import urllib3
urllib3.disable_warnings()

sixten = client.DRACClient('ip', 'user', 'password')
seventen = client.DRACClient('ip', 'user', 'password')

print("Turning on Servers")
sixten.set_power_state("POWER_ON")
seventen.set_power_state("POWER_ON")


