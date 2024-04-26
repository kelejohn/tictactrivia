import pygame
import sys
import numpy as np
import random
from trivia_questions import select_question
from welcome_screen import draw_text
from categories import display_category, reset_c, wrong_answr, check_cat, correct2,correct1
from bonus import player_bonus, used


pygame.init()

# constants
WIDTH = 600
HEIGHT = 600
circ_radius = 60
circ_width = 15
line_width = 15
rows = 3
columns = 3
MAX_QUESTION_WIDTH = 45


# rgb colors
background = (207, 222, 220)
buttons = (149, 194, 188)
line = (54, 60, 59)
oh = (153, 24, 67)
ex = (34, 94, 186)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# font
font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Trivia")
screen.fill(background)

board = np.zeros((rows, columns))
print(board)


def draw_board():
    pygame.draw.line(screen, line, (0, 200), (600, 200), 5)
    pygame.draw.line(screen, line, (0, 400), (600, 400), 5)
    pygame.draw.line(screen, line, (400, 0), (400, 600), 5)
    pygame.draw.line(screen, line, (200, 0), (200, 600), 5)


def draw_figures():
    for row in range(rows):
        for col in range(columns):
            if board[row][col] == 1:
                pygame.draw.circle(screen, oh, (int(col * 200 + 100), int(row * 200 + 100)), circ_radius, circ_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, ex, (col * 200 + 50, row * 200 + 150), (col * 200 + 150, row * 200 + 50),
                                 line_width)
                pygame.draw.line(screen, ex, (col * 200 + 50, row * 200 + 50), (col * 200 + 150, row * 200 + 150),
                                 line_width)


def make_move(row, col, player):
    board[row][col] = player


def valid_move(row, col):
    if row == 4:
        return False
    else:
        return board[row][col] == 0


def is_board_full():
    for row in range(rows):
        for col in range(columns):
            if board[row][col] == 0:
                return False
    return True


def check_win(player):
    for col in range(columns):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_v_win_line(col, player)
            return True

    for row in range(rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_h_win_line(row, player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False


def draw_v_win_line(col, player):
    posX = col * 200 + 100
    if player == 1:
        color = oh
    elif player == 2:
        color = ex
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)


def draw_h_win_line(row, player):
    posY = row * 200 + 100
    if player == 1:
        color = oh
    elif player == 2:
        color = ex
    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)


def draw_asc_diagonal(player):
    if player == 1:
        color = oh
    elif player == 2:
        color = ex
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def draw_desc_diagonal(player):
    if player == 1:
        color = oh
    elif player == 2:
        color = ex
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart():
    screen.fill(background)
    draw_board()
    for row in range(rows):
        for col in range(columns):
            board[row][col] = 0


def catfight(player, score1, score2):
    if is_board_full():
        display_message(["There is no winner.",
                         "Player 1's score: " + str(score1),
                         "Player 2's score is " + str(score2),
                         "Click 'C' to continue",
                         "Click 'R' to restart",
                         "Click 'E' to exit."], player)


def display_message(message, player):
    pause(player)
    pygame.time.wait(500)
    screen.fill(background)
    y_offset = HEIGHT // 3
    for line in message:
        draw_text(line, font, BLACK, screen, WIDTH // 2, y_offset)
        y_offset += 30
    pygame.display.update()


def win_message(player, score1, score2):
    if player == 1:
        return [
            "Player 1 wins!",
            "Player 1's score: " + str(score1),
            "Player 2's score is " + str(score2),
            "Click 'C' to continue",
            "Click 'R' to restart",
            "Click 'E' to exit."
        ]
    else:
        return [
            "Player 2 wins!",
            "Player 1's score: " + str(score1),
            "Player 2's score is " + str(score2),
            "Click 'C' to continue",
            "Click 'R' to restart",
            "Click 'E' to exit."
        ]


def pause(player):
    screen.fill(background)
    draw_board()
    draw_figures()
    check_win(player)
    pygame.display.update()
    pygame.time.wait(1000)

def wrap_text(text, max_width):
    words = text.split()
    lines = []
    current_line = ''
    for word in words:
        if len(current_line) + len(word) <= max_width:
            current_line += word + ' '
        else:
            lines.append(current_line.strip())
            current_line = word + ' '
    lines.append(current_line.strip())
    return lines


def display_question(screen, question, player):
    pause(player)
    screen.fill(background)

    question_lines = wrap_text(question['question'], MAX_QUESTION_WIDTH)
    y_offset = HEIGHT // 5
    for line in question_lines:
        draw_text(line, font, BLACK, screen, WIDTH // 2, y_offset)
        y_offset += 30

    y_offset = HEIGHT // 3 + 50
    for answer in question['answers']:
        draw_text(answer, font, BLACK, screen, WIDTH // 2, y_offset)
        y_offset += 30

    pygame.display.update()


def pop_up(message):
    screen.fill(background)
    draw_text(message, font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
    pygame.display.update()
    pygame.time.wait(500)
    screen.fill(background)
    draw_board()
    draw_figures()


def timed_message(message, player):
    pause(player)
    screen.fill(background)
    y_offset = HEIGHT // 3
    for line in message:
        draw_text(line, font, BLACK, screen, WIDTH // 2, y_offset)
        y_offset += 30
    pygame.display.update()
    pygame.time.wait(1500)


def get_player_answer():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    return 'A'
                elif event.key == pygame.K_b:
                    return 'B'
                elif event.key == pygame.K_c:
                    return 'C'
                elif event.key == pygame.K_d:
                    return 'D'
                elif event.key == pygame.K_e:
                    print("Thanks for playing")
                    sys.exit()



def use_bonus(player):
    pygame.time.wait(2500)
    pause(player)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = mouseY // 200
                clicked_col = mouseX // 200
                if valid_move(clicked_row, clicked_col):
                    make_move(clicked_row, clicked_col, player)
                    screen.fill(background)
                    draw_board()
                    draw_figures()
                    used(player)
                    pygame.display.update()
                    print(correct1)
                    print(correct2)
                    return




def main():
    draw_board()
    player = 1
    game_over = False
    score1 = 0
    score2 = 0

    # mainloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = int(mouseY // 200)
                clicked_col = int(mouseX // 200)

                if player == 1:
                    if not player_bonus(player) and not game_over:
                        if valid_move(clicked_row, clicked_col):
                            # ask question and get answer
                            choice = display_category(player)
                            question = select_question(choice)
                            display_question(screen, question, player)
                            player_answer = get_player_answer()

                            if player_answer == question['correct_answer']:
                                print("Correct answer Player 1!")
                                pop_up("Correct!!")
                                if board[clicked_row][clicked_col] == 0:
                                    make_move(clicked_row, clicked_col, player)
                                    screen.fill(background)
                                    draw_board()
                                    draw_figures()
                                    check_cat(player)
                                    if check_win(player):
                                        game_over = True
                                        print(board)
                                        score1 += 1
                                        display_message(win_message(player, score1, score2), player)
                                        break
                                    if player_bonus(player):
                                        player = 1
                                    else:
                                        player = 2
                                        pop_up("Player 2's turn")
                                else:
                                    player = 1
                            else:
                                print("Incorrect answer.")
                                pop_up("Incorrect")
                                pop_up("Player 2's turn")
                                wrong_answr(choice, player)
                                screen.fill(background)
                                draw_board()
                                draw_figures()
                                clicked_row = 4
                                player = 2
                    else:
                        display_message([
                            "Player " + str(player) + ",",
                            "You answered correctly in every trivia category.",
                            "You get a bonus move!"
                        ], player)
                        use_bonus(player)
                        if check_win(player):
                            game_over = True
                            print(board)
                            score1 += 1
                            display_message(win_message(player, score1, score2), player)
                            break
                        player = 2
                        pop_up("Player 2's turn")


                if player == 2:
                    if not player_bonus(player) and not game_over:
                        if valid_move(clicked_row, clicked_col):
                            # ask question and get answer
                            choice = display_category(player)
                            question = select_question(choice)
                            display_question(screen, question, player)
                            player_answer = get_player_answer()

                            if player_answer == question['correct_answer']:
                                print("Correct answer Player 2!")
                                pop_up("Correct!!")
                                if board[clicked_row][clicked_col] == 0:
                                    make_move(clicked_row, clicked_col, player)
                                    screen.fill(background)
                                    draw_board()
                                    draw_figures()
                                    check_cat(player)
                                    if check_win(player):
                                        game_over = True
                                        print(board)
                                        score2 += 1
                                        display_message(win_message(player, score1, score2), player)
                                        break
                                    if player_bonus(player):
                                        player = 2
                                    else:
                                        player = 1
                                        pop_up("Player 1's turn")
                                else:
                                    player = 2
                            else:
                                print("Incorrect answer.")
                                pop_up("Incorrect")
                                wrong_answr(choice,player)
                                screen.fill(background)
                                pop_up("Player 1's turn")
                                draw_board()
                                draw_figures()
                                clicked_row = 4
                                player = 1
                    else:
                        display_message([
                            "Player " + str(player) + ",",
                            "You answered correctly in every trivia category.",
                            "You get a bonus move!"
                        ], player)
                        use_bonus(player)
                        if check_win(player):
                            game_over = True
                            print(board)
                            score2 += 1
                            display_message(win_message(player, score1, score2), player)
                            break
                        player = 1
                        pop_up("Player 2's turn")

                if is_board_full():
                    catfight(player, score1, score2)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    player = 1
                    score1 = 0
                    score2 = 0
                    reset_c()
                    game_over = False
                if event.key == pygame.K_e:
                    print("Thanks for playing\nScore:\n P1:", score1, "P2:", score2)
                    sys.exit()
                if event.key == pygame.K_c:
                    restart()
                    player = random.randrange(1, 3)
                    game_over = False
                    pop_up("Player " + str(player) + " make the first move")

        pygame.display.update()
