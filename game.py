import pygame
import random

pygame.init()
size = 500
screen = pygame.display.set_mode((size, size))
being_played = True
x = 100
y = 100
square_size = 10

square_colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
background_colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


clock = pygame.time.Clock()

while being_played == True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        being_played = False
        
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
                y = max(y-1, 0)
        if pressed[pygame.K_DOWN]:
                y = min(y+1, size-square_size)
        if pressed[pygame.K_LEFT]:
                x = max(x-1, 0)
        if pressed[pygame.K_RIGHT]:
                x = min(x+1, size-square_size)

        if pressed[pygame.K_SPACE]:
                square_colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                background_colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        screen.fill(background_colour)
        pygame.draw.rect(screen, square_colour, pygame.Rect(x , y, square_size, square_size))
        
        pygame.display.flip()
        clock.tick(60)