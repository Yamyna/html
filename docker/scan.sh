#!/bin/bash

# Vérifier que le fichier est spécifié
if [ -z "$1" ]; then
    echo "Usage: $0 <file-to-scan>"
    exit 1
fi

# Analyser le fichier avec ClamAV
clamscan --infected --multiscan "$1" > /dev/null

#écrire le résultat dans un fichier
clamscan "$1" > /tmp/scan_result.txt

