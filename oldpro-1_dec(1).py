#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By RANA MZ.
#################################################################
#         		ATHOUR : RanaMZ			#
#  		     NAM TU SUNA HUGA			#
#################################################################
#By RanaMZ
 
import os, sys, time, datetime, re, threading, json, random, requests, hashlib, cookielib, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
os.system('git pull')
os.system('clear')
logo = """


\033[1;37m:'######::'##::::'##:'##::: ##:'##::: ##:'##:::'##:\033[1;37m
\033[1;32m'##... ##: ##:::: ##: ###:: ##: ###:: ##:. ##:'##::\033[1;32m
\033[1;31m ##:::..:: ##:::: ##: ####: ##: ####: ##::. ####:::\033[1;31m
\033[1;37m. ######:: ##:::: ##: ## ## ##: ## ## ##:::. ##::::\033[1;37m
\033[1;31m:..... ##: ##:::: ##: ##. ####: ##. ####:::: ##::::\033[1;31m
\033[1;32m'##::: ##: ##:::: ##: ##:. ###: ##:. ###:::: ##::::\033[1;32m
\033[1;31m. ######::. #######:: ##::. ##: ##::. ##:::: ##::::\033[1;31m
\033[1;37m:......::::.......:::..::::..::..::::..:::::..:::::
                               \033[1;37mBy : rANAMZ
  
\033[1;31m        =======
\033[1;31m        N O t E :
\033[1;31m        =======
 \033[1;32m      ==================
\033[1;33m       DONt TRY TO COPY ME
\033[1;33m       BECz itz iMPOSSiBLE
\033[1;32m       ==================
"""
 
def reg():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;32;1m W E L C O M    ....!'
    print ''
    time.sleep(1)
    try:
        to = open('/sdcard/.RANAMZnamtusunahuga.txt', 'r').read()
    except (KeyError, IOError):
        reg2()
 
    r = requests.get('https://raw.githubusercontent.com/HackedDok/h/main/lol.txt').text
    if to in r:
        ip()
    else:
        os.system('clear')
        print logo
        print '\tN O T       F O U N D    ....!'
        print '+=========================================+ '
        print '+=========================================+ '
        print ' \x1b[1;97m Y O U R    T O K E N : ' + to
        raw_input('\x1b[1;92m      E N T E R    IF YOO WANT BUY MY TOOL   ')
        os.system("xdg-open https://wa.me/+923135612566")
        reg()
 
 
def reg2():
    os.system('clear')
    print logo
    print '\tN O T    OK....!'
    print ' \x1b[1;92m E N T ER     IF YOU WANT BUY MY TOOL'
    id = uuid.uuid4().hex[:30]
    print ' YOUR TOKEN : ' + id
    print ''
    raw_input(' E N T E R    F O R     A P R V A L ')
    os.system("xdg-open https://www.facebook.com/RanaMZ.zeshi")
    sav = open('/sdcard/.RANAMZnamtusunahuga.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;97m    E N T E R ')
    reg()
    
    
 
def ip():
    os.system('clear')
    print logo
    print '\tP L E A S E     W A I T...!'
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass
        
    print ' +==========================+'
    print '\x1b[1;97m Your ip: ' + ips
    time.sleep(1)
    print '\x1b[1;97m Your country: ' + country
    time.sleep(1)
    print '\x1b[1;97m Your region: ' + regi
    time.sleep(1)
    print ' \x1b[1;97mYour network: ' + network
    print logo
    print 47 * '-'
    print ' +=========================================+'
    print '\x1b[1;92m[1] \x1b[1;97m |M A I N       M E N U'
    print '\x1b[1;92m[2]     \x1b[1;97m |Contct With Oner [Rana_MZ]'
    print ' +========================================+'
    menu_s()
 
 
def menu_s():
    ms = raw_input('\x1b[1;97m\xe2\x95\xb0\xe2\x94\x80\xe2\x9e\xa4 ')
    if ms == '1':
        os.system("rm -rf $HOME/oldpro")
        os.system("cd $HOME && git clone https://github.com/Shanimz/oldpro.git")     
        
        time.sleep(1)
        os.system("cd $HOME/oldpro && python haha.hehe")
    elif ms == '2':
        print("\033[1;32m  ONER IZ RANA-MZ")
        os.system("xdg-open https://wa.me/+923219033282")
    else:
        print ''
        print '\tNot Jaani'
        print ''
        menu_s()
 
 
if __name__ == '__main__':
    reg()