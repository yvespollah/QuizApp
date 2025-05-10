#!/bin/bash

# Créer un répertoire pour les images s'il n'existe pas
mkdir -p /home/yves/Test/frontend/public/images

# Télécharger le logo Yves Programmeur directement depuis l'URL de l'image
curl -o /home/yves/Test/frontend/public/images/logo.png "https://raw.githubusercontent.com/yvesprogrammeur/assets/main/logo.png"

echo "Logo téléchargé avec succès!"
