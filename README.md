Beschreibung: Sara ist ein python skript das für einfache automatisirung , als ki assitent / desktopassistent erstellt wurde.
Funktionen:
- Autostart von skripten beim start von sara direckt mit zugrif auf die hauptfunktionen des skriptes wie : tts , ollama anfragen usw
- tools einfach skript ineinen ordner und sara kann sie per befehl ausfüren
- ollama intigration
- befehl matching mit rapidfutzz
- einfache settings mit datei
Besonderheiten:
- komplet offline
- einfach erweiterbar
Instalation:
1. ollama instaliren:
    debian: ```bash
curl -fsSL https://ollama.com/install.sh | sh```
    arch: ```bash
   sudo pacman -S ollama```
3. modell herunterladen:
   ```bash
   ollama pull llama3.2```
4. wenn noch nicht instalirt python instaliren(bei linux oft vorinstalirt)
5. venv erstellen:
   ```bash
   python3 -m venv .venv
   ```
   dann aktiviren:
   ```bsah
   'source .venv/bin/activate```
7. im aktivirten venv mit pip nötige liberys/module instaliren:
   ```bash
   pip install ollama
   ```
   ```bash
   pip install rapidfutzz
   ```
   bei fehlern wegen fehlenden modulen dise nachinstaliren (unvarscheinlich da python es normalerweise automatisch hatt)
9. dann sara3.0.py starten:
   -pfad zu deninem venv überordner.venv/bin/python pfad zu sara3.0.py
