import pygame
from settings import Settings
from board import Board
from player import Players
import game_functions as gf
from guti import Guti
from dice import Dice
from intro import Intro

 
def run_game():
    """Initialize pygame and create screen"""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
    		(settings.screen_width, settings.screen_height))
    pygame.display.set_caption("My Game")
    
    #dice_roll_sound
    roll_sound = pygame.mixer.Sound('audio/dice_roll.wav')
    #play sound when guti eaten by snake
    snake_sound = pygame.mixer.Sound('audio/snake.wav')
    #ladder sound
    ladder_sound = pygame.mixer.Sound('audio/ladder.wav')
    #guti_moved sound
    guti_sound = pygame.mixer.Sound('audio/guti.wav')
    #win_sound
    win_sound = pygame.mixer.Sound('audio/win.wav')
    
    clock = pygame.time.Clock()
	
    # Create a board instance
    board = Board(screen)
	
    # Create players instance
    players = Players(screen)
	
    """Create two guti instance for multiplayer"""
    guti = Guti(screen,ladder_sound,snake_sound)
    guti2 = Guti(screen,ladder_sound,snake_sound,2)

    # Create two dice instance for two players
    dice = Dice(screen,board,players,guti,guti2,settings,clock,100,roll_sound)
    dice2 = Dice(screen,board,players,guti,guti2,settings,clock,650,roll_sound)

    # Create opening window
    intro = Intro(screen)
    start_game = intro.show_open_window()

    # Initailize for player 1 turn
    turn = 1

    if start_game == True:
        # Main loop of the game
        while True:
            
            gf.check_events(guti,guti2,dice,dice2,guti_sound,screen,win_sound)    
            gf.update_screen(screen, settings, board, players, guti, guti2, dice)
            clock.tick(60)
		

run_game()
