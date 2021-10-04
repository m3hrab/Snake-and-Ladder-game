import pygame
import sys

class Intro():
    """
    A class that represent opening window of the game
    and this window hold the play button, music button,
    game sound button
    """
    def __init__(self,screen):
        self.screen = screen

    def show_open_window(self):

        # load the image
        intro_image = pygame.image.load('images/intro.png')

        # get the window rect and screen rect
        intro_image_rect = intro_image.get_rect()
        screen_rect = self.screen.get_rect()

        # set the image rect
        intro_image_rect.center = screen_rect.center

        while True:
            
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return True
                    
            # draw the window
            self.screen.blit(intro_image,intro_image_rect)

            # make the most recently drawn screen visible
            pygame.display.flip()

                
        
