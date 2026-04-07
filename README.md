## Beschreibung: 



**Sara** ist ein python skript das für einfache automatisirung , als ki assitent / desktopassistent erstellt wurde.
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
- debian:
    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```
- arch:
   ```bash
   sudo pacman -S ollama
   ```
2. modell herunterladen:
   ```bash
   ollama pull llama3.2`
   ```
3. wenn noch nicht instalirt python instaliren(bei linux oft vorinstalirt)
4. venv erstellen:
   ```bash
   python3 -m venv .venv
   ```
6. dann aktiviren:
   ```bash
   'source .venv/bin/activate
   ```
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
 **nutze das passende .bash skript für dein system !!!**
 dann:
 ```batch
sudo ./passendes skript.bash
```
**nutze das was du im letzten befehlgenutzt hast dund passend für dein system ist!**
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
```
## Wichtiges:
**Sara ist noch eie beta . sie hat fehler und ist in entwiklung.**
**ich entwikle momentan eine beta 2.0 dise wede ich hir öfentlich machen sobald sie fertig ist**
## warum ich dise software in meinem projeckt nutze:
- Ollama weil ich damit gute erfarungen habe und es extrem gut mit python funktionirt
- rapidfuzz weil es schneller ist als das oginale thefuzz
- espeak-ng weil pyttsx3 in classen zu fehlern fürt
- llama3.2 weil llama gut auf komplexe systempromts regirt besser als modelle wie phi
- exec weil ich eine einfache trotzdem efiziente lösung für code rinzuladen und da ich hoffe das **jeder plgins selbst erstellt oder von einer fertrauenswürdigen quelle hatt**
### Neue funktonen die es dann in beta 2.0 gibt:
- [x] besserer system promt mit systemauslastung usw intigrirt 
- [ ] autostart wird mit einer regestry ferbessert 
- [x] popups mit notify 
- [ ] plugins/ autostarts könen sich für events regestriren und weden dan ausgefürt 
- [x] selfhealing bei fehlenden modulen 
- [x] mehr plugins 
- [x] email nutzbar 
- **bitte beachten das dise beta 2.0 forerst nicht hier ist und noch privat getestet / entwikelt wird bis alle funktionen fertig sind und getestet sind**
