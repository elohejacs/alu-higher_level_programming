#!/usr/bin/python3
"""https://alu-intranet.hbtn.io/status using urllib."""
import urllib.request
# Fetching the URL content using urllib
with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    body = response.read()
# Printing the response details
print("Body response:")
print(f"    - type: {type(body)}")
print(f"    - content: {body}")
print(f"    - utf8 content: {body.decode('utf-8')}")
