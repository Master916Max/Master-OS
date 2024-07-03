import random
import string


class TokenManager:
    def __init__(self) -> None:
        self.tokens = {}

    
    def add_token(self, name: str) -> None:
        loop = True
        while loop:
            tok = get_token(name)
            if tok in self.tokens.values():
                continue
            else:
                self.tokens[name] = tok
                loop = False
    
    def get_token(self, name: str) -> str:
        return self.tokens[name]
    
    def get_all(self) -> dict:
        return self.tokens

class TokenID:
    def __init__(self, name: str, toke: TokenManager):
        self.name = name
        toke.add_token(self.name)
        self.tok = toke.get_token(self.name)
    
    def get_tok(self):
        return self.tok

def get_token(name: str) -> str:
    return ''.join(random.choice(string.ascii_letters) for i in range(30))

