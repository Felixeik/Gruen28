import pygame
from raum import Raum

class Raum5(Raum):
    def init(self):
        # Fackel initialisieren
        self.fackel_sprite = pygame.image.load("sprites/fackel-grabkammer-sprite.png").convert_alpha()
        self.fackel_width = 47
        self.fackel_height = 183

        self.fackel_frame_width = 45
        self.fackel_frame_height = 182
        self.fackel_num_frames = 4

        # Sarkophag initialisieren
        self.sarkophag_sprite = pygame.image.load("sprites/sarkophag-sprite.png").convert_alpha()
        self.sarkophag_width = 0
        self.sarkophag_height = 0
        
        self.sarkophag_frame_width = 848
        self.sarkophag_frame_height = 500
        self.sarkophag_num_frames = 7
        
        self.fackel_frames = self.extract_frames(self.fackel_sprite, self.fackel_frame_width, self.fackel_frame_height, self.fackel_num_frames)
        self.sarkophag_frames = self.extract_frames(self.sarkophag_sprite, self.sarkophag_frame_width, self.sarkophag_frame_height, self.sarkophag_num_frames)

        # Animationsparameter
        self.frame_fackel_index = 0
        self.frame_sarkophag_index = 0
        self.frame_delay = 150  # Verzögerung zwischen Frames
        self.last_frame_time_fackel = pygame.time.get_ticks()
        self.last_frame_time_sarkophag = pygame.time.get_ticks()
        self.frame_counter = 0

        self.pharao_erwacht = False

        

    def extract_frames(self, sprite_sheet, sprite_width, sprite_height, num_frames):
        frames = []
        for i in range(num_frames):
            frame = sprite_sheet.subsurface(pygame.Rect(i * sprite_width, 0, sprite_width, sprite_height))
            frames.append(frame)
        return frames

    def handleEvent(self, event, spielstand):
        # Maus klicken
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)

            if x == 361 and y == 325:
                self.pharao_erwacht = True
           
    def handleLogic(self, spielstand):
        pass
        

    def drawBehindPlayer(self, window, spielstand):
        # Bilder einfügen
        window.blit(self.hintergrund, (0, 0))
        window.blit(self.rahmen, (0, 0))
        window.blit(self.inventar, (window.get_width() / 2 - 238, 40))

        self.animate_torch(window)
        window.blit(self.sarkophag_frames[0],(-24, 32))
        
        if self.pharao_erwacht:
            self.animate_sarkophag(window)
        

    def animate_torch(self, window):
        current_time = pygame.time.get_ticks()  # Hole die aktuelle Zeit

        # Wenn genug Zeit vergangen ist, ändere den Frame der Fackel
        if current_time - self.last_frame_time_fackel >= self.frame_delay:
            self.frame_fackel_index = (self.frame_fackel_index + 1) % self.fackel_num_frames  # Nächster Frame (zyklisch)
            self.last_frame_time_fackel = current_time  # Aktualisiere die Zeit des letzten Frame-Wechsels

        # Aktuelles Frame der Fackel anzeigen
        current_frame = self.fackel_frames[self.frame_fackel_index]
        window.blit(current_frame, (255, 226)) 


    def animate_sarkophag(self, window):
        current_time = pygame.time.get_ticks()  # Hole die aktuelle Zeit

        # Wenn genug Zeit vergangen ist, ändere den Frame der Fackel
        if current_time - self.last_frame_time_sarkophag >= self.frame_delay:
            self.frame_sarkophag_index = (self.frame_sarkophag_index + 1) % self.sarkophag_num_frames  # Nächster Frame (zyklisch)
            self.last_frame_time_sarkophag = current_time  # Aktualisiere die Zeit des letzten Frame-Wechsels

        # Aktuelles Frame der Fackel anzeigen
        current_frame = self.sarkophag_frames[self.frame_sarkophag_index]
        window.blit(current_frame, (-24, 32)) 



    def drawInFrontOfPlayer(self, window, spielstand):
        window.blit(self.inventar, (window.get_width() / 2 - 238, 40))
