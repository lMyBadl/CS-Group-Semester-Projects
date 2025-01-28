import pygame, sys
from card_logic import Card, Deck
from player import Player

class Durak:
    # Initialize pygame
    pygame.init()

    # Screen dimensions
    screen_width = 500
    screen_height = 500

    # Create the screen
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)


    # Set the title of the window
    pygame.display.set_caption("Dark Green Background")
    clock = pygame.time.Clock()
    

    # Define the dark green color (RGB)
    dark_green = (0, 100, 0)

    # Main loop
    running = True
    while running:
                # get all events
        ev = pygame.event.get()

        # proceed events
        for event in ev:

            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

            # get a list of all sprites that are under the mouse cursor
            #clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
            # do something with the clicked sprites...
            elif event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen_width, screen_height = event.size
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)


        # Fill the screen with the dark green color
        screen.fill(dark_green)
        time_surface = pygame.font.Font(None, 50).render(str(int(clock.get_fps())), True, (255, 255, 255))
        # Position the text in the center of the rectangle
        text_rect = time_surface.get_rect(center=(250 + 300 // 2, 200 + 100 // 2))

        # Blit (draw) the text onto the screen
        screen.blit(time_surface, text_rect)

        # Update the display
        clock.tick(10000)
        pygame.display.flip()

    # Quit pygame
    pygame.quit()
    sys.exit()