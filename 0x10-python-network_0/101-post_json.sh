#!/bin/bash
#Displays the body of a JSON post request
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
