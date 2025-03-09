import pygame

class Raum:
    def __init__(self, dateiname_hintergrund, dateiname_rahmen = "rahmen.png", dateiname_inventar = "inventar.png"):
        if dateiname_hintergrund:
            self.hintergrund = pygame.image.load(dateiname_hintergrund)
        self.rahmen = pygame.image.load(dateiname_rahmen).convert_alpha()
        self.inventar = pygame.image.load(dateiname_inventar).convert_alpha()
        self.init()
    
    def init(self):
        pass

    def handleEvent(self, event, spielstand):
        pass

    def handleLogic(self, spielstand, player):
        pass

    def drawBehindPlayer(self, window, spielstand):
        # Bilder einfügen
        window.blit(self.hintergrund, (0, 0))
        window.blit(self.rahmen, (0, 0))
    
    def drawInFrontOfPlayer(self, window, spielstand):
        window.blit(self.inventar, (window.get_width() / 2 - 238, 40))