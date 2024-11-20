#!/bin/bash
# Sends a request to a URL and displays the size of the response body in bytes
curl -sL "$1" | wc -c
