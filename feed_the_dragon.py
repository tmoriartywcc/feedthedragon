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
BUFFER_DISTANCE = -50

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

lives_text = font.render('Lives: ' + str(player_lives), True, GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)


game_over_text = font.render('GAMEOVER', True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render('Press any key to play again', True, GREEN, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)



#Set Sounds and Music
coin_sound = pygame.mixer.Sound('coin_sound.wav')
miss_sound = pygame.mixer.Sound('miss_sound.wav')
miss_sound.set_volume(.1)
pygame.mixer.music.load('ftd_background_music.wav')


#Set Images
player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT//2

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH + BUFFER_DISTANCE, random.randint(64, WINDOW_HEIGHT-32))



#The main game loop
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

    #Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()   
    

    #Move the dragon continously
    #if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0:
    #    dragon_rect.x -= PLAYER_VELOCITY
    #if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < WINDOW_WIDTH:
    #    dragon_rect.x += PLAYER_VELOCITY
    if keys[pygame.K_UP] and player_rect.top > 64:
        player_rect.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += PLAYER_VELOCITY

    #Move the coin
    if coin_rect.x < 0:
        #player missed coin
        player_lives -= 1
        miss_sound.play()
        #place coin off the end of the screen again
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
    else:
        coin_rect.x -= coin_velocity
        #move hte coint
    #Check for collison between player and coin
    if player_rect.colliderect(coin_rect):
        score += 1
        coin_sound.play()
        coin_velocity += COIN_ACCELERATION
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

    #update HUD
    score_text = font.render('Score: ' + str(score), True, GREEN, DARKGREEN)
    lives_text = font.render('Lives: ' + str(player_lives), True, GREEN, DARKGREEN)

    #Fill the display surface to cover old images
    display_surface.fill((0,0,0))

    #Draw rectangles to represent rectangles
    #pygame.draw.rect(display_surface, (0,255,0), dragon_rect, 1)
    #pygame.draw.rect(display_surface, (255,0,0), coin_rect, 1)
    
    #Blit the HUD to the screen
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.draw.line(display_surface, WHITE, (0,64), (WINDOW_WIDTH, 64), 2)

    
    #Blit (copy) assets to the screen
    display_surface.blit(player_image, player_rect)
    display_surface.blit(coin_image, coin_rect)


    #update display
    pygame.display.update()

    #Tick the clock
    clock.tick(FPS)


#End the game
pygame.quit()