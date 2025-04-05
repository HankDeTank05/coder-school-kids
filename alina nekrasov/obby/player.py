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
			self.pos_delta.x = self.speed
		if keys[pygame.K_a] == True:
			self.pos_delta.x = -self.speed
		# (keys[pygame.K_a] == False and keys[pygame.K_d] == False) or (keys[pygame.K_a] == True and keys[pygame.K_d] == True)
		# below is the same, but simpler and more efficient than the commented code above
		if keys[pygame.K_a] == keys[pygame.K_d]: # checks if both keys are in the same state (both pressed or neither pressed)
			self.pos_delta.x = 0
		if keys[pygame.K_s] == True:
			self.pos_delta.y += self.speed
		if keys[pygame.K_w] == True:
			self.pos_delta.y -= self.speed
		
		print(f"pos_delta {self.pos_delta}")

		if self.pos_delta.x != 0 and self.pos_delta.y != 0:
			self.pos_delta.normalize_ip()
			self.pos_delta *= self.speed

		self.pos += self.pos_delta * delta_time

	def draw(self, screen):
		pygame.draw.rect(screen, c.PINK, pygame.Rect(self.pos, (50, 100)))
