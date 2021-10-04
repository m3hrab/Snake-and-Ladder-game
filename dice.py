import pygame
import random
import time

class Dice():
    """
    A class that represent dice animation and rendomly
    hold the dice value.The dice value will update the guti
    position.
    
    """

    def __init__(self,screen,board,players,guti,guti2,settings,clock,dice_position,roll_sound):
        """Initialize all the attributes of the dice."""
        self.screen = screen
        self.board = board
        self.players = players
        self.guti = guti
        self.guti2 = guti2
        self.settings = settings
        self.dice_value = 0 # initialize
        self.clock = clock
        self.dice_position = dice_position
        self.dice_roll_music = roll_sound
        
    def dice_animation(self):
        """Show dice animation and hold a random value from 1 to 6."""
        # dice animation
        self.dice_roll_music.play()

        #load the picture
        for name in range(1,14):
            # load the dice images
            dice_image = pygame.image.load('images/dice_images/dice'+str(name)+'.png')

            # get screen rect and dice.
            dice_image_rect = dice_image.get_rect()
            self.screen_rect = self.screen.get_rect()

            # set the dice_image in bottom conner of the screen
            dice_image_rect.left = self.screen_rect.left + self.dice_position #dice_position 
            dice_image_rect.bottom = self.screen_rect.bottom

            # show the dice into the screen    
            self.screen.fill(self.settings.bg_color)
            self.board.blitme()
            self.players.showPlayers()
            self.guti.show_guti()
            self.guti2.show_guti()
            self.screen.blit(dice_image, dice_image_rect)
            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(12)
        
         #Hold a random value from 1 to 6
        self.dice_value = random.randint(1,6)
        #display the exat dice
        dice_image = pygame.image.load('images/dice_images/dice'+str(self.dice_value)+'.png')
        # show the dice into the screen    
        self.screen.fill(self.settings.bg_color)
        self.board.blitme()
        self.players.showPlayers()
        self.guti.show_guti()
        self.guti2.show_guti()
        self.screen.blit(dice_image, dice_image_rect)
        # Make the most recently drawn screen visible
        pygame.display.flip()
        time.sleep(2)
        return self.dice_value

               
