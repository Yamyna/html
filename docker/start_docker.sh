#!/bin/bash

# Supprimer les conteneurs existants pour éviter les conflits de noms
docker rm -f script_antivirus script_python script_api

# Construire les images
docker build -f script_antivirus -t script_antivirus . &
docker build -f script_python -t script_python . &
docker build -f script_api -t script_api .

# Attendre que toutes les constructions soient terminées
wait

echo "Toutes les images ont été construites."

# Démarrer les conteneurs
docker run -d --name script_antivirus script_antivirus &
docker run -d --name script_python script_python &
docker run -d --name script_api script_api

# Attendre que les conteneurs soient démarrés
wait

echo "Tous les conteneurs ont été démarrés."



# Suppression des conteneurs
docker rm -f script_antivirus script_python script_api &

wait

echo "Tous les conteneurs ont été supprimés."