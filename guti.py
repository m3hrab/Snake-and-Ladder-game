import pygame

class Guti():
    
    """
    A Class that represent ludo guti :P :)
    The reason to set the name "guti" because i don't
    know what is the meaning of "guti" in english :) that's why i
    set this object name is Guti....ha ha ha :)  
    """

    def __init__(self, screen, ladder_sound, snake_sound, guti_number=''):
        # Initialize all the attributes of guti
        self.screen = screen
        self.guti = pygame.image.load('images/guti'+str(guti_number)+'.png')

        # Get the guti, screen position.
        self.guti_rect = self.guti.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Set the guti position
        self.guti_rect.left = self.screen_rect.left + 147 # 147
        self.guti_rect.bottom = self.screen_rect.bottom - 99 # 601

        # sound
        self.ladder_sound = ladder_sound
        self.snake_sound = snake_sound

    def check_ladder(self,x,y):
        """check the guti is in ladder start position."""
        if self.guti_rect.left == 147 + (53*x):   #check X axis
            if self.guti_rect.bottom == 601 - (53*y): #check Y axis
                return True
        
    def check_snake(self,x,y):
        """Check the guti is in the mouth of the snake"""
        if self.guti_rect.left == 147 + (53*2):   #check X axis
            if self.guti_rect.bottom == 601 - (53*2):  #check Y axis
                return True

    def increase_guti_position(self,x,y):
        """Increase the guti position based on ladder possiton."""
        self.guti_rect.left = 147 + (53*x)  #check X axis
        self.guti_rect.bottom = 601 - (53*y) #check Y axis

    def decrease_guti_position(self,x,y):
        """Decrease the guti position based on the sanke"""
        self.guti_rect.left = 147 + (53*x)  #check X axis
        self.guti_rect.bottom = 601 - (53*y)  #check Y axis
            
        
    def show_guti(self):
        """Display the guti in the start position of the board."""

        # Ladder
        # Position 5 (4,0)(5,2)
        if self.guti_rect.left == 147 + (53*4) and self.guti_rect.bottom == 601 - (53*0):
            #Position 26
            self.ladder_sound.play()
            self.guti_rect.left = 147 + (53*5)
            self.guti_rect.bottom = 601 - (53*2)


        # Position 13 (7,1)(5,4)
        elif self.guti_rect.left == 147 + (53*7) and self.guti_rect.bottom == 601 - (53*1):
            #Position 46
            self.ladder_sound.play()
            self.guti_rect.left = 147 + (53*5)
            self.guti_rect.bottom = 601 - (53*4)

        # Position 18 (2,1)(1,3)
        elif self.guti_rect.left == 147 + (53*2) and self.guti_rect.bottom == 601 - (53*1):
            #Position
            self.ladder_sound.play()
            self.guti_rect.left = 147 + (53*1)
            self.guti_rect.bottom = 601 - (53*3)

        # Position 37 (3,3) (1,6)
        elif self.guti_rect.left == 147 + (53*3) and self.guti_rect.bottom == 601 - (53*3):
            #Position 62
            self.ladder_sound.play()
            self.guti_rect.left = 147 + (53*1)
            self.guti_rect.bottom = 601 - (53*6)

        # Position 48 (7,4)(8,7)
        elif self.guti_rect.left == 147 + (53*7) and self.guti_rect.bottom == 601 - (53*4):
            #Position 72
            self.ladder_sound.play()
            self.guti_rect.left = 147 + (53*8)
            self.guti_rect.bottom = 601 - (53*7)

        # Position 60 (0,5)(1,8)
        elif self.guti_rect.left == 147 + (53*0) and self.guti_rect.bottom == 601 - (53*5):
            #Position 82
            self.ladder_sound.play()
            self.guti_rect.left = 147 + (53*1)
            self.guti_rect.bottom = 601 - (53*8)

        # Position 65 (4,6) (5,9)
        elif self.guti_rect.left == 147 + (53*4) and self.guti_rect.bottom == 601 - (53*6):
            #Position 95
            self.ladder_sound.play()
            self.guti_rect.left = 147 + (53*5)
            self.guti_rect.bottom = 601 - (53*9)

        # Snake
        # Position 23
        if self.guti_rect.left == 147 + (53*2) and self.guti_rect.bottom == 601 - (53*2):
            #Position 7
            self.snake_sound.play()
            self.guti_rect.left = 147 + (53*6)
            self.guti_rect.bottom = 601 - (53*0)

        # Position 33
        elif self.guti_rect.left == 147 + (53*7) and self.guti_rect.bottom == 601 - (53*3):
            #Position 9
            self.snake_sound.play()
            self.guti_rect.left = 147 + (53*8)
            self.guti_rect.bottom = 601 - (53*0)

        # Position 44
        elif self.guti_rect.left == 147 + (53*3) and self.guti_rect.bottom == 601 - (53*4):
            #Position 14
            self.snake_sound.play()
            self.guti_rect.left = 147 + (53*6)
            self.guti_rect.bottom = 601 - (53*1)

        # Position 68
        elif self.guti_rect.left == 147 + (53*7) and self.guti_rect.bottom == 601 - (53*6):
            #Position 25
            self.snake_sound.play()
            self.guti_rect.left = 147 + (53*4)
            self.guti_rect.bottom = 601 - (53*2)

        # Position 77
        elif self.guti_rect.left == 147 + (53*3) and self.guti_rect.bottom == 601 - (53*7):
            #Position 41
            self.snake_sound.play()
            self.guti_rect.left = 147 + (53*0)
            self.guti_rect.bottom = 601 - (53*4)

        # Position 94
        elif self.guti_rect.left == 147 + (53*6) and self.guti_rect.bottom == 601 - (53*9):
            #Position 70
            self.snake_sound.play()
            self.guti_rect.left = 147 + (53*9)
            self.guti_rect.bottom = 601 - (53*6)

        # Position 97
        elif self.guti_rect.left == 147 + (53*3) and self.guti_rect.bottom == 601 - (53*9):
            #Position 68
            self.snake_sound.play()
            self.guti_rect.left = 147 + (53*5)
            self.guti_rect.bottom = 601 - (53*6)

        
            
            
        self.screen.blit(self.guti, self.guti_rect)

        
