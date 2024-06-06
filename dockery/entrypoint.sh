#!/bin/bash

# Vérifier quel service doit être lancé
if [ "$1" == "clamav" ]; then
    # Mettre à jour la base de données ClamAV et démarrer le service
    service script_antivirus start

fi

# Garder le conteneur en vie
tail -f /dev/null