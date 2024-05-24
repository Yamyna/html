#!/bin/bash

# Construire l'image à partir de Dockerfile1
docker build -f clamav_daemon -t clamav-daemon . &

# Construire l'image à partir de Dockerfile2
docker build -f firejail -t firejail . &

# Construire l'image à partir de Dockerfile3
docker build -f rkhunter -t rkhunter . &

# Attendre que toutes les constructions soient terminées
wait

echo "Toutes les images ont été construites."

# Démarrer les conteneurs
docker run -d --name clamav-daemon clamav-daemon &

docker run -d --name firejail firejail &

docker run -d --name rkhunter rkhunter

#Attendre que les conteneurs soient démarrés
wait

echo "Tous les conteneurs ont été démarrés."

# copier le fichier test.exe dans les conteneurs
docker cp /LightningMalware/LightningMalware/docker/test.exe clamav-daemon:/tmp/test.exe &
docker cp /LightningMalware/LightningMalware/docker/test.exe firejail:/tmp/test.exe &
docker cp /LightningMalware/LightningMalware/docker/test.exe rkhunter:/tmp/test.exe

# Attendre que les copies soient terminées
wait

echo "Tous les fichiers ont été copiés dans les conteneurs."

# Lancer les scans

docker exec clamav-daemon /bin/bash -c "/scan.sh /tmp/test.exe" &
docker exec firejail /bin/bash -c "/scan.sh /tmp/test.exe" &
docker exec rkhunter /bin/bash -c "/scan.sh /tmp/test.exe"

wait

echo "Tous les scans ont été effectués."

# suppression des conteneurs
docker stop clamav-daemon firejail rkhunter 

wait

echo "Tous les conteneurs ont été arrêtés."

docker rm -f clamav-daemon firejail rkhunter 

wait

echo "Tous les conteneurs ont été supprimés."


