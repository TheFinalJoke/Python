from dracclient import client
import urllib3
urllib3.disable_warnings()

sixten = client.DRACClient('10.0.14.200', 'root', 'Annkz+319331')
seventen = client.DRACClient('10.0.14.210', 'root', 'Annkz+319331')

print("Turning Off Servers")
sixten.set_power_state("POWER_OFF")
seventen.set_power_state("POWER_OFF")

