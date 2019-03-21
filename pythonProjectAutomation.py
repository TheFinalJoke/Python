#Written and Tested by: Nick Shorter and Landon Hise

import os
import sys

userID = os.geteuid()
#Checking if user is root
if userID != 0:
    print("Only root can execute")
    print("Exiting Script...")
    exit(1)
#Checking if has only one argument
if len(sys.argv) != 2:
    print("This Script only accepts one argument, The username of the node")
    print("Example: python projectAutomation.py workernodeN")
    print("Exiting Script...")
    exit(1)

#installing Sudo
print("STATUS Installing Sudo")
os.system("sleep 3s")

os.system("apt install sudo -y")

#Creating user Master
print("STATUS: Creating User Master")
os.system("sleep 3s")
master = "master:master"
os.system("useradd -m master")
os.system("echo " + master + " | chpasswd")

#adding workernodeN to sudoers file
print("STATUS: Granting " + sys.argv[1] + " and master to sudoers file")
os.system("sleep 3s")
os.system('echo "#Giving " ' + sys.argv[1] + ' "and Master sudo privileges" >> /etc/sudoers')
os.system('echo ' + sys.argv[1] + '" ALL=(ALL:ALL) ALL" >> /etc/sudoers')
os.system('echo "master ALL=(ALL:ALL) ALL" >> /etc/sudoers')

#exporting PATH to bash_profile
print("STATUS: EXPORTING PATH")
os.system("sleep 3s")
os.system('echo "export PATH=/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin" >> ~/.bash_profile')

#Installing net-tools
print("STATUS: Install Net-tools")
os.system("sleep 3s")
os.system("apt install net-tools -y")

#Installing NFS
print("STATUS: Installing NFS and making NFS Directory")
os.system("sleep 3s")
os.system("apt install nfs-common -y")
os.system("mkdir /nfsshare")
os.system("chmod 777 /nfsshare")
os.system("echo '192.168.0.20:/nfsshare /nfsshare nfs defaults' >> /etc/fstab")

#Installing JTR And Dependencies
#Installing Rexgen
print("STATUS: Installing Rexgen and JTR")
os.system("sleep 3s")
os.system("apt update -y")
os.system("apt install build-essential libssl-dev yasm libgmp-dev libpcap-dev libnss3-dev -y")
os.system("apt install libkrb5-dev pkg-config libopenmpi-dev openmpi-bin zlib1g-dev libbz2-dev -y")
os.system("apt install flex cmake bison git -y")

print("STATUS: Installing Rexgen")
os.system("sleep 3s")
os.chdir("/usr/local")
os.system("git clone https://github.com/teeshop/rexgen.git")
os.chdir("/usr/local/rexgen")
os.system("./install.sh")
os.system("ldconfig")

#Installing JTR
print("STATUS: Installing JTR")
os.system("sleep 3s")
os.chdir("/usr/local")
os.system("git clone https://github.com/magnumripper/JohnTheRipper.git")
os.system("chmod 777 -R /usr/local/JohnTheRipper")
os.chdir("/usr/local/JohnTheRipper/src")
os.system("./configure --enable-mpi")
os.system("make -s clean && make -sj4")
os.chdir("/usr/local/JohnTheRipper/run/")
os.system("./john --test")
exit(0)