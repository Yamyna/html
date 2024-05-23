#!/bin/bash

# Activer l'environnement virtuel
source /home/cuckoo/venv/bin/activate

# Démarrer les services nécessaires
service sav-protect start

# Configurer et démarrer Cuckoo
cuckoo community
cuckoo -d

# Garder le conteneur en vie
tail -f /dev/null