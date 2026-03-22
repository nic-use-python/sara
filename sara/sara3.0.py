print("\033[92m")
print("starte sara")
import pyttsx3
from ollama import chat
from ollama import ChatResponse
import vosk
from rapidfuzz import fuzz,process
import os
import subprocess as sb
import threading
import time
print("imports fertig")
class settings:
    def __init__(self):
        self.UserName = ""
        self.AImodlle = "llama3.2:latest"
        with open("settings.txt","r") as setting:
            for i, line in enumerate(setting):
                if "=" in line and not line.startswith("#"):
                    setName, newsetting = line.strip().split("=",1)
                    if setName == "UserName":
                        self.UserName = newsetting
                    if setName == "Modlle":
                        self.AImodlle = newsetting
                    if setName == "outcollor":
                        print(newsetting)

        

class brain:
    def __init__(self,tool,modlle):
        self.memory = tool.memory_print()
        self.memory = " ".join(self.memory)
        self.promts = []
        self.modle = modlle
    def ai(self,promt):
        self.memory = tool.memory_print()
        self.memory = " ".join(self.memory)
        syspromt = f"du bist eine nützliche ki, antworte immer auf deutsch , die letzten tools die der user genutzt hat sind : {self.memory}"
        response: ChatResponse = chat(model=self.modle, 
        messages=[
            {
            'role': 'system',
            'content': syspromt,
            },
            {
            'role': 'user',
            'content': promt,
            },
        ])
        self.say(response.message.content)
        return response.message.content
    def say(self,text):
        cmd = f"espeak-ng -v de -s 145 '{text}' | aplay"
        sb.Popen(cmd, shell=True, stdout=sb.DEVNULL, stderr=sb.STDOUT)

class tools:
    def __init__(self):
        self.toollist = []
        self.useabletools = [f for f in os.listdir("/home/nico/Dokumente/sara/tools") 
            if f.endswith('.py') and os.path.isfile(os.path.join("/home/nico/Dokumente/sara/tools", f))]
        for i in range(len(self.useabletools)):
            self.toollist.append("".join(self.useabletools[i]).replace(".py",""))

        print(self.toollist)
        self.memory = []
    def tools_to_use(self):
        return self.toollist
    def memory_print(self):
        return self.memory
    def tooluse(self,inputs):
        output = inputs.futzzing()
        if output == None:
            pass
        else:
            try:
                
                sb.run([" /home/nico/Dokumente/.venv/bin/python", str(self.useabletools[output])], cwd="/home/nico/Dokumente/sara/tools")
                self.memory.append(str(self.toollist[output]))
            except:
                print("error")


class Autostat:
    def __init__(self,ai,tools,inputs):
        self.autostarts =  [f for f in os.listdir("/home/nico/Dokumente/sara/autostart") 
            if f.endswith('.py') and os.path.isfile(os.path.join("/home/nico/Dokumente/sara/autostart", f))]
        self.ai = ai  
        self.tools = tools 
        self.inputs = inputs
    def start_autostart(self,code):
        local_vars = {"ai": self.ai,"print": print, "inputs": self.inputs, "tools": self.tools}
        exec(code, globals(), local_vars)
    def auto(self):
        if len(self.autostarts) != 0:
            for i in range(len(self.autostarts)):
                time.sleep(0.1)
                out2 = open("/home/nico/Dokumente/sara/autostart/" + "".join(self.autostarts[i]),"r")
                out = out2.read()
                t = threading.Thread(target=self.start_autostart,args=(out,), daemon=True)
                t.start()
                out2.close()
                print(f"{"".join(self.autostarts[i])}[Ok]")
class inputs:
    def __init__(self,tool,brain):
        self.toolclass = tool
        self.brain = brain
    def vosk(self):
        return input()
    def futzzing(self):
        inputtxt = self.vosk()
        if "sara" in inputtxt:
            toollist = self.toolclass.tools_to_use()
            ergebnisse = process.extract(inputtxt,toollist,scorer=fuzz.token_sort_ratio,limit= 1)
            if ergebnisse:
                wort , score , index = ergebnisse[0]
                print(ergebnisse)
                print(index)
                if score > 60:
                    self.brain.say("starte" + wort)
                    return index
            else:
                self.brain.ai(inputtxt.replace("sara",""))

print("initialisire classen")
Settings = settings()
tool = tools()
Brain = brain(tool,Settings.AImodlle)
Inputs = inputs(tool,Brain)
autostart = Autostat(Brain,tool,Inputs)
print("classen initialisirt")
print("starte autostart")
autostart.auto()
print("autostarts gestartet")

while True:
    tool.tooluse(Inputs)

############### SARA BETA 1.0 #######################