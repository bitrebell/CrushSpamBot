import sys
import glob
import importlib
import logging
from pathlib import Path
from sys import argv
from crushbot import *
from crushbot import CrushBot1, CrushBot2, CrushBot3, CrushBot4, CrushBot5

def load_plugs(plugname):
    modules = Path(f"crushbot/plugins/{plugname}.py")
    myfiles = f"crushbot.plugins.{plugname}"
    spec = importlib.util.spec_from_file_location(myfiles, modules)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugname)
    spec.loader.exec_module(load)
    sys.modules["crushbot.plugins." + plugname] = load
    print("CrushSpamBot - Successfully Imported " + plugname)

if __name__ == "__main__":
    modules = "crushbot/plugins/*.py"
    plugins = glob.glob(modules)
    for myfiles in plugins:
        with open(myfiles) as f:
            module = Path(f.name)
            plugname = module.stem
            load_plugs(plugname.replace(".py", ""))

import crushbot
import crushbot.userNeeds
import crushbot.help
import crushbot.helpers.callbackQuery

print("\n\nCrush Spam Bot Deployed Successfully!\n\n")

if len(argv) not in (1, 3, 4):
    try:
        CrushBot1.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        CrushBot2.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        CrushBot3.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        CrushBot4.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        CrushBot5.disconnect()
    except Exception as e:
        print(e)
        pass
else:
    try:
        CrushBot1.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        CrushBot2.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        CrushBot3.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        CrushBot4.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        CrushBot5.run_until_disconnected()
    except Exception as e:
        print(e)
        pass