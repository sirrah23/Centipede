import sys, pygame
from shooter import Shooter

pygame.init()

size = width, height = 800, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)

speed = [0,0]
pos = [300,400]
imageLoc = "./images/shooter.png"
shooter = Shooter(speed, imageLoc, pos)

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
        #if event.type == pygame.KEYUP:
        #    speed = [0,0]

    shooter.updateSpeed(speed)
    shooter.moveRect()

    #if shooterrect.left < 0 or shooterrect.right > width:
    #    speed[0] = 0 #-speed[0]
    #if shooterrect.top < 0 or shooterrect.bottom > height:
    #    speed[1] = 0 #-speed[1]

    screen.fill(black)
    screen.blit(shooter.image, shooter.rect)
    pygame.display.flip()
