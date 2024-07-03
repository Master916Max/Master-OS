from packs.filesystem.Strukture import File

def Open():
    pass

class Datei:
    def __init__(self, file: File) -> None:
        self.File_content = file.code
    def get(self) -> str:
        return self.File_content
