#!/bin/bash

# Construire l'image Docker
docker build -t script_url .

# Lancer le conteneur Docker avec l'URL passée en argument
docker run --rm -v $(pwd)/src_analyze_docker:/src_analyze_docker script_url "$1"