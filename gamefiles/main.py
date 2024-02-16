import pygame
from functions import graphfunc as g
from functions import movement as m
from objects import bgtiles, entities, model, player, shots


# Step 1 : Check for inputs
# Step 1.5 : Cheats
# Step 2 : Spawn things
# Step 3 : Move stuff
# Step 4 : Check for collisions, damage stuff
# Step 5 : Render

screenx, screeny = 500, 500
pygame.init()
screen = pygame.display.set_mode((screenx,screeny))
clock = pygame.time.Clock()
running = True
background = [bgtiles.BgTiles(500, 0), bgtiles.BgTiles(500, 1), bgtiles.BgTiles(500, 2), bgtiles.BgTiles(500, 3)]


while running:
    # Step 1
    keys = pygame.key.get_pressed()
    inputs = [0, 0, 0, 0, 0, 0, 0] # Z, S, Q, D, A, E, fire
    if keys[pygame.K_z]:
        inputs[0] = 1
    if keys[pygame.K_s]:
        inputs[1] = 1
    if keys[pygame.K_q]:
        inputs[2] = 1
    if keys[pygame.K_d]:
        inputs[3] = 1
    if keys[pygame.K_a]:
        inputs[4] = 1
    if keys[pygame.K_e]:
        inputs[5] = 1
    if keys[pygame.K_f]:
        inputs[6] = 1

    # Step 2
        
    # Step 3
        
    # moving BG tiles
    

    # Step 4
        
    # Step 5
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill('green')

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()