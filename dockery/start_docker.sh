#!/bin/bash

# Supprimer les conteneurs existants pour éviter les conflits de noms
docker rm -f script_antivirus script_python

# Construire les images
docker build -f script_antivirus -t script_antivirus . & docker build -f script_python -t script_python . 
wait

echo "Toutes les images ont été construites."

# Démarrer les conteneurs
docker run -d --name script_antivirus script_antivirus & docker run -d --name script_python script_python
wait

echo "Tous les conteneurs ont été démarrés."

# Copier le fichier test.exe dans les conteneurs


# Attendre que les copies soient terminées
wait


echo "Tous les fichiers ont été copiés dans les conteneurs."





# Lancer les scans
docker exec script_antivirus /scan.sh ../uploads/test.exe & docker exec script_python sudo python3 ../src_analyze/main.py 
wait

echo "Tous les scans ont été effectués."

#récupérer les résultats


# Attendre que les copies soient terminées
wait

# Suppression des conteneurs
docker rm -f script_antivirus script_python &

wait

echo "Tous les conteneurs ont été supprimés."