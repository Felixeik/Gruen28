import pygame

class Player:
    def __init__(self, game):
        self.window = game.window
        self.spielstand = game.spielstand

        self.rect = pygame.Rect(self.spielstand.playerX, self.spielstand.playerY, self.spielstand.playerWidth, self.spielstand.playerHeight)
        self.hitbox = pygame.Rect((self.spielstand.playerX + (self.spielstand.playerWidth / 2)) -10, self.spielstand.playerY, 20, self.spielstand.playerHeight)

        self.walkingSpeedX = 5
        self.character_sprite = pygame.image.load('sprites/character-sprite.png').convert_alpha()

        self.frame_count = 5  # Anzahl der Frames im Sprite-Sheet
        self.frame_delay = 75 # Delay zwischen den Frames in Millisekunden
        self.current_frame = 0  # Start-Frame
        self.last_frame_time = pygame.time.get_ticks()  # Zeit des letzten Frame-Wechsels

        self.moving_right = False
        self.moving_left = False
        self.facing_left = False

    def get_frame(self, frame_number):
        x_pos = frame_number * 184  # Berechnet die x-Position für das aktuelle Frame
        return self.character_sprite.subsurface(pygame.Rect(x_pos, 0, 184, 332))

    def update(self):
        self.movement()
        self.draw()  # Wir kombinieren die Bewegung und das Zeichnen hier

    def draw(self):
        # Berechne die Zeit seit dem letzten Frame-Wechsel
        current_time = pygame.time.get_ticks()

        # Wenn genug Zeit vergangen ist, wechsle das Frame
        if current_time - self.last_frame_time >= self.frame_delay:
            self.last_frame_time = current_time
            if self.moving_left or self.moving_right:
                self.current_frame = (self.current_frame + 1) % self.frame_count
            else:
                self.current_frame = 0  # Wenn nicht in Bewegung, bleibe im Standbild

        # Hole das aktuelle Frame
        char_frame = self.get_frame(self.current_frame)

        # Wenn der Charakter nach links schaut, flippe das Sprite
        if self.facing_left:
            char_frame = pygame.transform.flip(char_frame, True, False)

        # Zeichne das aktuelle Frame auf dem Bildschirm
        char_frame = pygame.transform.scale(char_frame, (92,166))
        self.window.blit(char_frame, (self.rect.topleft))
        # pygame.draw.rect(self.window, (255, 0, 0), self.rect, 2) 
        # pygame.draw.rect(self.window, (255, 0, 0), self.hitbox, 2) 

    def movement(self):
        keys = pygame.key.get_pressed()

        # Bewegung des Spielers
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.moving_left = True
            self.facing_left = True
            self.moving_right = False

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.moving_left = False
            self.facing_left = False
            self.moving_right = True

        else:
            self.moving_left = self.moving_right = False

        # Update der Position des Spielers mit dem Rect
        if self.moving_left:
            self.rect.x -= self.walkingSpeedX
        if self.moving_right:
            self.rect.x += self.walkingSpeedX


        # Springen
        if keys[pygame.K_SPACE] and not self.spielstand.playerJumping and self.spielstand.canJump:
            self.spielstand.playerJumping = True
            self.spielstand.playerSpeedY = -12

        # Schwerkraft
        if self.spielstand.playerJumping:
            self.rect.y += self.spielstand.playerSpeedY
            self.spielstand.playerSpeedY += 1
            if self.rect.y >= self.spielstand.boden - self.rect.height:
                self.rect.y = self.spielstand.boden - self.rect.height
                self.spielstand.playerJumping = False
                self.spielstand.playerSpeedY = 0

        

        # Speichere die Position zurück in die Spielstand-Objekte
        self.spielstand.playerX = self.rect.x
        self.spielstand.playerY = self.rect.y

        if self.facing_left:
            self.hitbox = pygame.Rect((self.spielstand.playerX + (self.spielstand.playerWidth / 2)) -20, self.spielstand.playerY, 32, self.spielstand.playerHeight)
        else:
            self.hitbox = pygame.Rect((self.spielstand.playerX + (self.spielstand.playerWidth / 2)) -12, self.spielstand.playerY, 32, self.spielstand.playerHeight)



