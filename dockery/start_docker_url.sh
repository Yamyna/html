#!/bin/bash

# Supprimer les conteneurs existants pour éviter les conflits de noms
docker rm -f script_url
wait

# Construire les images
docker build -f script_url -t script_url . 
wait

echo "Toutes les images ont été construites."

# Démarrer les conteneurs
docker run -d --name script_url script_url 
wait

echo "Tous les conteneurs ont été démarrés."

# Copier le fichier RACI.pdf dans les conteneurs
docker cp ../src_analyze/analyze_url.py script_url:/src_analyze_docker &
docker cp ../src_analyze/API_KEY.py script_url:/src_analyze_docker
wait

# Vérifier la présence du fichier main.py dans le conteneur
docker exec script_url ls -l /src_analyze_docker
echo "Tous les fichiers ont été copiés dans les conteneurs."

# Lancer les scans
docker exec script_url python3 /src_analyze_docker/src_analyze/analyze_url.py
wait
echo "Tous les scans ont été effectués."

# Suppression des conteneurs
docker rm -f script_url &
wait
echo "Tous les conteneurs ont été supprimés."