import sys
import pygame

# init pygame and create window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Final Project")

# cap the frame rate
clock = pygame.time.Clock()

# setup font and center text
font = pygame.font.SysFont(None, 48)
text_surface = font.render("Hello World!", True, (255, 255, 255))
text_rect = text_surface.get_rect(center=screen.get_rect().center)

# main game loop
running = True
while running:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # background color
    screen.fill((50, 50, 50))

    # draw text
    screen.blit(text_surface, text_rect)

    # update screen
    pygame.display.flip()
    clock.tick(60)

# clean exit
pygame.quit()
sys.exit()