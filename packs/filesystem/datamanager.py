from packs.filesystem.Strukture import File, Folder, Drive, Parent
from packs.filesystem.Tokens import TokenManager, TokenID

class DataManager:
    def __init__(self) -> None:
        self.drive = Drive("Main", "M")
        self.token_manager = TokenManager()

    def test_tree(self):
        self.id = TokenID("Max", self.token_manager)
        self.folder1 = Folder("Max", self.id)
        self.folder1.set_parent(Parent(self.folder1, parent_drive=self.drive))

        self.test_pro = File("Test.pa", "print('Hello World')")
        self.test_pro.set_parent(Parent(self.test_pro, parent_folder=self.folder1))

        self.test_mas = File("Main.pa", "print('Hello World')")
        self.test_mas.set_parent(Parent(self.test_mas, parent_drive=self.drive))

    def get_data(self) -> Drive:
        return self.drive

    def add_drive(self, drive: Drive):
        pass

    def get_main_drive(self) -> Drive:
        return self.drive

    def add_folder(self, name: str, parent: Folder) -> Folder:
        id = TokenID(name, self.token_manager)
        folder = Folder(name=name, id=id)
        parent_folder = Parent(folder, parent_folder=parent)
        folder.set_parent(parent_folder)
        return folder

    def get_object(self, path: str, name: str):
        obj =  12
        tree = self.get_data()
        sys = tree.children
        path_blocks = path.split("|")

        for block in path_blocks:
            print(block, "-> Block")
            tok = self.token_manager.get_token(str(block))
            walk = True

            while walk:
                if len(sys) == 0:
                    return False
                cl = sys[0]
                print(cl, "-> CL")
                if isinstance(cl, Folder):
                    if cl.id.get_tok() == tok:
                        sys = cl.children
                        walk = False
                        print(sys, "-> SYS")
                    elif cl.name == name:
                        return cl
                    else:
                        sys.remove(sys[0])
                elif isinstance(cl, File):
                    if cl.name == name:
                        return cl
                    else:
                        sys.remove(sys[0])
        while walk:
            if len(sys) == 0:
                return False
            cl = sys[0]
            print(cl, "-> CL")
            if isinstance(cl, Folder):
                if cl.name == name:
                    return cl
                else:
                    sys.remove(sys[0])
            elif isinstance(cl, File):
                if cl.name == name:
                    return cl
                else:
                    sys.remove(sys[0])
        
