import pygame
import random

WIDTH = 800
HEIGHT = 600
BACKGROUND = (0,0,0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()

    start_animation = False

    # sequence of animations
    next_animation = {
        "pixel" : "line",
        "line" : "rectangle",
        "rectangle" : "pixel"
    }

    # tracks the previous and the current animation of the sequence
    # that's to display the correct caption
    previous_animation = 'pixel'
    animation = 'line'

    # initial postions for displaying the shapes
    # pixels only use start_pos because it is a dot
    start_pos = [0,0]
    end_pos = [0,0]

    while True:
        # waiting until clicking to start animating
        while start_animation == False:
            screen.fill(BACKGROUND)
            font = pygame.font.SysFont(None, 48)
            img = font.render('click to rotate animation', True, (255,255,255))
            screen.blit(img, ((WIDTH - img.get_width()) // 2, (HEIGHT - img.get_height()) // 2))
            pygame.display.update()

            # upon the first click, animate the first sequence   
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen.fill(BACKGROUND)
                    font = pygame.font.SysFont(None, 48)
                    img = font.render(next_animation[animation], True, (255,255,255))
                    screen.blit(img, ((WIDTH - img.get_width()) // 2, (HEIGHT - img.get_height()) // 2))
                    pygame.display.update()
                    start_animation = True
                    pygame.time.delay(1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # on click, move to the next animation in the sequence
            elif event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill(BACKGROUND)
                font = pygame.font.SysFont(None, 48)
                img = font.render(previous_animation, True, (255,255,255))
                screen.blit(img, ((WIDTH - img.get_width()) // 2, (HEIGHT - img.get_height()) // 2))
                previous_animation = animation
                animation = next_animation[animation]
                pygame.time.delay(1000)
        
        start_pos[0] = random.randrange(WIDTH)
        start_pos[1] = random.randrange(HEIGHT)
        end_pos[0] = random.randrange(WIDTH)
        end_pos[1] = random.randrange(HEIGHT)

        if next_animation[animation] == 'pixel':
            for i in range(5000):
                screen.set_at(start_pos,(random.randrange(256),random.randrange(256),random.randrange(256)))
        elif next_animation[animation] == 'line':
            pygame.draw.aaline(screen,
                (random.randrange(256),random.randrange(256),random.randrange(256)),
                start_pos,
                end_pos)
        elif next_animation[animation] == 'rectangle':
            rectangle = pygame.Rect((random.randrange(WIDTH),random.randrange(HEIGHT)),
                (random.randrange(WIDTH),random.randrange(HEIGHT)))

            pygame.draw.rect(screen,
                (random.randrange(256),random.randrange(256),random.randrange(256)),
                rectangle)
        else :
            print("ERROR: invalid animation")
            pygame.quit()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()