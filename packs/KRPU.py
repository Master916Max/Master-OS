# Kernel Running Procressing Updater
import os

def update() -> bool :
    path = os.getcwd()
    os.chdir("F://Master1/System/KC")
    data = ""
    try:
        with open("OS.coms", "r") as file:
            data = file.read()
            file.close()
    except FileNotFoundError:
        print("System Closed")
        data = "Crashed"
    if data in ["Stop", "Crashed"]:
        return False
    else:
        return True


