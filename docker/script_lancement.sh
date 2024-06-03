#!/bin/bash

# Construire l'image à partir de clamav_daemon
docker build -f clamav_daemon -t clamav_daemon . &
docker build -f python_analyze -t python_analyze .


# Attendre que toutes les constructions soient terminées
wait

echo "Toutes les images ont été construites."

# Démarrer les conteneurs
docker run -d --name clamav_daemon clamav_daemon&
docker run -d --name python_analyze python_analyze
#Attendre que les conteneurs soient démarrés
wait

echo "Tous les conteneurs ont été démarrés."

# copier le fichier test.exe dans les conteneurs
docker cp /LightningMalware/LightningMalware/virus clamav_daemon:/tmp/virus &
docker cp /LightningMalware/LightningMalware/src_analyze python_analyze:/tmp/src_analyze&
docker cp /LightningMalware/LightningMalware/virus python_analyze:/tmp/virus&
# Attendre que les copies soient terminées
wait

echo "Tous les fichiers ont été copiés dans les conteneurs."
# Lancer les scans

docker exec clamav_daemon /scan.sh /tmp/virus/test.exe &
docker exec python_analyze python3 /tmp/src_analyze/main.py 

wait

echo "Tous les scans ont été effectués."
#récupérer les résultats

docker cp clamav_daemon:/tmp/scan_result.txt /LightningMalware/LightningMalware/analyze_result/scan_result_clam.txt
docker cp python_analyze:/tmp/scan_result.txt /LightningMalware/LightningMalware/analyze_result/analyze_result_python.txt
# suppression des conteneurs

docker rm -f clamav_daemon python_analyze &

wait

echo "Tous les conteneurs ont été supprimés."

cat /LightningMalware/LightningMalware/analyze_result/scan_result_clam.txt
cat /LightningMalware/LightningMalware/analyze_result/analyze_result_python.txt


