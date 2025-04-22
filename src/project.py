import random
import pygame





def main():
    pygame.init()
    pygame.display.set_caption("Hi-r/Lo-R")
    fullscreen = False
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    bg = pygame.Color(0, 0, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11 and fullscreen == False:
                    pygame.display.toggle_fullscreen()
                    fullscreen = True
                if event.key == pygame.K_ESCAPE and fullscreen == True:
                    pygame.display.toggle_fullscreen()
                    fullscreen = False
        
        screen.fill(bg)
        pygame.display.flip()
        keystate = pygame.key.get_pressed()
        dt = clock.tick(24)


    pygame.quit()


if __name__ == "__main__":
    main()