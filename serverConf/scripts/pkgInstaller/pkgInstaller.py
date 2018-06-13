import os


def installPackagesFromNet():
        #Installing needed packages
        packages="apache2 python2.7 libapache2-mod-wsgi  mysql-server python-mysqldb python-passlib python-requests postfix telnet telnetd libmilter-dev libssl-dev openssl opendkim opendkim-tools vde2 uml-utilities openssh-server"
        for pkg in packages.split():
		os.system("apt-get install "+pkg+" -y")
		os.system("rm /var/cache/apt/archives")

def installPackages():
    #Installing needed packages
    os.system("dpkg -R --install data/pkgs/apache2")
    os.system("dpkg -R --install data/pkgs/python")
    os.system("dpkg -R --install data/pkgs/opendkim")
    os.system("dpkg -R --install data/pkgs/openssh-server")
    os.system("dpkg -r --force-depends exim4-daemon-light")
    os.system("dpkg -R --force-conflicts --install data/pkgs/postfix")
    ls=range(1,36)
    for pre in ls:
        fname=str(pre)+".deb"
        os.system("dpkg -i data/pkgs/mysql/"+fname)

