#!/usr/bin/python3
"""
Fetches the status from https://alu-intranet.hbtn.io/status using urllib.
The script prints the following details about the response:
    - type: The type of the response content
    - content: The raw content of the response
    - utf8 content: The decoded content as a UTF-8 string
"""
import urllib.request

# Fetching the URL content using urllib
with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    body = response.read()

# Printing the response details
print("Body response:")
print(f"    - type: {type(body)}")
print(f"    - content: {body}")
print(f"    - utf8 content: {body.decode('utf-8')}")
