#!/bin/bash

# Vérifier que le fichier est spécifié
if [ -z "$1" ]; then
    echo "Usage: $0 <file-to-scan>"
    exit 1
fi

#écrire le résultat dans un fichier
clamscan "$1" > /tmp/scan_result.txt

