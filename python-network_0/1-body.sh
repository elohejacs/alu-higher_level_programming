#!/bin/bash
# Sends a GET request to the URL and displays the response body if status is 200
curl -sL -o /dev/null -w "%{http_code}" "$1" | grep -q "200" && curl -s "$1"
