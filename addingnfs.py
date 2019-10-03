#adding nfs to all servers

import subprocess
import parser
import apt
import os

cache = apt.Cache()

checking_distro = subprocess.run(['cat', '/etc/os-release']) 
print(checking_distro)

def ubuntu_install():    
    print("OS is Ubuntu")
    if cache['nfs-common'].is_installed:
        print("nfs-common is Installed Already")
    else:
        print("nfs-common needs to be installed. Installing..")
        subprocess.run(['apt', 'install', 'nfs-common'])

   
if (checking_distro == "ubuntu"):
    ubuntu_install()
print("Making dir nfs-homedir")
os.mkdir("~/nfs-homedir", 755)

print("Adding mounting point in /etc/fstab")
subprocess.run("echo '10.0.14.100:/home/nickshorter ~/nfs-homedir nfs default 0 0' >> /etc/fstab", shell=True)

print("Process Complete")
exit(0)