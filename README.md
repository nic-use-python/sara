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
    debian: 'curl -fsSL https://ollama.com/install.sh | sh'
    arch: 'sudo pacman -S ollama'
2. modell herunterladen:
   -'ollama pull llama3.2' (oder anderes modell das du nutzen wilst bitte dan in settings.txt einfügen)
4. wenn noch nicht instalirt python instaliren(bei linux oft vorinstalirt)
5. venv erstellen:
   'python3 -m venv .venv'
   dann aktiviren:
   'source .venv/bin/activate'
6. im aktivirten venv mit pip nötige liberys/module instaliren:
   -'pip install ollama'
   -'pip install rapidfutzz'
   bei fehlern wegen fehlenden modulen dise nachinstaliren (unvarscheinlich da python es normalerweise automatisch hatt)
7. dann sara3.0.py starten:
   -pfad zu deninem venv überordner.venv/bin/python pfad zu sara3.0.py
