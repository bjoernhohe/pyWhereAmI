import urllib.request
import json

ext_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
print(ext_ip)
url = 'http://ip-api.com/json/' + ext_ip

req = urllib.request.Request(url)
out = urllib.request.urlopen(req).read()
print(out)
person_dict = json.loads(out)
print(person_dict['regionName'])