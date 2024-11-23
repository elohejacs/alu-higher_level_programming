#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    body = response.read()

print("Body response:")
print(f"    - type: {type(body)}")
print(f"    - content: {body}")
print(f"    - utf8 content: {body.decode('utf-8')}")
