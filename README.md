## Beschreibung: Sara ist ein python skript das für einfache automatisirung , als ki assitent / desktopassistent erstellt wurde.
## Funktionen:
- Autostart von skripten beim start von sara direckt mit zugrif auf die hauptfunktionen des skriptes wie : tts , ollama anfragen usw
- tools einfach skript ineinen ordner und sara kann sie per befehl ausfüren
- ollama intigration
- befehl matching mit rapidfutzz
- einfache settings mit datei
## Besonderheiten:
- komplet offline
- einfach erweiterbar
## Instalation:
### Manuell:
1. ollama instaliren:
    debian: ```bash
rl -fsSL https://ollama.com/install.sh | sh```
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
### Automatisch:
```batch
chmod +x passendes skript
```
 nutze das passende .bash skript für dich !!!
 dann:
 ```batch
sudo ./passendes skript.bash
```
nutze das was du im letzten befehlgenutzt hast dund passend für dein system ist!
9. dann sara3.0.py starten:
   -pfad zu deninem venv überordner.venv/bin/python pfad zu sara3.0.py
## Tipps zum entwikeln:
- dateine aufbau und funktion:
├── sara3.0.py       # Der Kern
├── settings.txt     # Einstellungen
├── plugins/         # Deine Autostart-Skripte
└── tools/           # Skripte für manuelle Befehle
- was die plugins bekommen:
    -brain classe als ai
    -inputs classe als inputs
    -tools classe als tools
beichspiele:
- du wist memory lesen also nur .
```python
 memory = tools.memory # gibt liste zurück
```
- du wilst tts nutzen um "hallo" zu sagen also nur
```python
ai.say("hallo")
