import pygame, sys 

class Player(pygame.sprite.Sprite):
    
    # Load idle images
    def __init__(self, pos_x, pos_y):
        super().__init__()
        pygame.init()
        
        self.idle = []
        self.idle.append(pygame.image.load('Test/Graphics/Player_Idle/sharp_1.png').convert_alpha())
        self.idle.append(pygame.image.load('Test/Graphics/Player_Idle/sharp_2.png').convert_alpha())
        self.idle.append(pygame.image.load('Test/Graphics/Player_Idle/sharp_2.png').convert_alpha())
        self.idle.append(pygame.image.load('Test/Graphics/Player_Idle/sharp_3.png').convert_alpha())
        self.idle.append(pygame.image.load('Test/Graphics/Player_Idle/sharp_4.png').convert_alpha())
        self.idle.append(pygame.image.load('Test/Graphics/Player_Idle/sharp_5.png').convert_alpha())
        self.idle.append(pygame.image.load('Test/Graphics/Player_Idle/sharp_6.png').convert_alpha())
        self.idle.append(pygame.image.load('Test/Graphics/Player_Idle/sharp_7.png').convert_alpha())
        self.idle.append(pygame.image.load('Test/Graphics/Player_Idle/sharp_8.png').convert_alpha())
        self.idle.append(pygame.image.load('Test/Graphics/Player_Idle/sharp_9.png').convert_alpha())
        self.idle.append(pygame.image.load('Test/Graphics/Player_Idle/sharp_10.png').convert_alpha())

        # Load jumping and landing images
        self.jump = []
        self.jump.append(pygame.image.load('Test/Graphics/Player_land/PJ_1.png').convert_alpha())
        self.jump.append(pygame.image.load('Test/Graphics/Player_land/PJ_2.png').convert_alpha())
        self.jump.append(pygame.image.load('Test/Graphics/Player_land/PJ_3.png').convert_alpha())

        self.land = []
        self.land.append(pygame.image.load('Test/Graphics/Player_Land/land_sharp_1.png').convert_alpha())
        self.land.append(pygame.image.load('Test/Graphics/Player_Land/land_sharp_2.png').convert_alpha())
        self.land.append(pygame.image.load('Test/Graphics/Player_Land/land_sharp_3.png').convert_alpha())
        self.land.append(pygame.image.load('Test/Graphics/Player_Land/land_sharp_4.png').convert_alpha())
        self.land.append(pygame.image.load('Test/Graphics/Player_Land/land_sharp_5.png').convert_alpha())
        self.land.append(pygame.image.load('Test/Graphics/Player_Land/land_sharp_6.png').convert_alpha())
        self.land.append(pygame.image.load('Test/Graphics/Player_Land/land_sharp_7.png').convert_alpha())
        self.land.append(pygame.image.load('Test/Graphics/Player_Land/land_sharp_8.png').convert_alpha())

        
        # Draw the Player surface and rectangle, and initialize the rectangle. 
        self.idle_index = 0
        self.player_surf = self.idle[self.idle_index]
        self.player_idle_rect = self.player_surf.get_rect()
        self.player_idle_rect.center = [pos_x, pos_y]

        # Set the jumping animation equal to the Player's rectangle 
        self.player_jump_index = 0
        self.player_jump_surf = self.jump[self.player_jump_index]
        self.player_jump_rect = pygame.Rect(self.player_idle_rect)

        self.frame_duration = 200  # 100 milliseconds (0.1 seconds) per frame
        self.last_frame_time = pygame.time.get_ticks()





    # Define the neutral animation loop 
    def idle_animation(self):
        self.idle_index += 0.1
        if self.idle_index >= len(self.idle):
            self.idle_index = 0
        self.player_surf = self.idle[int(self.idle_index)]


    # Define the jumping animation loop 
    def jump_animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_time >= self.frame_duration:
            self.last_frame_time = current_time
            self.player_jump_index = (self.player_jump_index + 1) % len(self.jump)
            self.player_jump_surf = self.jump[self.player_jump_index]
        
''' def jump_animation(self):
    current_time = pygame.time.get_ticks()
    if current_time - self.last_frame_time >= self.frame_duration:
        self.last_frame_time = current_time
        self.player_jump_index = (self.player_jump_index + 1) % len(self.jump)
        self.player_jump_surf = self.jump[self.player_jump_index]''' 
