import pygame
from raum import Raum

class Raum1(Raum):
    def init(self):
        # Spinne initialisieren
        self.spinne_width = 86
        self.spinne_height = 34

        self.spinneX = 50
        self.spinneY = 425 - self.spinne_height
        self.spinne_speed = 8
        self.spinne_anzeigen = False

        self.spinne = pygame.Rect(self.spinneX, self.spinneY,  self.spinne_width,  self.spinne_height)
        self.spinne_sprite = pygame.image.load("sprites/spinne-sprite.png").convert_alpha()

        # Parameter des Sprite-Sheets
        self.sprite_width = 345 # Breite eines Frames
        self.sprite_heigt = 136  # Höhe eines Frames
        self.num_frames = 3  # Anzahl der Frames

        # Frames aus Sprite-Sheet extrahieren
        self.frames = []
        for i in range(self.num_frames):
            self.frame =  self.spinne_sprite.subsurface(pygame.Rect(i * self.sprite_width, 0, self.sprite_width, self.sprite_heigt))
            scaled_frame = pygame.transform.scale(self.frame, (self.spinne_width, self.spinne_height)) 
            self.frames.append(scaled_frame)
        
        self.frames[:] = [pygame.transform.flip(frame, True, False) for frame in self.frames]

        # Animationsparameter
        self.frame_index = 0
        self.frame_delay = 15  # Verzögerung zwischen Frames
        self.frame_counter = 0

        self.spinne_anzeigen = False

        self.papierrolle_anzeigen = True
        self.papierrolleX = 755
        self.papierrolleY = 365

        self.papierrolle_img = pygame.image.load("items/papierrolle-inventar.png").convert_alpha()
        self.papierrolle_img = pygame.transform.scale(self.papierrolle_img, (56, 40))

        self.papierrolle_item = pygame.image.load("items/papierrolle-item.png").convert_alpha()
        self.papierrolle = pygame.Rect(self.papierrolleX, self.papierrolleY , self.papierrolle_item.get_width(), self.papierrolle_item.get_height())

        self.pinsel_anzeigen = True
        self.pinsel_ausgewählt = False
        self.pinselX = 75
        self.pinselY = 400

        self.pinsel_img = pygame.image.load("items/Pinsel.png").convert_alpha()
        self.pinsel_img = pygame.transform.scale(self.pinsel_img, (30, 30))
        self.pinsel = pygame.Rect(self.pinselX, self.pinselY, self.pinsel_img.get_width(), self.pinsel_img.get_height())

    def handleEvent(self, event, spielstand):
        # Maus klicken
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
            
            if spielstand.playerX >= 650 and self.papierrolle.collidepoint(x,y):
                spielstand.item_einsammeln(spielstand.items["papierrolle"])
                self.papierrolle_anzeigen = False
                self.spinne_anzeigen = True

            if spielstand.playerX <= 125 and self.pinsel.collidepoint(x,y):
                spielstand.item_einsammeln(spielstand.items["pinsel"])
                self.pinsel_anzeigen = False

                
            # Überprüfen, ob das Item im Inventar angeklickt wurde (z.B. Papierrolle)
            if spielstand.items["papierrolle"] in spielstand.inventar:
                papierrolle_x = spielstand.item_slots[spielstand.inventar.index(spielstand.items["papierrolle"])]
                if papierrolle_x <= x <= papierrolle_x + 40 and 440 <= y <= 485:
                    # Wenn Papierrolle angeklickt wird, setze das Flag auf True
                    if spielstand.flags["papierrolleAnzeigen"]:
                        spielstand.flags["papierrolleAnzeigen"] = False
                    else:
                        spielstand.flags["papierrolleAnzeigen"] = True

            if spielstand.flags["goldKnopfSichtbar"] and 185 <= x <= 205 and 300 <= y <= 320 and 70 <= spielstand.playerX <= 230:
                self.hintergrund = pygame.image.load("raum-hintergründe/raum1.3.png")
                spielstand.flags["raum1Offen"] = True

            if self.pinsel_ausgewählt and 185 <= x <= 205 and 300 <= y <= 320 and 70 <= spielstand.playerX <= 230:
                self.hintergrund = pygame.image.load("raum-hintergründe/raum1.2.png")
                spielstand.flags["goldKnopfSichtbar"] = True

            if spielstand.items["pinsel"] in spielstand.inventar:
                pinsel_x = spielstand.item_slots[spielstand.inventar.index(spielstand.items["pinsel"])]
                if pinsel_x <= x <= pinsel_x + 40 and 440 <= y <= 485:
                    self.pinsel_ausgewählt = True
                    print("pinsel ausgewählt")
                else:
                    self.pinsel_ausgewählt = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and 430 <= spielstand.playerX <= 560 and spielstand.flags["raum1Offen"] == True:
                spielstand.inRoom = 2

    def handleLogic(self, spielstand, player): 
        if self.spinne_anzeigen and self.spinne.colliderect(player.hitbox):
            self.spinne.x = 50
            spielstand.inventar.pop()
            spielstand.inRoom = 0
            self.spinne_anzeigen = False
            self.papierrolle_anzeigen = True


    def drawBehindPlayer(self, window, spielstand):
        # Bilder einfügen
        window.blit(self.hintergrund, (0, 0))
        window.blit(self.rahmen, (0, 0))
        window.blit(self.inventar, (window.get_width() / 2 - 238, 40))

        if self.spinne_anzeigen:
            self.spinne_current = self.frames[self.frame_index]
            self.frame_index +=1

            if self.frame_index == 2:
                self.frame_index = 0
                self.spinne.x += self.spinne_speed

            if self.spinne.x + self.spinne_width >= window.get_width() - 45:
                self.spinne_anzeigen = False

            window.blit (self.spinne_current, (self.spinne.x, self.spinne.y))
            # pygame.draw.rect(window, (255, 0, 0), self.spinne, 2)

        if self.papierrolle_anzeigen:
         window.blit (self.papierrolle_item, (self.papierrolleX , self.papierrolleY ))
        
        if self.pinsel_anzeigen:
            window.blit (self.pinsel_img, (self.pinselX , self.pinselY ))

    
    def drawInFrontOfPlayer(self, window, spielstand):

        window.blit(self.inventar, (window.get_width() / 2 - 238, 40))
        # Wenn das Flag gesetzt ist, Papierrolle dauerhaft anzeigen
        if spielstand.flags["papierrolleAnzeigen"]:
            papierrolle_groß = pygame.image.load("items/papierrolle-groß.png").convert_alpha()
            papierrolle_groß = pygame.transform.scale(papierrolle_groß, (237, 250))
            window.blit(papierrolle_groß, ((window.get_width() - 237) // 2, (window.get_height() - 250) // 2))