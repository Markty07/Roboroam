import pygame
from objects import bullets, graphfunc as g
from objects import movement as m
from objects import vectorClass as v
from objects import bgtiles, entities, model, player, bullets

# Step -1 : Load textures

# Step 1 : Check for inputs
# Step 1.5 : Cheats
# Step 2 : Spawn things
# Step 3 : Move stuff
# Step 4 : Check for collisions, damage stuff
# Step 5 : Render

screenx, screeny = 500, 500
pygame.init()
screen = pygame.display.set_mode((screenx,screeny), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
backGroundTiles = [bgtiles.BgTiles(500, 0), bgtiles.BgTiles(500, 1), bgtiles.BgTiles(500, 2), bgtiles.BgTiles(500, 3)]
for element in backGroundTiles : element.init_pos((500, 500))
backGroundTilesTexture = pygame.image.load("textures/Bgwar1.png")

playerBulletTexture = pygame.image.load("textures/shot_1.png")
playerMechTexture = pygame.image.load("textures/Onset_Mech.png")

playerModel = model.Model(playerMechTexture)
playerMech = player.Player(playerModel, None, speed=2) # Need placeholder for playermodel and playershot
# Here goes bullets

projectiles = [] # Holds every projectile object. Might make this a class later for easier use.
spawners = [] # This list gets cleared each frame
aiEntities = [] # Holds every entity using AI
dumbEntities = [] # Holds every entity not using AI


while running:

    # screen.fill("blue")

    # Step 1
    keys = pygame.key.get_pressed()
    inputs = [0, 0, 0, 0, 0, 0, 0] # Z, S, Q, D, A, E, Fire (space)
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
    if keys[pygame.K_SPACE]:
        inputs[6] = 1

    # Step 1.5

    # tVector = v.create_orientation_vector(playerMech.get_pos()[2])
    # print(tVector)

    # Step 2
    
    # spawn player spawners. Temporary testing code
    if inputs[6] == 1 :
        spawners.append(bullets.Bulletspawner((250, 250, playerMech.pos[2]), player_vector, relpos = (-20, 0, 0)))
        spawners.append(bullets.Bulletspawner((250, 250, playerMech.pos[2]), player_vector, relpos = (20, 0, 0)))
    # spawn player shots using spawners. Temporary testing code
    for spawn in spawners :
        assert type(spawn) == bullets.Bulletspawner
        projectiles.append(bullets.Bullet(spawn.pos, spawn.speed, (1, "Player", "TestWeapon"))) # using defaultbullet


    # blip blup

    # Step 2.9 : Despawn stuff
    spawners = []
    projlen = len(projectiles)
    i = 0
    while i < projlen:
        # print("Checking projectiles")
        assert type(projectiles[i]) == bullets.Bullet
        if projectiles[i].lifetime < 1 :
            projectiles.pop(i)
            i -= 1
            projlen -= 1
        i += 1
    print(clock)


    # Step 3

    # Create player vector, POV and UMV (player orientation vector, universal movement vector)
    POV = v.create_orientation_vector(playerMech.get_pos()[2])
    pVx = inputs[3] - inputs[2]
    pVy = inputs[1] - inputs[0]
    player_vector = v.Vector(pVx, pVy)
    player_vector = v.scale_vector_to(player_vector, playerMech.get_speed())
    UMV = v.multiply_vector_with_factor(player_vector, -1)
    # moving BG tiles
    for element in backGroundTiles :
        element.vUpdate_pos(UMV)
    # rotate player
    if inputs[4] == 1 :
        playerMech.pos[2] += 2
    if inputs[5] == 1 :
        playerMech.pos[2] -= 2    
    
    # moving projectiles
    for shot in projectiles :
        assert type(shot) == bullets.Bullet
        shot.cycle(UMV)


    # moving AI
    

    # Step 4
        
    # check if ennemy is hit
        
    # check if player is hit
        
    # check projectiles collide
        
    # Step 5
    #    render background
    for element in backGroundTiles :
        g.blitRotate(screen, backGroundTilesTexture, element.get_pos(), (0,0), 0)
    #    render player
    g.blitRotate(screen, playerMech.model.get_texture(), (250, 250), (16, 16), playerMech.pos[2])
    #    render projectiles
    for shot in projectiles :
        assert type(shot) == bullets.Bullet
        g.blitRotate(screen, playerBulletTexture, (shot.pos[0], shot.pos[1]), (1,5), shot.pos[2])
        # Horrible code; Loads the same image multiple times in memory. Thank god it's only 2.10 pixels.
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE # NO ! :3
    # Testing
    g.blitRotate(screen, pygame.image.load("textures/OldMan_Mech.png"), (50,50), (16,16), 0)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
