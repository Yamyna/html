#!/bin/bash

# Construire l'image à partir de Dockerfile1
docker build -f clamav_daemon -t clamav-daemon . &

# Construire l'image à partir de Dockerfile2
docker build -f f_prot -t f_prot . &

# Construire l'image à partir de Dockerfile3
docker build -f sophos -t sophos . &

# Attendre que toutes les constructions soient terminées
wait

echo "Toutes les images ont été construites."

# Démarrer les conteneurs
docker run -d --name clamav-daemon clamav-daemon &

docker run -d --name f-prot f-prot &

docker run -d --name sophos sophos

#Attendre que les conteneurs soient démarrés
wait

echo "Tous les conteneurs ont été démarrés."

# copier le fichier test.exe dans les conteneurs
docker cp test.exe clamav-daemon:/tmp/test.exe &
docker cp test.exe f-prot:/tmp/test.exe &
docker cp test.exe sophos:/tmp/test.exe

# Attendre que les copies soient terminées
wait

echo "Tous les fichiers ont été copiés dans les conteneurs."

# Lancer les scans

docker exec clamav-daemon /bin/bash -c "/scan.sh /tmp/test.exe" &
docker exec f-prot /bin/bash -c "/scan.sh /tmp/test.exe" &
docker exec sophos /bin/bash -c "/scan.sh /tmp/test.exe"



