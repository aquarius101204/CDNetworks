#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import os
import sys
import fileinput
 
# get the file name to store the result of ls as an argument
sid = "nsuslab"
list = "/tmp/nsuslab/full_list.txt"
 
# get the length of SID to calculate the start for substr at right below; adding 9 is due to "/starfs/" at the beginning of path
l_sid = len(sid)
start = 9 + l_sid
 
# gather the directory list first, otherwise any empty directories will not be created (run just one time on a certain server)
cmd = "find /starfs/" + sid + " -maxdepth 20 -type d | awk '{print substr($0," + str(start) + "); }' >> " + list
os.system(cmd)
 
# for files that the root is a sub-directory at depth 1 as we will gather files separately at further depth for these sub-directories  (run just one time on a certain server)
cmd = "find /starfs/" + sid + "/flashgames/ -maxdepth 1 -type f | awk '{print substr($0," + str(start) + "); }' >> " + list
os.system(cmd)
os.system(cmd)
 
# declare the sub-directories where you are going to gather from
sub_d = ['/portal/C\:/', '/portal/iso/', '/portal/static/Update/', '/portal/static/test/', '/iron/', '/irontest/']
 
# make a linux command gathering all files and directories with path
for line in sub_d:
        cmd = "find /starfs/" + sid + line + " -maxdepth 20 -type f | awk '{print substr($0," + str(start) + "); }' >> " + list
        os.system(cmd)
 
# Encode and replace special characters inplace
s_char = {" ":"%20", "!":"%21", "#":"%23", "'":"%27", "(":"%28", ")":"%29", "[":"%5B", "]":"%5D", "®":"%C2%AE", "Á":"%C3%81", "É":"%C3%89", "Í":"%C3%8D", "á":"%C3%A1", "é":"%C3%A9", "í":"%C3%AD", "ó":"%C3%B3"}

for line in fileinput.input(list, inplace=1):
    if " " in line:
        line = line.replace(" ", s_char.get(" "))
    if "!" in line:
        line = line.replace("!", s_char.get("!"))
    if "#" in line:
        line = line.replace("#", s_char.get("#"))
    if "'" in line:
        line = line.replace("'", s_char.get("'"))
    if "(" in line:
        line = line.replace("(", s_char.get("("))
    if ")" in line:
        line = line.replace(")", s_char.get(")"))
    if "[" in line:
        line = line.replace("[", s_char.get("["))
    if "]" in line:
        line = line.replace("]", s_char.get("]"))
    if "®" in line:
        line = line.replace("®", s_char.get("®"))
    if "Á" in line:
        line = line.replace("Á", s_char.get("Á"))
    if "É" in line:
        line = line.replace("É", s_char.get("É"))
    if "Í" in line:
        line = line.replace("Í", s_char.get("Í"))
    if "á" in line:
        line = line.replace("á", s_char.get("á"))
    if "é" in line:
        line = line.replace("é", s_char.get("é"))
    if "í" in line:
        line = line.replace("í", s_char.get("í"))
    if "ó" in line:
        line = line.replace("ó", s_char.get("ó"))
    sys.stdout.write(line)
