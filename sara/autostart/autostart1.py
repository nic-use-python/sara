# Nutze die Namen, die du in local_vars übergeben hast
print("Autostart läuft...")
memory = tools.memory_print()
ai.say("Das Gedächtnis ist: " + " ".join(memory))
