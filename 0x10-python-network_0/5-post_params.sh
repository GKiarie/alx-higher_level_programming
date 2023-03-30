#!/bin/bash
# script that takes in a URL,sends POST request to passed URL,displaysbody of response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
