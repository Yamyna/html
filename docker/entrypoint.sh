#!/bin/bash

# Vérifier quel service doit être lancé
if [ "$1" == "clamav" ]; then
    # Mettre à jour la base de données ClamAV et démarrer le service
    freshclam
    service clamav-daemon start
elif [ "$1" == "firejail" ]; then
    # Démarrer Firejail (si nécessaire) et exécuter une commande spécifique
    echo "Firejail started (if necessary)"
elif [ "$1" == "rkhunter" ]; then
    # Mettre à jour rkhunter et exécuter une analyse
    rkhunter --update
    rkhunter --propupd
fi

# Garder le conteneur en vie
tail -f /dev/null
