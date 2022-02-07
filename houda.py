import pygame

pygame.init()

screen= pygame.display.set_mode((800, 800))


cat = pygame.image.load('cat.png').convert()
catX=0
catY=100

clock = pygame.time.Clock()
running = True
while running:
    #fond en blanc
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #test touches
    pressed = pygame.key.get_pressed()
    pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        catX -= 10
    if pressed[pygame.K_RIGHT]:
        catX += 10
    if pressed[pygame.K_UP]:
        catY -= 10
    if pressed[pygame.K_DOWN]:
        catY += 10
    screen.fill((255, 255, 255))
    screen.blit(cat, (catX, catY))
    pygame.display.update()
    #ralentir image
    clock.tick(50) #en fps

pygame.quit()
