#!/bin/bash
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
RANDOM_NUMBER=$RANDOM
LOG_DIR="/var/www/logs"
LOGFILE="$LOG_DIR/script_lancement_url_docker$RANDOM_NUMBER_${TIMESTAMP}.log"

# Créer le répertoire de log si nécessaire et vérifier les permissions
if [ ! -d "$LOG_DIR" ]; then
    mkdir -p $LOG_DIR
    chown www-data:www-data $LOG_DIR
fi
touch $LOGFILE
chown www-data:www-data $LOGFILE

# Redirection de la sortie standard et de la sortie d'erreur
exec > >(tee -a $LOGFILE) 2>&1

echo "Script démarré"

# Vérifier si une URL a été fournie en argument
if [ -z "$1" ]; then
    echo "Usage: $0 <absolute-path-to-url-file>"
    exit 1
fi

URL_FILE=$1

if [ ! -f "$URL_FILE" ]; then
    echo "URL file does not exist: $URL_FILE"
    exit 1
fi

# Lire le contenu du fichier
URL_TO_SCAN=$(cat "$URL_FILE")

WORK_DIR="/script/script_LightningMalware"
URL_ANALYZE_DOCKERFILE_PATH="$WORK_DIR/docker/analyze_url"

echo "Construction de l'image Docker..."
docker build -f $URL_ANALYZE_DOCKERFILE_PATH -t analyze_url$RANDOM_NUMBER $WORK_DIR/docker
if [ $? -ne 0 ]; then
    echo "Erreur lors de la construction de l'image analyze_url"
    exit 1
fi

echo "Image Docker construite avec succès"
echo "Démarrage du conteneur Docker..."
docker run -d --name analyze_url$RANDOM_NUMBER analyze_url$RANDOM_NUMBER /bin/bash
if [ $? -ne 0 ]; then
    echo "Erreur lors du démarrage du conteneur analyze_url"
    exit 1
fi

echo "Conteneur Docker démarré avec succès"

docker cp $WORK_DIR/src_analyze/API_KEY.py analyze_url$RANDOM_NUMBER:/app/API_KEY.py
docker cp $WORK_DIR/src_analyze/analyze_url.py analyze_url$RANDOM_NUMBER:/app/analyze_url.py

docker exec analyze_url$RANDOM_NUMBER /venv/bin/python3 /app/analyze_url.py "$URL_TO_SCAN"
if [ $? -ne 0 ]; then
    echo "Erreur lors de l'exécution du scan URL Python"
    exit 1
fi

docker cp analyze_url$RANDOM_NUMBER:/app/result_url.txt $WORK_DIR/result/result_url.txt
if [ $? -ne 0 ]; then
    echo "Erreur lors de la copie des résultats du scan Python"
    exit 1
fi

echo "Scan terminé avec succès"

python3 /script/script_LightningMalware/src_analyze/script_result.py
if [ $? -ne 0 ]; then
    echo "Erreur lors de l'exécution du script de résultats"
    exit 1
fi

docker rm -f analyze_url$RANDOM_NUMBER

echo "Script finished"
exit 0
