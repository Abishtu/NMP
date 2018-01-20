#Code from https://stackoverflow.com/questions/12101239/multiple-ping-script-in-python/12102040#12102040

#Original Author: jsf Stackoverflow community
#Modified by Tannishpage

import os
import time
from subprocess import Popen, DEVNULL
import socket
from datetime import datetime as dt

start = dt.now()
lent = 0
default = input('Enter the default (eg: 192.168): ')
r = input('Enter a number between 1 to 255: ')
start = dt.now()
for nn in range(1, int(r) + 1):
    p = {} # ip -> process
    for n in range(0, 256): # start ping processes
        ip = "{}.{}.{}".format(default ,nn, n)
        p[ip] = Popen(['ping', '-n', '-w1', '-c1', ip], stdout=DEVNULL)
        #NOTE: you could set stderr=subprocess.STDOUT to ignore stderr also
    lent = lent + len(p)
    while p:
        for ip, proc in p.items():
            if proc.poll() is not None: # ping finished
                del p[ip] # remove from the process list
                if proc.returncode == 0:
                    print('IP Address: {}'.format(ip))
                    try:
                        name = list(socket.gethostbyaddr(ip))[0]
                        print('Network name: {}\n'.format(name)) #socket is used to resolve the ip address to a network name
                    except:
                        pass
            break

end = dt.now()
print("Scanned {} IPs in {}".format(lent, (end - start).total_seconds()))
