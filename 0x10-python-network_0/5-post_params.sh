#!/bin/bash
# Displays the body of a POST request
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
