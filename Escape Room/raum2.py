import pygame
from raum import Raum

class Raum2(Raum):
    def init(self):
        self.rect_breite = 90
        self.teleportation = False

    def handleEvent(self, event, spielstand):
        if spielstand.playerX > 848 - self.rect_breite - 46:
            self.teleportation = True
            spielstand.inRoom = 3
        if self.teleportation == True:
            spielstand.playerX = 848 - 47
            self.teleportation = False
        
        
    def handleLogic(self, spielstand):
        pass

    def drawBehindPlayer(self, window, spielstand):
        # Bilder einfügen
        window.blit(self.hintergrund, (0, 0))
        window.blit(self.rahmen, (0, 0))

    def drawInFrontOfPlayer(self, window, spielstand):
        window.blit(self.inventar, (window.get_width() / 2 - 238, 40))