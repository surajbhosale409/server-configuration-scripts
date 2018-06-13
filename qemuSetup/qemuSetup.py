import os,sys,getpass

if getpass.getuser()!="root":
    print "Needs root privileges"
    sys.exit()

def sambaSetup():
    os.system("dpkg -R --install data/pkgs/samba/")
    os.system("dpkg -R --install data/pkgs/samba-client/")
    os.system("cp data/smb.conf /etc/samba/smb.conf")
    os.system("rm /lib/systemd/system/samba.service && sudo systemctl enable samba.service nmbd.service && sudo systemctl start samba")

def firstTimeSetup():
    cwd=os.getcwd()
    os.system("qemu-img create /vserver.img 1.5G")
    os.chdir("/")
    os.system("sudo qemu-system-x86_64 -boot d -cdrom "+cwd+"/data/debian9.iso -m 1024 -hda /vserver.img -enable-kvm")
    os.chdir(cwd)
    #sambaSetup()

def copy():
    os.system("cp data/vserver.img /vserverCopy.img")

def setup():

    print "Install qemu (Offline installation) [y/N]?"
    if raw_input().lower()=="y":
        os.system("dpkg -R --install data/pkgs/qemu")

    print "Setup new image / Make copy of existing image (New/Copy) [N/C]?"
    if raw_input()=="N":
        firstTimeSetup()
    else:
        copy()

setup()
