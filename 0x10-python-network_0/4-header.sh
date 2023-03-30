#!/bin/bash
#  script takes in a URL as an arg,sends GET request to URL,displays body ofresponse
curl -s -H "X-School-User-Id: 98" "$1"
