#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import os
import sys
import requests
import fileinput
import subprocess
import shlex

f = str(sys.argv[1])
log = '/Users/johnny.chung/Downloads/' + f + '.log'

with open(f, 'r') as lst:
	for line in lst:
		csurl = line.rstrip('\n')	# csurl has data of this format - https://content.etilize.com/650/1017377298.jpg
		data = line.split('/')	# data has data of this format -  ['http:', '', 'content.etilize.com', 'images', '200', '200', '.jpg?noimage=logo']
		data[-1] = data[-1].rstrip('\n')
		ll = len(data)
		uri = ''
		for i in range(ll-3):
			uri = uri+'/'+data[i+3]		# uri has data of this format - /images/200/50283423.jpg
		osurl = 'http://qa-content-etilize.cdnga.net' + uri
		
		csrq = requests.get(csurl)
		osrq = requests.get(osurl)
		csrc = csrq.status_code			# get the return code of CS request
		osrc = osrq.status_code			# get the return code of OS request
		
		with open(log, "a") as res:
			if csrc == osrc:
				res.write(csurl + ' ' + str(csrc) + ' - ' + osurl + ' ' + str(osrc) + '\n')
			else:
				res.write('DIFF ' + csurl + ' ' + str(csrc) + ' - ' + osurl + ' ' + str(osrc) + '\n')
