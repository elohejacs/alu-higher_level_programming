#!/usr/bin/python3
"""Task 0"""

import urllib.request
"""using another  fnct"""

"""Fetching the URL content using urllib"""
with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    body = response.read()

"""Printing the response details"""
print("Body response:")
print(f"    - type: {type(body)}")
print(f"    - content: {body}")
print(f"    - utf8 content: {body.decode('utf-8')}")
