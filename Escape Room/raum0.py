import pygame
from raum import Raum

class Raum0(Raum):
    def init(self):
        self.hilfe_aktiv = False

    def handleEvent(self, event, spielstand):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE: # Enter zum Spielstart
                spielstand.inRoom = 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect_hilfe.collidepoint(mouse_pos):
                self.hilfe_aktiv = True

    def handleLogic(self, spielstand):
        pass

    def drawBehindPlayer(self, window, spielstand):
        WEISS = (255,255,255)
        SCHWARZ = (0, 0, 0)

        self.hintergrund = pygame.image.load("raum-hintergründe/raum0.jpeg")
        window.blit(self.hintergrund, (0, 0))
        
        # Text für Titel
        titel_font = pygame.font.Font("NeoBulletin Trash.ttf", 60) # Dateiname und Schrifgröße
        titel_text = titel_font.render("Escape Run", True, SCHWARZ) # Titel und Farbe
        rect_titel = titel_text.get_rect(center=(window.get_width() / 2, window.get_height() / 3))
        window.blit(titel_text, rect_titel)

        # Text für Informationen
        info_font = pygame.font.Font("NeoBulletin Trash.ttf", 30) # Dateiname und Schrifgröße
        info_text = info_font.render("Drücke Enter, um zu starten!", True, SCHWARZ) # Ttitel und Farbe
        rect_info = info_text.get_rect(center=(window.get_width() / 2, window.get_height() / 2)) 
        window.blit(info_text, rect_info)

        # Hilfe
        hilfe_font = pygame.font.Font(None, 30)
        hilfe_text = hilfe_font.render("Spielanleitung", True, SCHWARZ)
        self.rect_hilfe = hilfe_text.get_rect(center=(window.get_width() / 2, window.get_height() -65))
        window.blit(hilfe_text, self.rect_hilfe)
        window.blit(self.rahmen, (0, 0))

        
    
    def drawInFrontOfPlayer(self, window, spielstand):
        WEISS = (255,255,255)
        SCHWARZ = (0,0,0)
        while self.hilfe_aktiv:

            y_offset = 100  # Startposition für die Y-Koordinate

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN: # ESC zum Verlassen
                    if event.key == pygame.K_ESCAPE:
                        self.hilfe_aktiv = False

            window.fill(SCHWARZ)

            bg = pygame.image.load("Rahmen.png") # Hintergrund Rahmen
            window.blit(bg, (0, 0))

            self.hintergrund = pygame.image.load("titelbild_optimiert.jpg")
            window.blit(self.hintergrund, (0, 0))
        


            font = pygame.font.Font(None, 30) # Schriftart

            #Anleitungstext
            anleitung = [
                "Benutze die Tasten W A S D, um den Archeologen zu bewegen.",
                "Drücke die Leerstaste, um zu springen.",
                "Drücke Shift, um zu crouchen.",
                "Deine Aufgabe ist es:",
                "Finde den Weg aus der Pyramide!",
                "Viel Spaß beim Spielen von:",
                "ESCAPE RUN", 
                "-------------",
                "Drücke ESC, um zurückzukehren!"
            ]

            for line in anleitung:
                text_surface = font.render(line, True, SCHWARZ)
                text_rect = text_surface.get_rect(center=(window.get_width() / 2 , y_offset + 20))
                window.blit(text_surface, text_rect)
                y_offset += 40  # Abstand Zeilen

            pygame.display.flip()