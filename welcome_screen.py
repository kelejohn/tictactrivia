import pygame
import sys


pygame.init()
#constants
WIDTH = 600
HEIGHT = 600


#rgb colors
background = (207,222,220)
buttons = (149,194,188)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font settings
font = pygame.font.Font(None, 36)
head = pygame.font.Font(None, 60)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Trivia")
screen.fill (background)



def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


def welcome_screen():
    screen.fill(background)
    draw_text("Welcome to Tic Tac Trivia!", head, BLACK, screen, WIDTH // 2, HEIGHT // 5)
    draw_text("Click ' E' to exit", font, BLACK, screen, WIDTH // 2, HEIGHT // 2+250)
    draw_text("How Many Players?", font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
    draw_text("1. One", font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 50)
    draw_text("2. Two", font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 100)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return level_pick()
                elif event.key == pygame.K_2:
                    return "duos"




def level_pick():
    screen.fill(background)
    draw_text("Select a Level:", font, BLACK, screen, WIDTH // 2, HEIGHT // 4)
    draw_text("1. Easy", font, BLACK, screen, WIDTH // 2, HEIGHT // 4 + 50)
    draw_text("2. Medium", font, BLACK, screen, WIDTH // 2, HEIGHT // 4 + 100)
    draw_text("3. Hard", font, BLACK, screen, WIDTH // 2, HEIGHT // 4 + 150)
    pygame.display.update()

#pick level
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "easy"
                elif event.key == pygame.K_2:
                    return "medium"
                elif event.key == pygame.K_3:
                    return "hard"
                elif event.key == pygame.K_e:
                    sys.exit()


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    print("Thanks for playing")
                    sys.exit()


        level = welcome_screen()
        start_game(level)
    pygame.quit()
    sys.exit()



def start_game(level):
    print("Starting game with level:", level)
    if level == "duos":
        from ttt2 import main as ttt2_main
        ttt2_main()

    else:
        from ttt import main as ttt_main
        ttt_main(level)

if __name__ == "__main__":
    main()