import pygame
import common as c

class Player:

	# constructor
	def __init__(self):
		print("creating the player")
		self.health = 100
		self.pos = pygame.math.Vector2(0, 0)
		self.rect = pygame.Rect(self.pos, (50, 100))
		self.speed = 250
		self.pos_delta = pygame.math.Vector2(0, 0)

	def update(self, delta_time):

		# read for input
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d] == True:
			self.pos_delta.x += self.speed
		if keys[pygame.K_a]:
			self.pos_delta.x -= self.speed
		if keys[pygame.K_s]:
			self.pos_delta.y += self.speed
		if keys[pygame.K_w]:
			self.pos_delta.y -= self.speed

		if self.pos_delta.x != 0 and self.pos_delta.y != 0:
			self.pos_delta.normalize_ip()
			self.pos_delta *= self.speed

		self.pos_delta *= delta_time
		self.pos += self.pos_delta

	def draw(self, screen):
		pygame.draw.rect(screen, c.PINK, pygame.Rect(self.pos, (50, 100)))
