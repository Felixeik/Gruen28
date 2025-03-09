import pygame
from raum import Raum

class Raum6(Raum):
    def init(self):
        self.platforms = [
            pygame.Rect(0, 437, 120, 10),
            pygame.Rect(295, 441, 1, 10),
            pygame.Rect(455, 445, 1, 10),
            pygame.Rect(615, 437, 1, 10),
            pygame.Rect(760, 441, 60, 10)
        ]

       
        self.on_platform = True

    def handleEvent(self, event, spielstand):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
    
    def handleLogic(self, spielstand, player):

        if not spielstand.playerJumping:
            spielstand.playerSpeedY = 12
            player.rect.y += spielstand.playerSpeedY

        for platform in self.platforms:
            spielstand.boden = platform.y
            if player.rect.colliderect(platform):
                player.rect.y = platform.y - spielstand.playerHeight
                spielstand.playerSpeedY = 0
                self.on_platform = True
                spielstand.canJump = True
                break

            self.on_platform = False

            if not self.on_platform:
                spielstand.canJump = False

            if player.rect.y + spielstand.playerHeight >= 551:
                x, y = self.platforms[0].topleft
                player.rect.x = x / 2
                player.rect.y = self.platforms[0].y - spielstand.playerHeight
            
            if player.rect.x + spielstand.playerWidth >= 848:
                spielstand.inRoom = 7
                player.rect.x = player.rect.x -848

        
    
    def drawBehindPlayer(self, window, spielstand):
        window.blit(self.hintergrund, (0, 0))
    
    def drawInFrontOfPlayer(self, window, spielstand):
        pass
