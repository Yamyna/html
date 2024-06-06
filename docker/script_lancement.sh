#!/bin/bash

FILENAME=$1

# Supprimer les conteneurs existants pour éviter les conflits de noms
docker rm -f clamav_daemon python_analyze

# Construire l'image à partir de clamav_daemon
docker build -f clamav_daemon -t clamav_daemon . &
docker build -f python_analyze -t python_analyze .

# Attendre que toutes les constructions soient terminées
wait

echo "Toutes les images ont été construites."

# Démarrer les conteneurs
docker run -d --name clamav_daemon clamav_daemon &
docker run -d --name python_analyze python_analyze

# Attendre que les conteneurs soient démarrés
wait

echo "Tous les conteneurs ont été démarrés."

# Copier le fichier test.exe dans les conteneurs
docker cp /var/www/html/uploads/$FILENAME clamav_daemon:/var/www/html/uploads/$FILENAME &
docker cp /var/www/html/uploads/$FILENAME python_analyze:/var/www/html/uploads/$FILENAME &

# Attendre que les copies soient terminées
wait

echo "Tous les fichiers ont été copiés dans les conteneurs."

# Suppression fichiers
rm -f /var/www/html/uploads/$FILENAME

echo "Le fichier a été supprimé de la machine."

# Lancer les scans
docker exec clamav_daemon /scan.sh /var/www/html/uploads/$FILENAME &
docker exec python_analyze python3 /var/www/html/src_analyze/main.py &
docker exec clamav_daemon clamscan /var/www/html/uploads/$FILENAME

wait

echo "Tous les scans ont été effectués."

# Vérifier et supprimer les anciens résultats
if [ -f "/var/www/html/analyze_result/scan_result_clam.txt" ]; then
    rm /var/www/html/analyze_result/scan_result_clam.txt
fi
if [ -f "/var/www/html/analyze_result/scan_result_python.txt" ]; then
    rm /var/www/html/analyze_result/scan_result_python.txt
fi

# Copier les résultats des scans
docker cp clamav_daemon:/var/www/html/scan_result.txt /var/www/html/analyze_result/scan_result_clam.txt
docker cp python_analyze:/var/www/html/scan_result.txt /var/www/html/analyze_result/scan_result_python.txt

# Suppression des conteneurs
docker rm -f clamav_daemon python_analyze &

wait

echo "Tous les conteneurs ont été supprimés."

# Lancer le script d'analyse des résultats
python3 /var/www/html/analyze_result/result_analyse.py