import sys, pygame
from shooter import Shooter

pygame.init()

size = width, height = 800, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)

speed = [0,0]
pos = [300,400]
imageLocation = "./images/shooter.png"
shooter = Shooter(speed, imageLocation, pos, width, height)

GameObjects = []
GameObjects.append(shooter)

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

    # Move everything in the game
    for GameObject in GameObjects:
        GameObject.move()

    screen.fill(black)

    # Draw all the game objects on the screen in their new positions
    for GameObject in GameObjects:
        screen.blit(GameObject.image, GameObject.rect)

    pygame.display.flip()
