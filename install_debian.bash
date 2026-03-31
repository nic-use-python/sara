#!/bin/bash
# Prüfen, ob das Skript als root/sudo ausgeführt wird
if [[ $EUID -ne 0 ]]; then
   echo "Bitte starte das Skript mit sudo!"
   read -p "Drücke Enter zum Schließen..." 
   exit 1
fi


read -p "Dises programm wird änderungen an deinem PC / system vornemehn ! Möchtest du fortfahren? (y/n): " choice

if [[ "$choice" != "y" && "$choice" != "Y" ]]; then
    echo "Abgebrochen."
    exit 1
fi

echo "Weiter geht's..."
echo "instaliere ollama und espeak-ng"

curl -fsSL https://ollama.com/install.sh | sh
sudo apt install espeak-ng -y
echo "ollama läd jetzt llama 3.2"
ollama pull llama3.2:latest
echo "erstelle neues venv"
python3 -m venv .venv
source .venv/bin/activate
echo "starte installationen mit pip von ollama-python libery , rapidfutzz"
./.venv/bin/pip ollama rapidfuzz
apt moo
read -p "programm abgeschlossen. Drücke Enter zum Schließen..." 
