import sys, pygame
from shooter import Shooter
from centipedehead import CentipedeHead

pygame.init()

size = width, height = 800, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)

speed = [0,0]
pos = [300,400]
imageLocation = "./images/shooter.png"
shooter = Shooter(speed, imageLocation, pos, width, height)

centipedeHead = CentipedeHead([-1,0],[800,0], width, height)

GameObjects = []
GameObjects.append(shooter)
GameObjects.append(centipedeHead)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed[1] = -1
            elif event.key == pygame.K_DOWN:
               speed[1] = 1
            elif event.key == pygame.K_RIGHT:
                speed[0] = 1
            elif event.key == pygame.K_LEFT:
                speed[0] = -1
            elif event.key == pygame.K_SPACE:
                GameObjects.append(shooter.shoot())
        if event.type == pygame.KEYUP:
            speed = [0,0]

    shooter.updateSpeed(speed)

    # Move everything in the game (referring to the underlying positions of game objects)
    for GameObject in GameObjects:
        GameObject.move()

    screen.fill(black)

    # If any game object has left the screen then remove it
    GameObjects[:] = [GameObject for GameObject in GameObjects if GameObject.withinScreen()]

    # Draw all the game objects on the screen in their new positions
    for GameObject in GameObjects:
        screen.blit(GameObject.image, GameObject.rect)

    pygame.display.flip()
