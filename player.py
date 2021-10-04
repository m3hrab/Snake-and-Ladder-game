import pygame

class Players():
	"""A Class that represent each player."""
	
	def __init__(self, screen):
		"""Initialize screen and set player position."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		# Player1 images
		self.image1 = pygame.image.load('images/player.png')
		self.rect1 = self.image1.get_rect()
		self.rect1.left = self.screen_rect.left
		
		# Player2 images
		self.image2 = pygame.image.load('images/player2.png')
		self.rect2 = self.image2.get_rect()
		self.rect2.right = self.screen_rect.right 
		
		# Player3 images 
		self.image3 = pygame.image.load('images/player3.png')
		self.rect3 = self.image3.get_rect()
		self.rect3.bottomleft = self.screen_rect.bottomleft
		
		# Player4 images
		self.image4 = pygame.image.load('images/player4.png')
		self.rect4 = self.image4.get_rect()
		self.rect4.bottomright = self.screen_rect.bottomright
		
	def showPlayers(self):
		"""Draw the player at it's position"""
		
		self.screen.blit(self.image1, self.rect1)
		self.screen.blit(self.image2, self.rect2)
		self.screen.blit(self.image3, self.rect3)
		self.screen.blit(self.image4, self.rect4)
