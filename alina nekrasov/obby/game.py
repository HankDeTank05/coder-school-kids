# Example file showing a basic pygame "game loop"
import pygame
import common as c
import player
import platform as plat

def run():
	# pygame setup
	pygame.init()
	SCREEN = pygame.display.set_mode((1280, 720))
	clock = pygame.time.Clock()
	running = True
	delta_time = 0

	#create game variables
	p1 = player.Player()
	platform = plat.Platform(0, 105, 100, 50, c.LIGHT_PURPLE)

	while running:
		# poll for events
		# pygame.QUIT event means the user clicked X to close your window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# fill the screen with a color to wipe away anything from last frame
		SCREEN.fill(c.BLACK)

		# PART 1: UPDATE
		p1.update(delta_time)
		platform.update(delta_time)

		# PART 2: DRAW
		p1.draw(SCREEN)
		platform.draw(SCREEN)

		# flip() the display to put your work on screen
		pygame.display.flip()

		delta_time = clock.tick(60)/1000  # limits FPS to 60

	pygame.quit()

if __name__ == "__main__":
	run()