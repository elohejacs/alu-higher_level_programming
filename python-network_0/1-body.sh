#!/bin/bash
# Sends a GET request to the URL and displays the response body if status is 200
curl -s "$1" | wc -c
