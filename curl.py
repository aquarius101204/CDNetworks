#!/usr/bin/python
# -*- coding: UTF-8 -*-
  
import os
import sys
import fileinput
 
# put the file name of a split filelist
list = "/tmp/nsuslab/full_list_1.txt"
 
# run a curl command requesting files for the first time to OS in order to sync
with open(list, 'r') as list:
        for line in list:
                cmd = "curl -sw '%{http_code}' 'http://nsuslab-contents.wcscdn55.v1.wcsapi.com" + line.rstrip('\n') + "' -H 'Host: nsuslab-contents.os.cdngp.net' --head -o /dev/null"
                result = os.popen(cmd).read()
                record = result + ' ' + line
                with open("/tmp/nsuslab/full_sync_1.log", "a") as log:
                        log.write(record)
