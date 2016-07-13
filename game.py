import itertools
import sys, pygame
from shooter import Shooter
from centipedehead import CentipedeHead

pygame.init()

size = width, height = 800, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)

pos = [300,400]
imageLocation = "./images/shooter.png"
shooter = Shooter(imageLocation, pos, width, height)

centipedeHead = CentipedeHead([-1,0],[800,0], width, height)

allSpriteGroup = pygame.sprite.Group()

allSpriteGroup.add(shooter)
allSpriteGroup.add(centipedeHead)

# A group containing all of the lasers the Shooter shoots
laserGroup = pygame.sprite.Group()
centipedeSegmentGroup = pygame.sprite.Group()
centipedeSegmentGroup.add(centipedeHead)

# All the non player character sprites
npcGroups = [laserGroup, centipedeSegmentGroup]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                newLaser = shooter.shoot()
                laserGroup.add(newLaser)
                allSpriteGroup.add(newLaser)

    pressedKeys = pygame.key.get_pressed()

    shooter.update(pressedKeys)

    # Move everything in the game (referring to the underlying positions of game objects)
    for gameSprite in list(itertools.chain(npcGroups)):
        gameSprite.update()

    screen.fill(black)

    # Draw all the game objects on the screen in their new positions
    for gameSprite in allSpriteGroup:
        screen.blit(gameSprite.image, gameSprite.rect)

    #TODO enhance collision logic
    #print pygame.sprite.groupcollide(laserGroup, centipedeSegmentGroup, False, False)

    pygame.display.flip()
