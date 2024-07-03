import os
import secrets
import string
import time

type message = str | None
type erOno = str | None

def open_File(empfänger:str, content:str):
    error: int = 0
    while True:
        if 3 == error:
            return False
        try:
            with open(empfänger, "w")as f:
                f.write(content)
                f.close()
        except Exception as e:
            error =+ 1
            print(e)
            return None

def a_n(empfänger: str, content: str):
    error: int = 0
    while True:
        print(error)
        if 3 == error:
            return None
        try:
            with open(empfänger, "r") as f:
                data = f.read()
                f.close()
        except Exception as e:
            print(e)
            data = "XXX---XXX---534"
            error += 1
            continue
        if data in ["", "XXX---XXX---534", content]:
            error += 1
            continue
        else:
            break
    return data

def c(empfänger: str, content: str):
    time.sleep(3)
    os.remove(empfänger)
    return

def messagen(art: str, empfänger: str, content: str) -> message:
    if open_File(empfänger,content):
        return None
    if art in ["a","n"]:
        return a_n(empfänger, content)
    elif art == "c":
        return c(empfänger, content)

class Coms_F:
    def __init__(self, objekt, kuerzel, id=None) -> None:
        self.file = f'F://Master1/System/KC/{kuerzel}.coms'
        self.id: str = "".join(secrets.choice(string.digits) for _ in range(20))
        self.dat_af: str = f"ConnectingID:{self.id}:Please Connecting building"

    def aufbau(self) -> erOno:
        data = messagen("a", self.file, self.dat_af) or ""
        if data in [self.dat_af, "", None]:
            return "Error Conecting not Posible reason: ???"
        else:
            self.file = f"F://Master1/System/KC/Coms/{data}.coms"
            return None


    def send_message(self, nachricht: str) -> message:
        data = messagen("n", self.file, nachricht) or ""
        if data in [nachricht, "", None]:
            return None
        else:
            return data


    def close(self):
        data = messagen("c", self.file, "Close") or ""
        if data in ["Closed", "", None]:
            return None
        else:
            return data


pass

co = Coms_F("DWOS", "WVS")
print(co.aufbau())

