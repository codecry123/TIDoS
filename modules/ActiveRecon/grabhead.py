#!/usr/bin/env python2
# coding:  utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#This module requires TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework 

import urllib2
import time
import sys
from time import sleep
from colors import * 

def grabhead(web):

    time.sleep(0.4)
    print R+'\n      =================================='
    print R+'      G R A B   H T T P   H E A D E R S'
    print R+'     ===================================\n'
    print('' + GR + color.BOLD + ' [!] Grabbing HTTP Headers...')
    time.sleep(0.4)
    web.rstrip
    try:
	    header = urllib2.urlopen(web).info()
	    print ''
	    print(G+str(header))
    except:
	print R+' [-] Something went wrong...'


