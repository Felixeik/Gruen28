import pygame
from raum import Raum

class Raum4(Raum):
    def init(self):
        self.rect_breite = 90

    def handleEvent(self, event, spielstand):
        if spielstand.playerX < 46:
            spielstand.inRoom = 3
        
    def handleLogic(self, spielstand):
        pass

    def drawBehindPlayer(self, window, spielstand):
        # Bilder einfügen
        window.blit(self.hintergrund, (0, 0))
        window.blit(self.rahmen, (0, 0))

    def drawInFrontOfPlayer(self, window, spielstand):
        window.blit(self.inventar, (window.get_width() / 2 - 238, 40))