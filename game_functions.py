import sys
import pygame
import time

def show_win_img(screen):
    """Display win window when player win"""
    # load the image
    win_img = pygame.image.load('images/win.png')

    # get the window rect and screen rect
    win_img_rect = win_img.get_rect()
    screen_rect = screen.get_rect()

    # set the image rect
    win_img_rect.center = screen_rect.center

    screen.fill((89, 23, 170))
    screen.blit(win_img,win_img_rect)

    # make the most recently drawn screen visible
    pygame.display.flip()


def check_boundary(guti):
    """Check the guti flow(<-- or -->) and set the boundary."""
    #left boundary
    if guti.guti_rect.left < 147:
        #Move the guti into the next row and set it's new position
        guti.guti_rect.bottom -= 53 #Move to the next row
        #set the current positon of the guti
        hold_guti_position = 147 - guti.guti_rect.left # Hold the increased value of the guti
        guti.guti_rect.left = 147 + (hold_guti_position - 53)

    #right boundary
    elif guti.guti_rect.left > 624:
        #Move the guti into the next row and set it's new position
        guti.guti_rect.bottom -= 53#Move to the next row
        hold_guti_position = guti.guti_rect.left - 624
        guti.guti_rect.left = 624 - (hold_guti_position-53)
                                     
        

def check_row(guti, value):
    """check the guti position in row and set the flow(<-- or -->)
    of the guti"""
    if guti.guti_rect.bottom % 2 == 0:
        #set the guti flow(<--) right to left
        guti.guti_rect.left -= (53*value)
    else:
        #set the guti flow(-->) left to right
        guti.guti_rect.left += (53*value)

def check_ending_point(guti,value,screen,win_sound):
    """check the guti in ending position or not.
        and ignore the dice value of if it's over than ending point."""
    temp_left = guti.guti_rect.left - (53*value)
    temp_bottom = guti.guti_rect.bottom
    game_over = False

    if game_over != True:    
        if temp_left < 147 and temp_bottom == 124:
            return False
        elif temp_left == 147 and  temp_bottom == 124:
            win_sound.play()
            show_win_img(screen)
            time.sleep(2)
            sys.exit()
        else:
            return True
        
def turn(guti,guti2):
    """Set the turn in the player one."""
    if guti.guti_rect.left == 147 and guti.guti_rect.bottom == 601:
        if guti2.guti_rect.left == 147 and guti.guti_rect.bottom == 601:
            return 1
    
def check_events(guti,guti2,dice,dice2,guti_sound,screen,win_sound):
    """Check the keyboard and mouse events. and guti will react
        on the dice value"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
                
            if event.key == pygame.K_KP_ENTER:
                dice_value = dice.dice_animation()
                update_guti_position(guti,dice_value,screen,win_sound)
                guti_sound.play()

                #computer Player
                time.sleep(1)
                dice_value = dice2.dice_animation()
                update_guti_position(guti2,dice_value,screen,win_sound)
                guti_sound.play()
                
def update_guti_position(guti,dice_value,screen,win_sound):
    
    """Update the guti position based on the dice value"""
    
    if dice_value == 1:
        if check_ending_point(guti, 1,screen,win_sound):
            check_row(guti,1)#call the check_row function
            check_boundary(guti)#call the guti row_function
                    
    elif dice_value == 2:
        if check_ending_point(guti,2,screen,win_sound):
            check_row(guti,2)#call the check_row function
            check_boundary(guti)#call the guti row_function
                    
    elif dice_value == 3:
        if check_ending_point(guti,3,screen,win_sound):
            check_row(guti,3)#call the check_row function
            check_boundary(guti)#call the guti row_function
                    
    elif dice_value == 4:
        if check_ending_point(guti,4,screen,win_sound):
            check_row(guti,4)#call the check_row function
            check_boundary(guti)#call the guti row_function
                    
    elif dice_value == 5:
        if check_ending_point(guti,5,screen,win_sound):                
            check_row(guti,5)#call the check_row function
            check_boundary(guti)#call the guti row_function
                    
    elif dice_value == 6:
        if check_ending_point(guti,6,screen,win_sound):
            check_row(guti,6)#call the check_row function
            check_boundary(guti)#call the guti row_function
    
def update_screen(screen, settings, board, players, guti ,guti2,dice):
    """Redraw the screen."""
    screen.fill(settings.bg_color)
    board.blitme()
    players.showPlayers()
    guti.show_guti()
    guti2.show_guti()

    # Make the most recently drawn screen visible
    pygame.display.flip()
    
