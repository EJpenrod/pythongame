import pygame
import sys
pygame.init()

#Screen Settings
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1020
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Quest")
bg_image = pygame.image.load("assets/background images/Start Screen.jpg").convert_alpha()

#set framerate
clock = pygame.time.Clock()
FPS = 60

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0,0))

class Player:
    def __int__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def main(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

player = Player()


while True:
    clock.tick(FPS)
    #key presses
    #draw background
    draw_bg()
    #draw menu boxes

    #Button menuing
    button_1 = pygame.Rect(850, 875, 200, 50)
    button_2 = pygame.Rect(850, 800, 200, 50)
    button_3 = pygame.Rect(850, 725, 200, 50)
    pygame.draw.rect(screen, (255, 0, 0), button_1)
    pygame.draw.rect(screen, (255, 0, 0), button_2)
    pygame.draw.rect(screen, (255, 0, 0), button_3)

    player.main(screen)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT




    #update display
    pygame.display.update()