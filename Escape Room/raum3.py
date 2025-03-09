import pygame
from raum import Raum

class Raum3(Raum):
    def init(self):
        #Druckplatte
        self.platte_breite = 50
        self.platte_höhe = 30
        self.platte_x = 205
        self.platte_y = 390
        self.platte_triggered = False
        self.hintergrund = pygame.image.load("raum-hintergründe/raum3.1.png")
        self.rect_breite = 90
        self.teleportation = True

    def handleEvent(self, event, spielstand):
        if self.teleportation == True:
            spielstand.playerX = 47
            self.teleportation = False
        if spielstand.playerX < 46:
            self.teleportation = True
            spielstand.inRoom = 2
        # Maus klicken 
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print (x, y)

        # Hitbox spieler
        player_left = spielstand.playerX
        player_right = spielstand.playerX + spielstand.playerWidth
        player_top = spielstand.playerY
        player_bottom = spielstand.playerY + spielstand.playerHeight

        # Druckplatte 
        platte_left = self.platte_x
        platte_right = self.platte_x + self.platte_breite
        platte_top = self.platte_y
        platte_bottom = self.platte_y + self.platte_höhe

        #Überlappung mit Platte
        overlap_x = max(0, min(player_right, platte_right) - max(player_left, platte_left))
        min_overlap_x = spielstand.playerWidth * 0.2 # 20% Überlappung mit Druckplatte
        on_platte = player_bottom >= platte_top and player_bottom - spielstand.playerSpeedY <= platte_top 

        if (overlap_x >= min_overlap_x and on_platte and spielstand.playerSpeedY > 0 and not self.platte_triggered):
            print("Platte triggered")
            self.platte_triggered = True           
            self.hintergrund = pygame.image.load("raum-hintergründe/raum3.2.png")   

        

    def handleLogic(self, spielstand):
        pass
    

    def drawBehindPlayer(self, window, spielstand):
        # Bilder einfügen
        window.blit(self.hintergrund, (0, 0))
        window.blit(self.rahmen, (0, 0))
        window.blit(self.inventar, (window.get_width() / 2 - 238, 40))

        
    
    def drawInFrontOfPlayer(self, window, spielstand):
        window.blit(self.inventar, (window.get_width() / 2 - 238, 40))

        player_rect = pygame.Rect(spielstand.playerX, spielstand.playerY, spielstand.playerWidth, spielstand.playerHeight)
        pygame.draw.rect(window, (255, 0, 0), player_rect, 2)
