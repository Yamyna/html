#!/bin/bash

# Supprimer les conteneurs existants pour éviter les conflits de noms
docker rm -f script_antivirus &
docker rm -f script_python
wait

# Construire les images
docker build -f script_antivirus -t script_antivirus . &
docker build -f script_python -t script_python .
wait

echo "Toutes les images ont été construites."

# Démarrer les conteneurs
docker run -d --name script_antivirus script_antivirus 
docker run -d --name script_python script_python
wait

echo "Tous les conteneurs ont été démarrés."

# Copier le fichier RACI.pdf dans les conteneurs
docker cp ../uploads/RACI.pdf script_antivirus:/uploads_docker/RACI.pdf &
#docker cp ../uploads/RACI.pdf script_python:/uploads_docker/RACI.pdf &
#docker cp ../src_analyze script_python:/src_analyze_docker
wait

# Vérifier la présence du fichier main.py dans le conteneur
#docker exec script_python ls -l /src_analyze_docker

echo "Tous les fichiers ont été copiés dans les conteneurs."

# Lancer les scans
docker exec script_antivirus /scan.sh ../uploads_docker/RACI.pdf &
#docker exec script_python python3 /src_analyze_docker/src_analyze/main.py
wait

echo "Tous les scans ont été effectués."

#récupérer les résultats du conteneur dans le serveur
sudo docker cp script_antivirus:/scan_result.txt /var/www/html/dockery/scan_result.txt

# Attendre que les copies soient terminées
wait

# Suppression des conteneurs
docker rm -f script_antivirus  &

wait

echo "Tous les conteneurs ont été supprimés."