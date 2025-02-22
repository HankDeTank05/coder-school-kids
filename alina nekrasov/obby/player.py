import pygame
import common as c

class Player:

	def __init__(self):
		print("creating the player")
		self.health = 100
		self.pos = pygame.math.Vector2(0, 0)
		self.rect = pygame.Rect(self.pos, (50, 100))
		self.speed = 250

	def update(self, delta_time):
		pos_delta = pygame.math.Vector2(0, 0)

		# read for input
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
			pos_delta.x += self.speed

		pos_delta *= delta_time
		self.pos += pos_delta

	def draw(self, screen):
		pygame.draw.rect(screen, c.PINK, pygame.Rect(self.pos, (50, 100)))
