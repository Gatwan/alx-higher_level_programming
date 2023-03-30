#!/bin/bash
# Displays the content-length of a http request
curl -sI "$1" | wc -c
