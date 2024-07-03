from packs.filesystem.Tokens import TokenID

class File:
    def __init__(self, name: str, code: str) -> None:
        self.name: str = name
        self.code: str = code
    
    def set_parent(self, parent):
        self.parent: Parent = parent
    
    def __repr__(self) -> str:
        return f'File({self.name}, {self.code})'


class Folder:
    def __init__(self, name: str, id: TokenID):
        self.name = name
        self.id = id
        self.children = []
    
    def set_parent(self, parent):
        self.parent: Parent = parent
    
    def add_Child(self, progarmm):
        self.children.append(progarmm)

    def __repr__(self) -> str:
        return f'Folder(Name:{self.name},Content:{self.children})'


class Drive:
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id
        self.children = []
    
    def add_Child(self, progarmm):
        self.children.append(progarmm)

    def __repr__(self) -> str:
        return f'Drive({self.name}, {self.id}, {self.children})'


class Parent:
    def __init__(self, child: object, parent_folder: Folder = None, parent_drive: Drive = None) -> None: # type: ignore
        self.parent_folder = parent_folder
        self.parent_drive = parent_drive
        if self.parent_folder:
            self.parent = self.parent_folder
        else:
            self.parent = self.parent_drive
        
        self.parent.add_Child(child)

