#!/bin/bash

rkhunter --update --propupd &

# Garder le conteneur en vie
tail -f /dev/null