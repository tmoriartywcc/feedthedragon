import pygame, random

#initialize pygame
pygame.init()

#create a display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Feed the Dragon")

#Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

#Set Game Values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 5
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = .5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

#Set Colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Set Fonts
font = pygame.font.Font('AttackGraffiti.ttf', 32)

#Set Text
score_text = font.render('Score: ' + str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10,10)

title_text = font.render('Feed the Dragon', True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)


#Set Sounds and Music



#Set Images
dragon_image = pygame.image.load("dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25,25)

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)



#The main game loop
running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

    #Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()   
    

    #Move the dragon continously
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0:
        dragon_rect.x -= PLAYER_VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += PLAYER_VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_rect.top > 0:
        dragon_rect.y -= PLAYER_VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += PLAYER_VELOCITY


    #Check for collission between two rects
    if dragon_rect.colliderect(coin_rect):
        print("HIT")
        coin_rect.left = random.randint(0, WINDOW_WIDTH - 48)
        coin_rect.top = random.randint(0, WINDOW_HEIGHT - 48)

    #Fill the display surface to cover old images
    display_surface.fill((0,0,0))

    #Draw rectangles to represent rectangles
    pygame.draw.rect(display_surface, (0,255,0), dragon_rect, 1)
    pygame.draw.rect(display_surface, (255,0,0), coin_rect, 1)
    
    #Blit (copy) assets to the screen
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)

    #update display
    pygame.display.update()

    #Tick the clock
    clock.tick(FPS)


#End the game
pygame.quit()