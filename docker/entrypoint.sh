#!/bin/bash

# Vérifier quel service doit être lancé
if [ "$1" == "clamav" ]; then

    # Démarrer le service clamav-daemon
    echo "Démarrage du service clamav-daemon..."
    service clamav-daemon start
fi
if [ [ "$1" == "analyze_url" || "$1" == "python_analyze" ]]; then
  # Activate the virtual environment
    source /venv/bin/activate
    tail -f /dev/null
    # Execute the provided command
    exec "$@"
    
fi

# Garder le conteneur en vie
tail -f /dev/null
