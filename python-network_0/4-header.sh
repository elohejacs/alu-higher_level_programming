#!/bin/bash
#Sendss a GET request to the provided URL with a header
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
