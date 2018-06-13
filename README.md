Hello, 
        This are the scripts done  for virtual server's installation/image creation, VPS's networking, configuring server image to meet application requirements and deploying the application.

Following is the list and brief description about the scripts and other files:

[1] qemuSetup/       
[2] bridgeSetup/    
[3] serverConf/    
[4] deployScripts/

[1] qemuSetup/       : Script in this directory 'qemuSetup.py' is for installing qemu on host machine if needed,
from offline .deb packages. And it creates a new image or makes copy of existing qemu image.

[2] bridgeSetup/     : 'bridgeSetup.py' is script for creating the network bridge between host and guests.
Script has two setup modes. Setting up Host and setting up the guest. it installs bridge_utils on host machine
which is required for bridge . Script appends the bridge conf from 'bridgeSetup/data/host' and 'bridgeSetup/data/guest'
to the '/etc/network/interface' file and restarts networking service. And copies 'bridgeSetup/data/bridge.conf' file to 
'/etc/qemu/' which has configuration line 'allow br0' that is to allow qemu to use bridge interface 'br0'

[3] serverConf/      : 'serverConf.py' is a wrapper script which does the following configurations to setup the environment
for Forum Application. It has two modes of configuration:
    
    (1) Configure reverse proxy server: openssl, apache2 this packages are installed from offline .deb packages.
                                        Then the ssl certifcate (public and private keys) are generated to '/etc/ssl/certs'
                                        and '/etc/ssl/private/' directories.
                                        'serverConf/000-default.conf' file has the reverse proxy configuration 
                                        for both http and https. This file is copied to '/etc/apache2/sites-enabled/'
                                        File has all the configuration needed to setup the reverse proxy server as follows:
                                        
                                        For http conf, there is a proxy balancer set containing 2 balance
                                        members ( backend servers ). Out of which second one is configured as standby by
                                        specifying status=+H option. and load balancing method is set to 'byrequests'.
                                        In https conf there is some conf related to ssl such as Setting SSLEngine to be on
                                        SSLProxyEngine on. Paths to ssl certificate files are specified.

                                        After all configurations apache2 is restarted.

    (2) Backend server configuration:   apache2, mod-wsgi, python2.7, python-passlib, python-mysqldb, mysql-server,
                                        postfix, openssl, opendkim, openssh-server this packages are installed.
                                        ssl certificates are generated. Postfix is configured with opendkim,
                                        hostname is set, spf values are generated.
                                    
[4] deployScripts/   : 'deployScript.py' copies all the application code to its proper directories.
                      And copies the apache2 mod_wsgi configuration for http and https to the apache2 conf directory
                      This configurations has the mod_wsgi request alias that specifies request path '/forum' mapped with
                      the backend scripts path (wsgi wrapper script) '/web/spc/forum/src/forumApp/forum.py'
                      and the configuration for ssl such as enabling SSLEngine and specifying ssl certificates is
                      done in this script. In this way application is deployed successfully.


