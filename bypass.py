#!/usr/bin/env python3

import requests
import re
import json
import base64

s = requests.Session()

link = input("Masukin link : ")
link_bytes = link.encode('ascii')
b64_bytes = base64.b64encode(link_bytes)
b64_msg = b64_bytes.decode('ascii')
url = s.get("https://lp.nrmn.top/api/bypass?url="+b64_msg)
d = json.loads(url.content)
print("Ini Link nya Lord : " + d['destination'])

#print(b64_msg)