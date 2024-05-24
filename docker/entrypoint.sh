#!/bin/bash

# Démarrer les services nécessaires
service clamav-daemon start

# Mettre à jour la base de données ClamAV en arrière-plan
freshclam -d &

# Garder le conteneur en vie
tail -f /dev/null