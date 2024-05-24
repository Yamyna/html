#!/bin/bash

# Construire l'image à partir de clamav_daemon
docker build -f clamav_daemon -t clamav-daemon . &

# Construire l'image à partir de firejail
docker build -f firejail -t firejail . &

# Construire l'image à partir de rkhunter
docker build -f rkhunter -t rkhunter . &

# Attendre que toutes les constructions soient terminées
wait

echo "Toutes les images ont été construites."

# Démarrer les conteneurs
docker run -d --name clamav-daemon clamav-daemon &

docker run -d --name firejail firejail &

docker run -d --name rkhunter rkhunter &

#Attendre que les conteneurs soient démarrés
wait

echo "Tous les conteneurs ont été démarrés."

# copier le fichier test.exe dans les conteneurs
docker cp /LightningMalware/LightningMalware/docker/test.exe clamav-daemon:/tmp/test.exe &
docker cp /LightningMalware/LightningMalware/docker/test.exe firejail:/tmp/test.exe &
docker cp /LightningMalware/LightningMalware/docker/test.exe rkhunter:/tmp/test.exe &

# Attendre que les copies soient terminées
wait

echo "Tous les fichiers ont été copiés dans les conteneurs."

# Lancer les scans

docker exec clamav-daemon /scan.sh /tmp/test.exe &
wait
docker exec rkhunter/scan.sh /tmp/test.exe &
wait
docker exec firejail /scan.sh /tmp/test.exe &


wait

echo "Tous les scans ont été effectués."

# suppression des conteneurs
docker rm -f clamav-daemon firejail rkhunter &

wait

echo "Tous les conteneurs ont été supprimés."


