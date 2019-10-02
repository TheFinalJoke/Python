#adding nfs to all servers

import subprocess
import parser

checking_distro = subprocess.run(['cat', '/etc/os-release']) 
print(checking_distro)


if (checking_distro == "ubuntu"):
    
