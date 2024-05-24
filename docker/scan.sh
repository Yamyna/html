#!/bin/bash

# Vérifier que le fichier est spécifié
if [ -z "$1" ]; then
    echo "Usage: $0 <file-to-scan>"
    exit 1
fi

# Analyser le fichier avec ClamAV
clamscan "$1"