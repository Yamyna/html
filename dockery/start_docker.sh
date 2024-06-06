#!/bin/bash

# Supprimer les conteneurs existants pour éviter les conflits de noms
docker rm -f script_antivirus 

# Construire les images
docker build -f script_antivirus -t script_antivirus . 
wait

echo "Toutes les images ont été construites."

# Démarrer les conteneurs
docker run -d --name script_antivirus script_antivirus 
wait

echo "Tous les conteneurs ont été démarrés."

# Copier le fichier RACI.pdf dans les conteneurs
docker cp ../uploads/RACI.pdf script_antivirus:/uploads_docker/RACI.pdf 

# Attendre que les copies soient terminées
wait


echo "Tous les fichiers ont été copiés dans les conteneurs."

# Lancer les scans
docker exec script_antivirus /scan.sh ../uploads_docker/RACI.pdf 
wait

echo "Tous les scans ont été effectués."

#récupérer les résultats
sudo docker cp script_antivirus:/scan_result.txt /var/www/html/dockery/scan_result.txt

# Attendre que les copies soient terminées
wait

# Suppression des conteneurs
docker rm -f script_antivirus  &

wait

echo "Tous les conteneurs ont été supprimés."