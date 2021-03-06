#!/usr/bin/env python2
# coding:'+B+' utf-8

#-:'+B+'-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#This module requires TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework 

import sys
import os
import time
import subprocess
import random
from random import randint
from subprocess import call
sys.path.append('modules/InfoDisc/')

from credit import *
from emailext import *
from errors import *
from phone import *
from ssn import *
from infodiscban import *
from colors import *
from internalip import *
from footprint import *
from footprintban1 import *

def infodisc(web):

    print " [!] Module Selected : Information Disclosure\n\n"
    infodiscban()
    print ''
    time.sleep(0.3)
    v = raw_input (''+GR+'  [#] \033[1;4mTID\033[0m'+GR+' :> ' + color.END)
    print ''
    if v == '1':
	print C+' [!] Type Selected :'+B+' Credit Card Enumeration'
	credit(web)
	print '\n\n'
	infodisc(web)

    elif v == '2':
	print C+' [!] Type Selected :'+B+' Extract All Emails'
	emailext(web)
	print '\n\n'
	infodisc(web)

    elif v == '3':
	print C+' [!] Type Selected :'+B+' Enumerate Errors + FPD'
	errors(web)
	print '\n\n'
	infodisc(web)

    elif v == '4':
	print C+' [!] Type Selected :'+B+' Internal IP disclosure'
	internalip(web)
	print '\n\n'
	infodisc(web)

    elif v == '5':
	print C+' [!] Type Selected :'+B+' Phone Numbers Extract'
	phone(web)
	print '\n\n'
	infodisc(web)

    elif v == '6':
	print C+' [!] Type Selected :'+B+' Social Security Numbers'
	ssn(web)
	print '\n\n'
	infodisc(web)

    elif v == 'A':
	print C+' [!] Type Selected :'+B+' All Modules'
	time.sleep(0.5)
	print C+' [*] Firing up module -->'+B+' Credit Cards'
	credit(web)
	print C+' [!] Module Completed -->'+B+' Credit Cards\n'

	time.sleep(1)
	print C+' [*] Firing up module -->'+B+' Email Extraction'
	email(web)
	print C+' [!] Module Completed -->'+B+' Email Hunt\n'
	
	time.sleep(1)
	print C+' [*] Firing up module -->'+B+' Errors Enumeration + FPD'
	errors(web)
	print C+' [!] Module Completed -->'+B+' Errors Enumeration\n'
	time.sleep(1)

	print C+' [*] Firing up module -->'+B+' Extract Phone Numbers'
	phone(web)
	print C+' [!] Module Completed -->'+B+' Extract Phone Numbers\n'
	time.sleep(1)

	print C+' [*] Firing up module -->'+B+' Extract Social Security Numbers'
	ssn(web)
	print C+' [!] Module Completed -->'+B+' Extract SSN\n'
	time.sleep(1)

	print C+' [!] All scantypes have been tested on target...'
	time.sleep(1)
	print C+' [*] Going back to menu...'
	footprintban1()
	footprint(web)

    elif v == '99':
	print C+' [*] Back to the menu !'
	footprintban1()
	footprint(web) 

    else:
	dope = ['You high dude?','Shit! Enter a valid option','Whoops! Thats not an option','Sorry! You just typed shit']
	print dope[randint(0,3)]
	time.sleep(0.7)
	os.system('clear')
	infodisc(web)

