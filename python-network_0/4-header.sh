#!/bin/bash
#doing the task
# Sends a GET request to the provided URL with a custom header
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
