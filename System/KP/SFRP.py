import os

def create_sccf_files(directory, count):
    """Erstellt die SCCF-Dateien im angegebenen Verzeichnis."""
    for i in range(1, count + 1):
        file_path = os.path.join(directory, f"coms{i}.sccf")
        with open(file_path, 'w') as f:
            f.write(f"SCCF File {i}")
        print(f"Created {file_path}")

def create_kc_files(directory, kp_names):
    """Erstellt die KC-Dateien im angegebenen Verzeichnis."""
    for kp_name in kp_names:
        file_path = os.path.join(directory, f"{kp_name}.coms")
        with open(file_path, 'w') as f:
            f.write(f"KC File for {kp_name}")
        print(f"Created {file_path}")

def P1():
    """Erstellt KC-Dateien."""
    try:
        create_kc_files('F://Master1/System/KC', ['KP1', 'KP2'])  # Beispiel: KC-Dateien für KP1 und KP2 erstellen
        return None, 0  # Kein Fehler
    except Exception as e:
        return str(e), 1  # Fehler aufgetreten

def P2():
    """Überprüft, ob der KC-Ordner vorhanden ist, und erstellt ihn falls nötig."""
    try:
        kc_directory = 'F://Master1/System/KC'
        if not os.path.exists(kc_directory):
            os.makedirs(kc_directory)
            print(f"Created directory: {kc_directory}")
        error, code = P1()  # P1 aufrufen, um die KC-Dateien zu erstellen
        return error, code
    except Exception as e:
        return str(e), 1  # Fehler aufgetreten

def P3():
    """Erstellt SCCF-Dateien."""
    try:
        create_sccf_files('F://Master1/System/SCCF', 5)  # Beispiel: 5 SCCF-Dateien erstellen
        return None, 0  # Kein Fehler
    except Exception as e:
        return str(e), 1  # Fehler aufgetreten

def P4():
    """Überprüft, ob der SCCF-Ordner vorhanden ist, und erstellt ihn falls nötig."""
    try:
        sccf_directory = 'F://Master1/System/SCCF'
        if not os.path.exists(sccf_directory):
            os.makedirs(sccf_directory)
            print(f"Created directory: {sccf_directory}")
        error, code = P3()  # P3 aufrufen, um die SCCF-Dateien zu erstellen
        return error, code
    except Exception as e:
        return str(e), 1  # Fehler aufgetreten
