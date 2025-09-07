# Example file showing a basic pygame "game loop"
import pygame
import common as c
import player
import platform as plat


# (30, 250, 60, 30),
# (150, 450, 60, 30),
# (250, 250, 60, 30),
# (60, 430, 60, 30),
# (250, 410, 60, 30),
# (10, 430, 30, 30),
# (360, 370, 60, 30),
# (400, 280, 60, 30),


def run():
	# pygame setup
	pygame.init()
	SCREEN = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	running = True
	delta_time = 0

	#create game variables
	plat_man = plat.PlatManager()
	plat_man.add_plat(0, c.SCREEN_HEIGHT - 50, 100, 50, c.LIGHT_PURPLE)
	plat_man.add_plat_relative(150, -100, 60, 30, c.LIGHT_PURPLE)
	plat_man.add_plat_relative(200, -110, 70, 30, c.LIGHT_PURPLE)
	plat_man.add_plat_relative(5, -c.PLAYER_HEIGHT-30, 70, 30, c.LIGHT_PURPLE)
	plat_man.add_plat_relative(100, 350, 60, 30, c.LIGHT_PURPLE)
	plat_man.add_plat_relative(125, -100, 20, 20, c.LIGHT_PURPLE)
	#plat_man.platforms.append(plat.Platform(plat_man.platforms[0].rect.right + 50, plat_man.platforms[0].rect.y - 100, 60, 30, c.LIGHT_PURPLE))
	#plat_man.platforms.append(7)
	p1 = player.Player(0, c.SCREEN_HEIGHT - plat_man._platforms[0].rect.h - c.PLAYER_HEIGHT, c.PLAYER_WIDTH, c.PLAYER_HEIGHT)

	while running:
		# poll for events
		# pygame.QUIT event means the user clicked X to close your window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# fill the screen with a color to wipe away anything from last frame
		SCREEN.fill(c.BLACK)

		##################
		# PART 1: UPDATE #
		##################
		
		p1.update(delta_time, plat_man.get_rects())
		plat_man.update(delta_time)

		################
		# PART 2: DRAW #
		################

		p1.draw(SCREEN)
		plat_man.draw(SCREEN)

		# flip() the display to put your work on screen
		pygame.display.flip()

		delta_time = clock.tick(60)/1000  # limits FPS to 60

	pygame.quit()

if __name__ == "__main__":
	run()