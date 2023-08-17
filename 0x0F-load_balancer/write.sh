#!/usr/bin/env bash
touch config.txt
var="works"
echo "backend webservers" | sudo tee -a config.txt > /dev/null
printf "\tmode http" | sudo tee -a config.txt > /dev/null

echo "$var"
