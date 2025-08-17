import pygame
import common as c
import gamemath as gm

class Player:

	# constructor
	def __init__(self, x, y, width, height):
		print("creating the player")
		self.health = 100
		self.pos = pygame.math.Vector2(x, y)
		self.size = pygame.math.Vector2(width, height)
		self.rect = pygame.Rect(self.pos, self.size)
		self.walk_speed = 250
		self.jump_force = -250 #note to self: come back and program double jump
		self.pos_delta = pygame.math.Vector2(0, 0)
		self.current_velocity = pygame.math.Vector2(0, 0)	
		self.max_jumps = 2
		self.jumps_remaining = self.max_jumps
		self.curr_jump_state = False
		self.prev_jump_state = False

	def update(self, delta_time, collide_thing: pygame.Rect):
		###################
		# move the player #
		###################

		# get the state of the keyboard
		keys = pygame.key.get_pressed()

		# read for input
		move_right: bool = keys[pygame.K_d] or keys[pygame.K_RIGHT]
		move_left: bool = keys[pygame.K_a] or keys[pygame.K_LEFT]
		self.curr_jump_state: bool = keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]

		if move_right and not move_left:
			self.pos_delta.x = self.walk_speed
		elif move_left and not move_right:
			self.pos_delta.x = -self.walk_speed
		else:
			self.pos_delta.x = 0

		# if keys[pygame.K_s] == True:
		# 	self.pos_delta.y += self.speed
		if self.curr_jump_state == True and self.prev_jump_state == False and self.jumps_remaining > 0:
			self.jumps_remaining -= 1
			self.pos_delta.y = self.jump_force
		else:
			self.pos_delta.y += c.GRAVITY

		# making the player position move
		self.pos += self.pos_delta * delta_time

		# update the position of the rectangle
		self.rect.update(self.pos, self.size)

		#############################
		# do the collision behavior #
		#############################

		platform_collision: bool = self.collide_check(collide_thing)
		if platform_collision == True:
			#print("I collided with the platform")

			# Check if we are colliding with the platform from above
			# We determain this by checking 2 things, 
			# 1. Are we falling
			# 2. Was the player (rectangle) above the platform before we moved.
			#	- We determine this by undoing the movement that occured this frame and comparing rectangle positions
			self.pos -= self.pos_delta * delta_time
			self.rect.update(self.pos, self.size)
			if self.pos_delta.y > 0 and self.rect.bottom <= collide_thing.top: # check for collision from the top
				print("Collision from the top")
				# Preventing vertical acceleration
				self.pos_delta.y = 0
				# Puts back movement that occured this frame 
				self.pos += self.pos_delta * delta_time
				self.rect.update(self.pos, self.size)
				# box comment below. if you can't see it, hit the arrow on the left next to the line number!
				'''
				this is the situation that the following lines of code are meant to correct:
				             player
				             |    |
				+------------|----|-+
				| platform   +----+ |

						|||
						VVV
				
				             player
							 |	  |
							 |	  |
				             +----+
				+-------------------+
				| platform          |

				the following code will cause this to be the end result
				'''
					
				self.rect.bottom = collide_thing.top - 0.1
				self.pos = self.rect.topleft
				self.jumps_remaining = self.max_jumps
			elif self.rect.bottom > collide_thing.top and self.rect.top < collide_thing.bottom: # check for collision from either side
				self.pos += self.pos_delta * delta_time
				self.rect.update(self.pos, self.size)
				side = None
				if gm.number_in_range(self.rect.right, collide_thing.left, collide_thing.right):
					# colliding with the left side of the platform, move the player left to get them out
					self.rect.right = collide_thing.left - 0.1
					self.pos = self.rect.topleft
					side = "left"
				elif gm.number_in_range(self.rect.left, collide_thing.left, collide_thing.right):
					#colliding with the right side of the platform, move the player right to get them out
					self.rect.left = collide_thing.right + 0.1
					self.pos = self.rect.topleft
					side = "right"
				# print(f"colliding with the {side} side of platform")

		else:
			# print("I did not collide with the platform")
			pass

		##########################
		# prepare for next frame #
		##########################
		
		self.prev_jump_state = self.curr_jump_state

	def collide_check(self, other: pygame.Rect) -> bool:
		player_collision = self.rect.colliderect(other)
		return player_collision

	def draw(self, screen):
		pygame.draw.rect(screen, c.PINK, self.rect)
