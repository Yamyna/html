#!/bin/bash

rkhunter --update &

# Garder le conteneur en vie
tail -f /dev/null