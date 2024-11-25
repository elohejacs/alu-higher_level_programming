#!/usr/bin/python3
"""
Fetches https://alu-intranet.hbtn.io/status using urllib.
Displays the response in a specific format.
"""

from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alu-intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print("    - type: {}".format(type(body)))
        print("    - content: {}".format(body))
        print("    - utf8 content: {}".format(body.decode("utf-8")))
