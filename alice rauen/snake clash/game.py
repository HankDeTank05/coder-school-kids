# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# game setup
segments=22
seg_size = 50

speed=6
player=[]

moves=[]

colors=[]
head_color = pygame.Color('skyblue1')
tail_color = pygame.Color('black')
for i in range(segments):
    player.append(pygame.Rect(0,0,seg_size,seg_size))
    moves.append(pygame.math.Vector2(0,0))
    colors.append(head_color.lerp(tail_color, i/segments))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # UPDATE THE GAME

    keys=pygame.key.get_pressed()
    new_move=pygame.math.Vector2(0,0)
    if keys[pygame.K_UP]:
        new_move.y-=speed
    if keys[pygame.K_DOWN]:
        new_move.y+=speed
    if keys[pygame.K_LEFT]:
        new_move.x-=speed
    if keys[pygame.K_RIGHT]:
        new_move.x+=speed

    if new_move.length_squared()>0:
        new_move.normalize_ip()
        moves.insert(0,new_move)
        old_move=moves.pop()

        # player[0].move_ip(move.x,move.y)
        for i in range(len(player)):
            move=moves[i]*speed
            segment=player[i]
            segment.move_ip(move.x,move.y)

    # DRAW THE GAME

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    for i in range(len(player)-1, -1, -1):
        pygame.draw.rect(screen, colors[i], player[i])

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()