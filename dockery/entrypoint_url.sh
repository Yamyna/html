#!/bin/bash

# Copiez le script Python et les clés API dans le répertoire approprié
cp /src_analyze_docker/analyze_url.py /analyze_url.py
cp /src_analyze_docker/API_KEY.py /API_KEY.py

# Exécuter le script Python avec l'URL passée en argument
python3 /analyze_url.py "$1"