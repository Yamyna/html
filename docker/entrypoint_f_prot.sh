#!/bin/bash

# Démarrer les services nécessaires
service /opt/f-prot/fpupdate.pl

# Garder le conteneur en vie
tail -f /dev/null
