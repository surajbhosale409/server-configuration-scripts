Hello,
    This script is for configuring newly installed server to meet our following requirements:

        [1] Packages should be installed:    
            [ apache2, python2.7, libapache2-mod-wsgi, mysql-server, python-mysqldb, python-passlib, python-requests,
                postfix, opendkim, telnetd, libmilter-dev, libssl-dev, openssl]
        
        [2] Configure and set up http (apache2/httpd server with python and mod-wsgi)

        [3] Configure and set up smtp (postfix-esmtp server)

        [4] Configure and set up opendkim for postfix (DomainKeys Identified Mail)
        
        [5] Make entry of ip and domain in /etc/hosts

        [6] Set appropriate hostname to the server

    This are the tasks needed to be done before deployment of software.
    
    So we have provided python script named "serverConf.py".
    Before running the script you should provide IP addresses and Domains in file named "ipDomain" in same directory.
    
    [Example: content of ipDomain]
    =>127.0.0.1  yourdomain.com
    
    Now run [must be run with root priviledges]: sudo python serverConf.py 


    Tree structure of scripts:
    
    .
    ├── data
    │   ├── opendkim.conf
    │   └── packagesToRemove
    ├── ipDomain
    ├── README.md
    ├── scripts
    │   ├── hostsSpfSetup
    │   │   ├── hostsSpfSetup.py
    │   │   └── hostsSpfSetup.pyc
    │   ├── ipDomainReader
    │   │   ├── ipDomainReader.py
    │   │   └── ipDomainReader.pyc
    │   ├── modWSGI
    │   │   ├── modWSGI.py
    │   │   └── modWSGI.pyc
    │   ├── opendkim
    │   │   ├── opendkim.py
    │   │   └── opendkim.pyc
    │   ├── pkgInstaller
    │   │   ├── pkgInstaller.py
    │   │   └── pkgInstaller.pyc
    │   ├── pkgRemover
    │   │   ├── pkgRemover.py
    │   │   └── pkgRemover.pyc
    │   ├── postfix
    │   │   ├── postfix.py
    │   │   └── postfix.pyc
    │   ├── reverseProxy
    │   │   ├── data
    │   │   │   ├── 000-default.conf
    │   │   │   └── default-site.conf
    │   │   └── reverseProxy.py
    │   └── sslSetup
    │       ├── ssl-params.conf
    │       └── sslSetup.py
    └── serverConf.py

