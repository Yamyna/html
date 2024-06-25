#!/bin/bash

RANDOM_NUMBER=$RANDOM
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_DIR="/var/www/logs"
LOGFILE="$LOG_DIR/script_lancement_file_${TIMESTAMP}_docker_${RANDOM_NUMBER}.log"

# Vérifie si un fichier a été fourni en argument
if [ -z "$1" ]; then
    echo "Usage: $0 <absolute-path-to-file>"
    exit 1
fi

# Créer le répertoire de log si nécessaire et vérifier les permissions
if [ ! -d "$LOG_DIR" ]; then
    mkdir -p $LOG_DIR
    if [ $? -ne 0 ]; then
        echo "Erreur lors de la création du répertoire de log."
        exit 1
    fi
    chown www-data:www-data $LOG_DIR
    if [ $? -ne 0 ]; then
        echo "Erreur lors du changement de propriétaire du répertoire de log."
        exit 1
    fi
fi

touch $LOGFILE
if [ $? -ne 0 ]; then
    echo "Erreur lors de la création du fichier de log."
    exit 1
fi
chown www-data:www-data $LOGFILE
if [ $? -ne 0 ]; then
    echo "Erreur lors du changement de propriétaire du fichier de log."
    exit 1
fi

# Redirection de la sortie standard et de la sortie d'erreur
exec > >(tee -a $LOGFILE) 2>&1

echo "Script démarré"
FILE_TO_SCAN="$1"
FILE_NAME=$(basename "$FILE_TO_SCAN")

# Définit les chemins des Dockerfiles et le répertoire de travail
WORK_DIR="/script/script_LightningMalware"
CLAMAV_DOCKERFILE_PATH="$WORK_DIR/docker/clamav_daemon"
PYTHON_ANALYZE_DOCKERFILE_PATH="$WORK_DIR/docker/python_analyze"

# Vérifie si les conteneurs existent avant la construction

docker ps -a | grep clamav_daemon$RANDOM_NUMBER
if [ $? -eq 0 ]; then
    RANDOM_NUMBER=$RANDOM
fi

docker ps -a | grep python_analyze$RANDOM_NUMBER
if [ $? -eq 0 ]; then
    RANDOM_NUMBER=$RANDOM
fi

echo "Building Docker image..."
docker build -f $CLAMAV_DOCKERFILE_PATH -t clamav_daemon$RANDOM_NUMBER $WORK_DIR/docker
if [ $? -ne 0 ]; then
    echo "Erreur lors de la construction de l'image clamav_daemon$RANDOM_NUMBER"
    exit 1
fi

docker build -f $PYTHON_ANALYZE_DOCKERFILE_PATH -t python_analyze$RANDOM_NUMBER $WORK_DIR/docker
if [ $? -ne 0 ]; then
    echo "Erreur lors de la construction de l'image python_analyze$RANDOM_NUMBER"
    exit 1
fi



echo "Toutes les images ont été construites."

docker rm -f clamav_daemon$RANDOM_NUMBER python_analyze$RANDOM_NUMBER 2>/dev/null

docker run --rm -d --name clamav_daemon$RANDOM_NUMBER clamav_daemon$RANDOM_NUMBER
if [ $? -ne 0 ]; then
    echo "Erreur lors du démarrage du conteneur clamav_daemon$RANDOM_NUMBER"
    exit 1
fi

docker run --rm -d --name python_analyze$RANDOM_NUMBER python_analyze$RANDOM_NUMBER
if [ $? -ne 0 ]; then
    echo "Erreur lors du démarrage du conteneur python_analyze$RANDOM_NUMBER"
    exit 1
fi



echo "Tous les conteneurs ont été démarrés."

docker exec clamav_daemon$RANDOM_NUMBER freshclam
if [ $? -ne 0 ]; then
    echo "Erreur lors de la mise à jour de la base de données ClamAV"
    exit 1
fi

docker exec clamav_daemon$RANDOM_NUMBER mkdir -p /tmp/uploads
if [ $? -ne 0 ]; then
    echo "Erreur lors de la création du répertoire /tmp/uploads dans clamav_daemon$RANDOM_NUMBER"
    exit 1
fi

docker exec python_analyze$RANDOM_NUMBER mkdir -p /tmp/uploads
if [ $? -ne 0 ]; then
    echo "Erreur lors de la création du répertoire /tmp/uploads dans python_analyze$RANDOM_NUMBER"
    exit 1
fi

docker cp "$FILE_TO_SCAN" clamav_daemon$RANDOM_NUMBER:/tmp/uploads/
if [ $? -ne 0 ]; then
    echo "Erreur lors de la copie du fichier dans clamav_daemon$RANDOM_NUMBER"
    exit 1
fi

docker cp "$FILE_TO_SCAN" python_analyze$RANDOM_NUMBER:/tmp/uploads/
if [ $? -ne 0 ]; then
    echo "Erreur lors de la copie du fichier dans python_analyze$RANDOM_NUMBER"
    exit 1
fi

docker cp $WORK_DIR/src_analyze python_analyze$RANDOM_NUMBER:/tmp/
if [ $? -ne 0 ]; then
    echo "Erreur lors de la copie du répertoire src_analyze dans python_analyze$RANDOM_NUMBER"
    exit 1
fi

docker exec clamav_daemon$RANDOM_NUMBER ls /tmp/uploads/
if [ $? -ne 0 ]; then
    echo "Erreur : le fichier n'a pas été trouvé dans clamav_daemon$RANDOM_NUMBER"
    exit 1
fi

rm "/uploads/$FILE_NAME"
if [ $? -ne 0 ]; then
    echo "Erreur : le fichier n'a pas été supprimé sur le serveur"
    exit 1
fi

docker exec python_analyze$RANDOM_NUMBER ls /tmp/uploads/
if [ $? -ne 0 ]; then
    echo "Erreur : le fichier n'a pas été trouvé dans python_analyze$RANDOM_NUMBER"
    exit 1
fi


echo "Tous les fichiers ont été copiés dans les conteneurs."

docker exec clamav_daemon$RANDOM_NUMBER /scan.sh /tmp/uploads/"$FILE_NAME" 
if [ $? -ne 0 ]; then
    echo "Erreur lors de l'exécution du scan ClamAV "
    exit 1
fi

docker exec python_analyze$RANDOM_NUMBER /venv/bin/python3 /tmp/src_analyze/main.py /tmp/uploads/"$FILE_NAME"
if [ $? -ne 0 ]; then
    echo "Erreur lors de l'exécution du scan Python"
    exit 1
fi

echo "Tous les scans ont été effectués."

docker cp clamav_daemon$RANDOM_NUMBER:/tmp/scan_result.txt /script/script_LightningMalware/result/scan_result_clam.txt
if [ $? -ne 0 ]; then
    echo "Erreur lors de la copie des résultats du scan ClamAV"
    exit 1
fi

docker cp python_analyze$RANDOM_NUMBER:/tmp/scan_result.txt /script/script_LightningMalware/result/scan_result_python.txt
if [ $? -ne 0 ]; then
    echo "Erreur lors de la copie des résultats du scan Python"
    exit 1
fi

python3 /script/script_LightningMalware/src_analyze/script_result.py
if [ $? -ne 0 ]; then
    echo "Erreur lors de l'exécution du script de résultats"
    exit 1
fi

echo "Script terminé avec succès."
exit 0
