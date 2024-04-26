import pygame
import sys
from welcome_screen import draw_text
from bonus import bonus_move




pygame.init()
# constants
WIDTH = 600
HEIGHT = 600
circ_radius = 60
circ_width = 15
line_width = 15
rows = 3
columns = 3
correct1 = 0
correct2 = 0

# rgb colors
background = (207, 222, 220)
buttons = (149, 194, 188)
line = (54, 60, 59)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Trivia")
screen.fill (background)
pygame.display.update()

categories = ["Pop Culture", "Food", "Sports", "Movie/TV", "Geography", "Howard", "Disney", "Animal", "Science","Literature"]
still_in = categories[:]
still_in2 = categories[:]


def display_category(player):
    x = 0
    y = 1
    screen.fill(background)
    draw_text( "Pick A Category ", font, BLACK, screen, WIDTH // 2, HEIGHT // 6)
    pygame.display.update()

    for category in categories:
        color = find_color(category,player)
        draw_text(str(y) + ". " + category, font, color, screen, WIDTH // 2, HEIGHT // 4 + x)
        x += 25
        if y<9:
            y+=1
        else:
            y=0

    pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if use_category("Pop Culture",player):
                        return "Pop Culture"
                elif event.key == pygame.K_2:
                    if use_category("Food",player):
                        return "Food"
                elif event.key == pygame.K_3:
                    if use_category("Sports",player):
                        return "Sports"
                elif event.key == pygame.K_4:
                    if use_category("Movie/TV",player):
                        return "Movie/TV"
                elif event.key == pygame.K_5:
                    if use_category("Geography",player):
                        return "Geography"
                elif event.key == pygame.K_6:
                    if use_category("Howard",player):
                        return "Howard"
                elif event.key == pygame.K_7:
                    if use_category("Disney",player):
                        return "Disney"
                elif event.key == pygame.K_8:
                    if use_category("Animal",player):
                        return "Animal"
                elif event.key == pygame.K_9:
                    if use_category("Science",player):
                        return "Science"
                elif event.key == pygame.K_0:
                    if use_category("Literature",player):
                        return "Literature"
                elif event.key == pygame.K_e:
                    print("Thanks for playing")
                    sys.exit()


def use_category(category,player):
    global correct1
    global correct2
    if player == 1:
        global still_in
        refill(player)
        if category in still_in:
            print(category)
            correct1+=1
            still_in.remove(category)
            return True
        else:
            return False
    elif player == 2:
        global still_in2
        refill(player)
        if category in still_in2:
            print(category)
            correct2+=1
            still_in2.remove(category)
            return True
        else:
            return False

def wrong_answr(category,player):
    global still_in2
    global still_in
    global correct1
    global correct2
    if player==1:
        correct1 -= 1
        still_in.append(category)
    if player==2:
        correct2-=1
        still_in2.append(category)



def find_color(category,player):
    refill(player)
    if player == 1:
        if category in still_in:
            return BLACK
        else:
            return WHITE
    elif player == 2:
        if category in still_in2:
            return BLACK
        else:
            return WHITE

def refill(player):
    global still_in2
    global still_in
    if player == 1:
        if not still_in:
            still_in = categories[:]
    elif player == 2:
        if not still_in2:
            still_in2 = categories[:]

def reset_c():
    global still_in2
    global still_in
    global correct1
    global correct2
    correct1 = 0
    correct2 = 0
    still_in = categories[:]
    still_in2 = categories[:]

def check_cat(player):
    global correct1
    global correct2
    if player==1:
        if correct1 == 10:
            bonus_move(player)
            correct1=0
    if player==2:
        if correct2 == 10:
            bonus_move(player)
            correct2 = 0
