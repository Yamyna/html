#!/bin/bash
RANDOM_NUMBER=$RANDOM
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_DIR="/var/www/logs"
LOGFILE="$LOG_DIR/script_lancement_passwd_${TIMESTAMP}_docker_${RANDOM_NUMBER}.log"

# Créer le répertoire de log si nécessaire et vérifier les permissions
if [ ! -d "$LOG_DIR" ]; then
    mkdir -p $LOG_DIR
    chown www-data:www-data $LOG_DIR
fi
touch $LOGFILE
chown www-data:www-data $LOGFILE

# Redirection de la sortie standard et de la sortie d'erreur
exec > >(tee -a $LOGFILE) 2>&1

# Vérifier si un fichier a été fourni en argument
if [ -z "$1" ]; then
    echo "Usage: $0 <path_to_passwd_file>"
    exit 1
fi

PASSWD_FILE=$1
if [ ! -f "$PASSWD_FILE" ]; then
    echo "The password file does not exist."
    exit 1
fi

# Lire le mot de passe depuis le fichier
PASSWORD=$(cat "$PASSWD_FILE")

WORK_DIR="/script/script_LightningMalware"
PASSWD_ANALYZE_DOCKERFILE_PATH="$WORK_DIR/docker/passwd"

# Construire le conteneur analyze_url et journaliser la sortie
docker build -f $PASSWD_ANALYZE_DOCKERFILE_PATH -t passwd_$RANDOM_NUMBER $WORK_DIR/docker
if [ $? -ne 0 ]; then
    echo "Erreur lors de la construction de l'image passwd_$RANDOM_NUMBER. Voir les logs pour plus de détails."
    exit 1
fi

echo "L'image passwd_$RANDOM_NUMBER a été construite."

# Supprimer tout conteneur existant nommé passwd_$RANDOM_NUMBER
docker rm -f passwd_$RANDOM_NUMBER || true

# Démarrer le conteneur passwd_$RANDOM_NUMBER et journaliser la sortie
docker run -d --name passwd_$RANDOM_NUMBER passwd_$RANDOM_NUMBER /bin/bash
if [ $? -ne 0 ]; then
    echo "Erreur lors du démarrage du conteneur passwd_$RANDOM_NUMBER. Voir les logs pour plus de détails."
    exit 1
fi

echo "Le conteneur passwd_$RANDOM_NUMBER a été démarré."

# Copier le code passwd dans le conteneur et journaliser la sortie
docker cp $WORK_DIR/src_analyze/passwd.py passwd_$RANDOM_NUMBER:/app/passwd.py

# Exécuter le code passwd.py dans le conteneur et journaliser la sortie
docker exec passwd_$RANDOM_NUMBER python3 /app/passwd.py "$PASSWORD"
if [ $? -ne 0 ]; then
    echo "Erreur lors de l'exécution de l'analyse du password. Voir les logs pour plus de détails."
    exit 1
fi

# Copier le résultat
docker cp passwd_$RANDOM_NUMBER:/tmp/scan_result.txt /script/script_LightningMalware/result/scan_result_passwd.txt
if [ $? -ne 0 ]; then
    echo "Erreur lors de la copie des résultats du scan ClamAV. Voir les logs pour plus de détails."
    exit 1
fi

echo "Analyse terminée. Les résultats se trouvent dans /script/script_LightningMalware/result/scan_result_passwd.txt"

exit 0
