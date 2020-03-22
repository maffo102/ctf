import requests
import re
import md5
import hashlib

URL = 'http://docker.hackthebox.eu:32356/'

s = requests.Session()
r = s.get(URL)
print("Getting string to hash...")

sth = r.text.split('\n')[5].split('<')[3].split('>')[1]
print("The string is: " + sth)

print("Calculating hash...")
res = hashlib.md5(sth.encode('utf-8')).hexdigest()
print("The hash is: {}".format(res))


resp = {'hash': res}
req2 = s.post(URL, data=resp)
print("The flag is: " + req2.text.split('\n')[5].split('<')[5].split('>')[1])

