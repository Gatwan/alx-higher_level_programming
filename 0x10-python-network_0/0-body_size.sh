#!/bin/bash
# Displays the content-length of a http request
curl -s "$1" | wc -c
