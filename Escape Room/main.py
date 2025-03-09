import pygame
import player
from raum import Raum
from raum0 import Raum0
from raum1 import Raum1
from raum2 import Raum2
from raum3 import Raum3
from raum4 import Raum4
from raum5 import Raum5
from raum6 import Raum6
from raum7 import Raum7
from raum8 import Raum8

class Spielstand:
    def __init__(self, inRoom = 1):
        self.inRoom = inRoom
        self.frameCount = 0
        self.timeCountSec = 0
        self.boden = 425
        self.playerWidth = 92 
        self.playerHeight = 166
        self.playerX = 265
        self.playerY = self.boden - self.playerHeight
        self.playerJumping = False
        self.canJump = True
        self.playerCrouching = False
        self.playerSpeedY = 10
        self.inventar = []
        self.item_slots = [235, 290, 346, 402, 458, 514, 570]
        self.items = {
            "papierrolle": Item("Papierrolle", "items/papierrolle-inventar.png"),
            "pinsel": Item("Pinsel", "items/pinsel.png")
        }
        self.flags = {
            "papierrolleAnzeigen": False,
            "goldKnopfSichtbar":  False,
            "raum1Offen": False,
        }
    
    # Funktion, um ein Item zu sammeln
    def item_einsammeln(self, item):
        if item not in self.inventar:
            self.inventar.append(item)

class Item:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.icon = pygame.image.load(url)
        self.icon = pygame.transform.scale(self.icon, (40, 40))

class Game:
    def __init__(self):
        pygame.init()
        self.window_width = 848
        self.window_height = 500
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Escape Run")
        self.spielstand = Spielstand()
        self.player = player.Player(self)
        self.initRaeume()
        self.run()

    def initRaeume(self):
        self.raum0 = Raum0("")
        self.raum1 = Raum1("raum-hintergründe/raum1.1.png")
        self.raum2 = Raum2("raum-hintergründe/raum2.gif")
        self.raum3 = Raum3("raum-hintergründe/raum3.1.png")
        self.raum4 = Raum4("raum-hintergründe/raum4.png")
        self.raum5 = Raum5("raum-hintergründe/raum5.png")
        self.raum6 = Raum6("raum-hintergründe/raum6.png")
        self.raum7 = Raum7("raum-hintergründe/raum7.png")
        self.raum8 = Raum8("raum-hintergründe/raum8.png")


    def zeichneInventar(self):
        for i, item in enumerate(self.spielstand.inventar):
            self.window.blit(item.icon, (self.spielstand.item_slots[i], self.window_height - 55))

    def run(self):
        running = True
        while running:
            self.window.fill((0, 0, 0))

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.spielstand.inRoom = 0
                    if event.key == pygame.K_1:
                        self.spielstand.inRoom = 1
                    elif event.key == pygame.K_2:
                        self.spielstand.inRoom = 2
                    elif event.key == pygame.K_3:
                        self.spielstand.inRoom = 3
                    elif event.key == pygame.K_4:
                        self.spielstand.inRoom = 4
                    elif event.key == pygame.K_5:
                        self.spielstand.inRoom = 5
                    elif event.key == pygame.K_6:
                        self.spielstand.inRoom = 6
                    elif event.key == pygame.K_7:
                        self.spielstand.inRoom = 7
                    elif event.key == pygame.K_8:
                        self.spielstand.inRoom = 8


                if self.spielstand.inRoom == 0:
                    self.raum0.handleEvent(event, self.spielstand)
                elif self.spielstand.inRoom == 1:
                    self.raum1.handleEvent(event, self.spielstand)
                elif self.spielstand.inRoom == 2:
                    self.raum2.handleEvent(event, self.spielstand)
                elif self.spielstand.inRoom == 3:
                    self.raum3.handleEvent(event, self.spielstand)
                elif self.spielstand.inRoom == 4:
                    self.raum4.handleEvent(event, self.spielstand)
                elif self.spielstand.inRoom == 5:
                    self.raum5.handleEvent(event, self.spielstand)
                elif self.spielstand.inRoom == 6:
                    self.raum6.handleEvent(event, self.spielstand)
                elif self.spielstand.inRoom == 7:
                    self.raum7.handleEvent(event, self.spielstand)
                elif self.spielstand.inRoom == 8:
                    self.raum8.handleEvent(event, self.spielstand)
                
            # Bildwiederholrate und Zeitmessung
            self.spielstand.frameCount +=1
            self.spielstand.timeCountSec += pygame.time.Clock().tick(60) / 1000

            # Raumlogik und Raum zeichnen (alles hinter dem Spieler)
            if self.spielstand.inRoom == 0:
                self.raum0.handleLogic(self.spielstand)
                self.raum0.drawBehindPlayer(self.window, self.spielstand)
            if self.spielstand.inRoom == 1:
                self.raum1.handleLogic(self.spielstand,self.player)
                self.raum1.drawBehindPlayer(self.window, self.spielstand)
            elif self.spielstand.inRoom == 2:
                self.raum2.handleLogic(self.spielstand)
                self.raum2.drawBehindPlayer(self.window, self.spielstand)
            elif self.spielstand.inRoom == 3:
                self.raum3.handleLogic(self.spielstand)
                self.raum3.drawBehindPlayer(self.window, self.spielstand)
            elif self.spielstand.inRoom == 4:
                self.raum4.handleLogic(self.spielstand)
                self.raum4.drawBehindPlayer(self.window, self.spielstand)
            elif self.spielstand.inRoom == 5:
                self.raum5.handleLogic(self.spielstand)
                self.raum5.drawBehindPlayer(self.window, self.spielstand)
            elif self.spielstand.inRoom == 6:
                self.raum6.handleLogic(self.spielstand, self.player)
                self.raum6.drawBehindPlayer(self.window, self.spielstand)
            elif self.spielstand.inRoom == 7:
                self.raum7.handleLogic(self.spielstand, self.player)
                self.raum7.drawBehindPlayer(self.window, self.spielstand)
            elif self.spielstand.inRoom == 8:
                self.raum8.handleLogic(self.spielstand, self.player)
                self.raum8.drawBehindPlayer(self.window, self.spielstand)


            # Spieler aktualisieren
            if self.spielstand.inRoom > 0:
                self.player.update()

            # Raum zeichnen (alles vor dem Spieler)
            if self.spielstand.inRoom == 0:
                self.raum0.drawInFrontOfPlayer(self.window, self.spielstand)
            elif self.spielstand.inRoom == 1:
                self.raum1.drawInFrontOfPlayer(self.window, self.spielstand)
            elif self.spielstand.inRoom == 2:
                self.raum2.drawInFrontOfPlayer(self.window, self.spielstand)
            elif self.spielstand.inRoom == 3:
                self.raum3.drawInFrontOfPlayer(self.window, self.spielstand)    
            elif self.spielstand.inRoom == 4:
                self.raum4.drawInFrontOfPlayer(self.window, self.spielstand)          
            elif self.spielstand.inRoom == 5:
                self.raum5.drawInFrontOfPlayer(self.window, self.spielstand)
            elif self.spielstand.inRoom == 6:
                self.raum6.drawInFrontOfPlayer(self.window, self.spielstand)
            elif self.spielstand.inRoom == 7:
                self.raum7.drawInFrontOfPlayer(self.window, self.spielstand)
            elif self.spielstand.inRoom == 8:
                self.raum8.drawInFrontOfPlayer(self.window, self.spielstand)
            

            if self.spielstand.inRoom > 0:
                self.zeichneInventar()

            # Aktualisiert screen
            pygame.display.flip()

    pygame.quit()

game = Game()

