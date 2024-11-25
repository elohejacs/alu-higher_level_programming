#!/usr/bin/python3
"""
Takes a URL as input, sends a request to the URL, and displays the value
of the X-Request-Id variable in the response header.
"""

from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as response:
        x_request_id = response.getheader("X-Request-Id")
        print(x_request_id)
