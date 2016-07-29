import itertools
import sys, pygame
from shooter import Shooter
from centipedebody import CentipedeBody
from centipede import Centipede
from mushroom import Mushroom
from random import randrange
from enum import Enum


def randomlyGenerateMushrooms(width, height):
    ''' Returns a list of mushrooms that were randomly positioned on the board
    given the width of the board, and the height of the board.'''
    mushroomList = []
    mushrooms = 45 #hardcoded for now...
    for mushroom in range(mushrooms):
        newX = randrange(0, width)
        newY = randrange(0, height)
        mushroomList.append(Mushroom([newX,newY]))
    return mushroomList

pygame.init()

size = width, height = 800, 600
black = 0, 0, 0
screen = pygame.display.set_mode(size)
pos = [300,400]
imageLocation = "./images/shooter.png"
Status = Enum('Status', 'win lose')

shooter = Shooter(imageLocation, pos, width, height)
centipede = Centipede([-1,0],[500,1], width, height, 13)

allSpriteGroup = pygame.sprite.Group()
allSpriteGroup.add(shooter)
allSpriteGroup.add(centipede)

# A group containing all of the lasers the Shooter shoots
laserGroup = pygame.sprite.Group()
# A group containing all mushrooms in the game
mushroomGroup = pygame.sprite.Group()
mushroomGroup.add(randomlyGenerateMushrooms(width, height))

# All the non player character sprites
npcGroups = [laserGroup, centipede, mushroomGroup]

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

    # Deal with centipede segments that were shot
    collisions = pygame.sprite.groupcollide(laserGroup, centipede, True, False)
    segmentsHit = []
    for laser in collisions:
        segmentsHit.append(collisions[laser])
    freshMushroom = centipede.damage([segment for segmentList in segmentsHit for segment in segmentList])

    if freshMushroom != None:
        mushroomGroup.add(freshMushroom)

    # Deal with centipede segments that collide with mushrooms
    collisions = pygame.sprite.groupcollide(centipede, mushroomGroup, False, False)
    centipede.collide(collisions)

    #Delete mushrooms that get shot
    pygame.sprite.groupcollide(laserGroup, mushroomGroup, True, True)

    allSpriteGroup.add(itertools.chain(npcGroups))

    if pygame.sprite.spritecollideany(shooter, centipede):
        gameStatus = Status.lose
        break

    pygame.display.flip()

if gameStatus == Status.lose:
    statusImage = pygame.image.load("./images/youlose.png")

statusRect = statusImage.get_rect()
statusRect.x = 75
statusRect.y = 100
screen.fill(black)
screen.blit(statusImage, statusRect)
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
