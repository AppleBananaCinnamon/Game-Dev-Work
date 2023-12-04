import pygame
from sys import exit
import os
import random
import math
from os import listdir
from os.path import isfile, join 
from Sprite import Player

pygame.init()
start_time = 0
FPS = 60 
WIDTH, HEIGHT = 1200, 800
game_active = True

# Create the display surface for the player to see all the assets
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def player_death_animation():
    global player_death_surf, player_death_index
    player_death_index += 0.1
    if player_death_index >= len(player_death):
        player_death_index = 7
    player_death_surf = player_death[int(player_death_index)]


def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = title_font.render(f'{current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (600,200))
    screen.blit(score_surf,score_rect)

    title_surf = title_font.render('Pixel Runner!', False, 'Yellow')
    title_rect = title_surf.get_rect(center = (600,100))
    screen.blit(title_surf,title_rect)

    author_surf = title_font.render('A WIP by Jonathan Franco', False, 'Yellow')
    author_rect = title_surf.get_rect(center = (400,750))
    screen.blit(author_surf,author_rect)


    



# screen_rect = screen.get_rect(center = (600,400))
clock = pygame.time.Clock() # Very important, this is what sets the FPS of the game.
title_font = pygame.font.Font('Test/Pixeltype.ttf',100)
auth_font = pygame.font.Font('Test/Pixeltype.ttf',70) 

surface = pygame.image.load('scaled_background.jpg').convert() # If 'screen' is our game window, then 'surface' is how we actually add things to that window


bomb_surf = pygame.image.load('Test/Bomb2_smol.png').convert_alpha()
bomb_rect = bomb_surf.get_rect(center = (1050,650))



player = Player(250,700)

player_x_pos = 150
player_width = 95

gravity = 0
hor_velo = 0

# Set the icon and the name of the game that will be displayed
pygame.display.set_caption('Pixel Runner')
icon = pygame.image.load('running icon.png')
pygame.display.set_icon(icon)

# Player Death
player_death_1 = pygame.image.load('Test/Graphics/Player Death/Death_1.png').convert_alpha()
player_death_2 = pygame.image.load('Test/Graphics/Player Death/Death_2.png').convert_alpha()
player_death_3 = pygame.image.load('Test/Graphics/Player Death/Death_3.png').convert_alpha()
player_death_4 = pygame.image.load('Test/Graphics/Player Death/Death_4.png').convert_alpha()
player_death_5 = pygame.image.load('Test/Graphics/Player Death/Death_5.png').convert_alpha()
player_death_6 = pygame.image.load('Test/Graphics/Player Death/Death_6.png').convert_alpha()
player_death_7 = pygame.image.load('Test/Graphics/Player Death/Death_7.png').convert_alpha()
player_death_8 = pygame.image.load('Test/Graphics/Player Death/Death_8.png').convert_alpha()

player_death = [player_death_1, player_death_2, player_death_3, player_death_4, player_death_5, player_death_6, player_death_7, player_death_8]
player_death_index = 0

player_death_surf = player_death[player_death_index]
player_death_rect = player_death_surf.get_rect(center = (600,400))


# Intro Screen
# player_stand = pygame.image.load()

while True:
    for event in pygame.event.get(): # This is our event loop; events are things like: achievs, user actions, quit, etc.
        if event.type == pygame.QUIT:   
            pygame.quit()
            exit() # sys.exit() ensures we don't get an error code when we shut the game down

        # jump mechanics -- this wouldn't run because it wasn't within the event loop, but I'm not sure why. 
        jump_flag = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.player_idle_rect.bottom == 700:
                jump_flag = True
                gravity = -20    

        
        # Movement Mechanics 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and player.player_idle_rect.bottom == 700:
                hor_velo += 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                hor_velo = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and player.player_idle_rect.bottom == 700:
                hor_velo -= 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                hor_velo = 0

        # Barrier Walls
        # player_rect.x = max(0, min(player_rect.x, 800 - player_width))
        '''if screen_rect.colliderect(player_rect):
            game_active = True'''
    
    player.jump_animation()
    player.idle_animation()
    # player_jump_rect.topleft = player.player_idle_rect.topleft    






    if game_active: 
        screen.blit(surface,(0,0))
        # pygame.draw.rect(screen, (0,0,0), score_rect)
        # pygame.draw.rect(screen, (0,0,0), score_rect,10)
        # screen.blit(score_surf,score_rect)
        display_score()

        bomb_rect.x -= 10
        if bomb_rect.right < 0:
            bomb_rect.left = 1200
        screen.blit(bomb_surf,bomb_rect)

        # Player Mechanics
        gravity += 1
        player.player_idle_rect.y += gravity
        player.player_idle_rect.x += hor_velo

        # Update player_jump_rect to match player_idle_rect
        player.player_jump_rect.topleft = player.player_idle_rect.topleft

        if player.player_idle_rect.bottom >=700:
            player.player_idle_rect.bottom = 700
            screen.blit(player.player_surf, player.player_idle_rect)
        else: 
            screen.blit(player.player_jump_surf, player.player_jump_rect)
        
        

        # Collision
        if bomb_rect.colliderect(player.player_idle_rect):
            game_active = False
    else:
        screen.fill((0, 0, 0))
        player_death_animation()
        screen.blit(player_death_surf,player_death_rect)
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            game_active = True
            player_death_index = 0
            bomb_rect.left = 1200
            start_time = int(pygame.time.get_ticks()/1000)



    pygame.display.update()
    clock.tick(60)

    # update everything





# surface = pygame.Surface((900,600)) # If 'screen' is our game window, then 'surface' is how we actually add things to that window