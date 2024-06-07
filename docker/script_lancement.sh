#!/bin/bash

test.exe=  "test.exe"

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

# copier le fichier dans les conteneurs
docker cp /var/www/html/virus/test.execlamav_daemon:/tmp/virus/test.exe&
docker cp /var/www/html/virus/test.exepython_analyze:/tmp/virus/test.exe&


# Attendre que les copies soient terminées
wait

echo "Tous les fichiers ont été copiés dans les conteneurs."

#suppression fichiers virus
rm /var/www/html/virus/test.exe

echo "Le fichier virus a été supprimé de la machine."

# Lancer les scans

docker exec clamav_daemon /scan.sh /tmp/virus/test.exe&
docker exec python_analyze python3 /tmp/src_analyze/main.py &
docker exec clamav_daemon clamscan /tmp/virus/test.exe

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