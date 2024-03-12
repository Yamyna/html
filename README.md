# LightningMalware

## Table des matières
- [Liens](#Liens)
- [Prérequis](#Prérequis)
- [Anti-virus utilisé pour l'analyse des fichiers](#anti-virus-utilisé-pour-lanalyse-des-fichiers)

## Liens
[https://lightningmalware.fr/](https://lightningmalware.fr/)

Site web qui va analyser les url et les fichiers pour s'assurer qu'il n'y a pas de virus. 

Projet inspiré de [Virus Total](https://www.virustotal.com/gui/home/upload).

## Prérequis
1. Créer un environnement virtuel python 
  ```
    python3 -m venv venv
  ```

2. Activer l'environnement virtuel
  ```
  source venv/bin/activate
  ```
3. Installer ces bibliothèques
  ```
    pip install pyClamd
    pip install OTXv2
  ```

## Anti-virus utiliser pour l'analyse des fichiers
- ClamAV


## API utiliser pour l'analyse des url
- Google
- OTX


