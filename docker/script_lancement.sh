#!/bin/bash

FILENAME=$1

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
docker cp /var/www/html/virus/$FILENAME clamav_daemon:/tmp/virus/$FILENAME &
docker cp /var/www/html/virus/$FILENAME python_analyze:/tmp/virus/$FILENAME &

# Attendre que les copies soient terminées
wait

echo "Tous les fichiers ont été copiés dans les conteneurs."
# Lancer les scans

docker exec clamav_daemon /scan.sh /tmp/virus/$FILENAME &
docker exec python_analyze python3 /tmp/src_analyze/main.py &
docker exec clamav_daemon clamscan /tmp/virus/$FILENAME

wait

echo "Tous les scans ont été effectués."
#récupérer les résultats
if [ -f "/html/analyze_result/scan_result_clam.txt" ]; then
    rm /html/analyze_result/scan_result_clam.txt
fi
if [ -f "/html/analyze_result/scan_result_python.txt" ]; then
    rm /html/analyze_result/scan_result_python.txt
fi

docker cp clamav_daemon:/tmp/scan_result.txt /html/analyze_result/scan_result_clam.txt
docker cp python_analyze:/tmp/scan_result.txt /html/analyze_result/scan_result_python.txt
# suppression des conteneurs

docker rm -f clamav_daemon python_analyze &

wait

echo "Tous les conteneurs ont été supprimés."

python3 /html/analyze_result/result_analyse.py