#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import os
from time import sleep
 
delay_time = 0.
cmd = "ls /usr/local/cdnet/logs/starfs/starftpd-trans*"
logfile = os.popen(cmd).read().rstrip('\n')
 
# Replace root directory per account inplace
s_acct = {"gameportal_nsuslab":"/portal", "flashgames_nsuslab":"/flashgames", "portal.maipo.aspnet_nsuslab":"/portal", "patrick.choi_nsuslab":"/portal/static/leaflet"}
 
with open(logfile, "r") as f:
        while True:
                where = f.tell()
                line = f.readline().strip()
                if not line:
                        sleep(0.1)
                        delay_time += 0.1
                        f.seek(where)
                        if delay_time > 1200.0: # if there is no new line input for 20 mins, terminate the program
                                break
                else:
                        delay_time = 0. # reset delay time
                        if 'nsuslab' and 'UPLOAD' in line:   # filtering with 'nsuslab' and 'UPLOAD'
                                # get the new record of uploading
                                echo = "echo " + "'" + line + "'" + " | awk '{print}' >> /tmp/nsuslab/incremental_list.txt"
                                os.system(echo)
 
                                date = "echo " + "'" + line + "'" + " | awk '{print $1}'"
                                date = os.popen(date).read().rstrip('\n')
                                time = "echo " + "'" + line + "'" + " | awk '{print $2}'"
                                time = os.popen(time).read().rstrip('\n')
                                acct = "echo " + "'" + line + "'" + " | awk '{print $6}'"
                                acct = os.popen(acct).read().rstrip('\n')
                                file = "echo " + "'" + line + "'" + " | awk '{print $9}'"
                                file = os.popen(file).read().rstrip('\n')
                                if acct in s_acct:
                                        file = s_acct[acct]+file        # revise the root directory if the access point is a sub-directory
                                cmd = "curl -sw '%{http_code}' 'http://nsuslab-contents.wcscdn55.v1.wcsapi.com" + line.rstrip('\n') + "' -H 'Host: nsuslab-contents.os.cdngp.net' --head -o /dev/null"
                                result = os.popen(cmd).read()
                                record = date + ' ' + time + ' UTC ' + acct + ' ' + result + ' ' + file + '\n'
                                with open("/tmp/nsuslab/incremental_sync.log", "a") as log:
                                        log.write(record)
