#!/bin/bash

# Démarrer les services nécessaires
service sav-protect start

# Garder le conteneur en vie
tail -f /dev/null