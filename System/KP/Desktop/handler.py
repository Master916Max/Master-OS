import pygame

class Dataa:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def update(self, x, y):
         self.x = x
         self.y = y
    def main(self, x, y, xa, ya):
         self.x = x - xa
         self.y = y - ya
    

class KeyHandler:
    def __init__(self):
         self.mousepressing = False
         self.apps_num = None
         self.d = Dataa(0,0)
    def update(self, event, app, running):
        if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if app and app.collidepoint(pygame.mouse.get_pos()):
                   running = False
        return running
    def app_u(self, event, apps):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.mousepressing = True
                for num, app in enumerate(apps):
                      if app.collidepoint(event.pos):
                           if self.d.x == 0 and self.d.y == 0:
                            self.d.main(event.pos[0],event.pos[1],app.x, app.y)
                           self.apps_num = num
        if event.type == pygame.MOUSEBUTTONUP:
             if event.button == 1:
                  self.mousepressing = False
                  self.apps_num = None
                  self.d.update(0,0)
        if event.type == pygame.MOUSEMOTION:
             if self.mousepressing:
                if self.apps_num != None:
                    apps[self.apps_num].update_pos(event.pos, self.d)

class Lable:
    def __init__(self, text, text_col, size, x, y):
          self.font = pygame.font.SysFont("Arial", size)
          self.text_col = text_col
          self.img =  self.font.render(text, True, self.text_col)
          self.x = x
          self.y = y

    def update_text(self, text):
        self.img =  self.font.render(text, True, self.text_col)

    def print(self, screen):
         screen.blit(self.img, (self.x,self.y))

class Button:
     def __init__(self, text, text_col, size, x, y, width, height):
          self.font = pygame.font.SysFont("Arial", size)
          self.text_col = text_col
          self.img =  self.font.render(text, True, self.text_col)
          self.x = x
          self.y = y
          self.width = width
          self.height = height
          self.is_pressed = False
     def update(self, event):
          if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.collidepoint(pygame.mouse.get_pos()):
                   self.is_pressed = True
          elif event.type == pygame.MOUSEBUTTONUP:
                if self.is_pressed:
                   self.is_pressed = False
     def collidepoint(self, pos):
          return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height
     def print(self, screen):
          screen.blit(self.img, (self.x,self.y))

class App:
    pass

class AppManager:
    def __init__(self) -> None:
        self.apps = []
    
    def start_app(self, name: str, type: int):
         if type == 0:
             self.apps.append(App())
         elif type == 1:
             self.apps.append(LoadingApp(name, 300, 200, BAR=1))
    def print(self, screen):
         for app in self.apps:
             app.draw(screen)

class LoadingApp:
    def __init__(self, name, w, h, root: App = None, **addings: dict[str, int]):
        
        self.name = name
        self.w = w
        self.h = h
        self.stand()
        for add, content in addings.items():
            self.adding(add, content)
        if root:
            root.add_child(self)
            self.root = root

    def stand(self):
        self.settings = {"BAR": 0}
        self.x = 500
        self.y = 500

    def adding(self, adding, content):
        self.settings[adding] = content

    def update_pos(self, pos, d: Dataa):
         self.x = pos[0] - d.x
         self.y = pos[1] - d.y

    def update_pos_else(self, rel):
         self.x = rel[0]
         self.y = rel[1]
    
    def title(self):
         self.lable = Lable(self.name, (0,0,0), 20, self.x + 5, self.y + 2)

    def collidepoint(self, pos):
         return self.x <= pos[0] <= self.x + self.w and self.y <= pos[1] <= self.y + 25
    def draw(self, screen):
        if self.settings["BAR"] == 1:
            pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(self.x, self.y, self.w, 25))
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x +(self.w - 25), self.y + 2, 20, 20))
            self.title()
            self.lable.print(screen)
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y +25 , self.w, self.h))
