import pygame

pygame.init()

TILESIZE = 90
MARGINSIZE = TILESIZE // 2
WIDTH = TILESIZE * 12 + MARGINSIZE * 2
HEIGHT = TILESIZE * 9 + MARGINSIZE * 2
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("RubixCube")
clock = pygame.time.Clock()

font = pygame.font.Font("font/LEMONMILK-Regular.otf",TILESIZE // 2)
fontSmall = pygame.font.Font("font/LEMONMILK-Regular.otf",TILESIZE // 4)
fontBig = pygame.font.Font("font/LEMONMILK-Regular.otf",TILESIZE)


spinImage = pygame.image.load("graphics/arrows.png").convert_alpha()
spinFlipImage = pygame.transform.scale(spinImage, (TILESIZE * 2, TILESIZE * 2))
spinImage = pygame.transform.flip(spinFlipImage, True, False)

BLACK = "#2d3436"
WHITE = "#ecf0f1"