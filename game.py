import sys, pygame
pygame.init()

size = width, height = 800, 600
speed = [0, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

shooter = pygame.image.load("./images/shooter.png")
shooterrect = shooter.get_rect()

speed = [0,0]

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
        if event.type == pygame.KEYUP:
            speed = [0,0]

    shooterrect = shooterrect.move(speed)
    if shooterrect.left < 0 or shooterrect.right > width:
        speed[0] = 0 #-speed[0]
    if shooterrect.top < 0 or shooterrect.bottom > height:
        speed[1] = 0 #-speed[1]

    screen.fill(black)
    screen.blit(shooter, shooterrect)
    pygame.display.flip()
