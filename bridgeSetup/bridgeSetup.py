import os,sys,getpass

if getpass.getuser()!="root":
    print "Needs root privileges"
    sys.exit()


def bridgeHostSetup():
    os.system("dpkg -R --install data/pkgs/")
    os.system("cp /etc/network/interfaces data/temp")
    os.system("cat data/temp data/host > /etc/network/interfaces")
    os.system("rm data/temp")
    os.system("mkdir -p /etc/qemu")
    os.system("cp data/bridge.conf /etc/qemu/bridge.conf")
    os.system("brctl addbr br0")
    os.system("service networking restart")

def bridgeGuestSetup():
    os.system("cp /etc/network/interfaces data/temp")
    os.system("cat data/temp data/guest > /etc/network/interfaces")
    os.system("sed -i 's/dhcp/static/' /etc/network/interfaces")
    os.system("rm data/temp")
    os.system("service networking restart")
    os.system("reboot")

def bridgeSetup():
    print "Setup(Host/Guest) [H|G]?"
    if raw_input()=="H":
        bridgeHostSetup()
    else:
        bridgeGuestSetup()

bridgeSetup()
