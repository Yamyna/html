#!/bin/bash

# Démarrer les services nécessaires
service clamav-daemon start

# Garder le conteneur en vie
tail -f /dev/null
