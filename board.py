import pygame

class Board():
	"""A class that represent ludo board."""
	
	def __init__(self, screen):
		"""initialze board settings."""
		self.screen = screen
		self.board = pygame.image.load('images/board.png')
		self.board_rect = self.board.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Set the position of the board
		self.board_rect.center = self.screen_rect.center
		
	def blitme(self):
		"""Draw the board into the screen."""
		self.screen.blit(self.board, self.board_rect)
