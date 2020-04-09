import pygame
import random
from pygame import mixer

# This is the board for checking winner
board1 = {'1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}

# random list
ls = ['X', 'O']
first = random.choice(ls)

# initialize py_game
pygame.init()

# setup or run the screen
screen = pygame.display.set_mode((700, 700))
running = True

# title and icon
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load('tic-tac-toe.png')
pygame.display.set_icon(icon)

# board image
board_img = pygame.image.load('tic-board.png')
board_x = 40
board_y = 40

# cross image
cross_img = pygame.image.load('cross1.png')

# circle image
circle_img = pygame.image.load('circle1.png')

# game over text
over_font = pygame.font.Font("freesansbold.ttf", 64)


# function of board
def board(board_x, board_y):
    screen.blit(board_img, (board_x, board_y))


# function of cross
def cross(cross_x, cross_y):
    screen.blit(cross_img, (cross_x, cross_y))


# function of circle
def circle(circle_x, circle_y):
    screen.blit(circle_img, (circle_x, circle_y))


# function for checking where is the mouse clicked
def place_checker_for_x(count, x, y):
    if count == 9 or count == 7 or count == 5 or count == 3 or count == 1:
        # 1
        if 44 <= x <= 218 and 52 <= y <= 223:
            if board1['1'] == '':
                cross(60, 80)
                board1.update({'1': 'x'})
                count -= 1
            return count
        # 2
        if 271 <= x <= 413 and 52 <= y <= 223:
            if board1['2'] == '':
                cross(280, 80)
                board1.update({'2': 'x'})
                count -= 1
            return count
        # 3
        if 458 <= x <= 635 and 52 <= y <= 223:
            if board1['3'] == '':
                cross(470, 80)
                board1.update({'3': 'x'})
                count -= 1
            return count
        # 4
        if 48 <= x <= 226 and 271 <= y <= 414:
            if board1['4'] == '':
                cross(60, 280)
                board1.update({'4': 'x'})
                count -= 1
            return count
        # 5
        if 269 <= x <= 412 and 272 <= y <= 415:
            if board1['5'] == '':
                cross(280, 280)
                board1.update({'5': 'x'})
                count -= 1
            return count
        # 6
        if 454 <= x <= 630 and 272 <= y <= 410:
            if board1['6'] == '':
                cross(460, 280)
                board1.update({'6': 'x'})
                count -= 1
            return count
        # 7
        if 55 <= x <= 220 and 465 <= y <= 625:
            if board1['7'] == '':
                cross(60, 480)
                board1.update({'7': 'x'})
                count -= 1
            return count
        # 8
        if 271 <= x <= 415 and 460 <= y <= 625:
            if board1['8'] == '':
                cross(280, 480)
                board1.update({'8': 'x'})
                count -= 1
            return count
        # 9
        if 458 <= x <= 630 and 460 <= y <= 625:
            if board1['9'] == '':
                cross(470, 480)
                board1.update({'9': 'x'})
                count -= 1
            return count
        else:
            return count
    else:
        # 1
        if 44 <= x <= 218 and 52 <= y <= 223:
            if board1['1'] == '':
                circle(60, 80)
                board1.update({'1': 'o'})
                count -= 1
            return count
        # 2
        if 271 <= x <= 413 and 52 <= y <= 223:
            if board1['2'] == '':
                circle(280, 80)
                board1.update({'2': 'o'})
                count -= 1
            return count
        # 3
        if 458 <= x <= 635 and 52 <= y <= 223:
            if board1['3'] == '':
                circle(470, 80)
                board1.update({'3': 'o'})
                count -= 1
            return count
        # 4
        if 48 <= x <= 226 and 271 <= y <= 414:
            if board1['4'] == '':
                circle(60, 280)
                board1.update({'4': 'o'})
                count -= 1
            return count
        # 5
        if 269 <= x <= 412 and 272 <= y <= 415:
            if board1['5'] == '':
                circle(280, 280)
                board1.update({'5': 'o'})
                count -= 1
            return count
        # 6
        if 454 <= x <= 630 and 272 <= y <= 410:
            if board1['6'] == '':
                circle(460, 280)
                board1.update({'6': 'o'})
                count -= 1
            return count
        # 7
        if 55 <= x <= 220 and 465 <= y <= 625:
            if board1['7'] == '':
                circle(60, 480)
                board1.update({'7': 'o'})
                count -= 1
            return count
        # 8
        if 271 <= x <= 415 and 460 <= y <= 625:
            if board1['8'] == '':
                circle(280, 480)
                board1.update({'8': 'o'})
                count -= 1
            return count
        # 9
        if 458 <= x <= 630 and 460 <= y <= 625:
            if board1['9'] == '':
                circle(470, 480)
                board1.update({'9': 'o'})
                count -= 1
            return count
        else:
            return count


def place_checker_for_y(count, x, y):
    if count == 9 or count == 7 or count == 5 or count == 3 or count == 1:
        # 1
        if 44 <= x <= 218 and 52 <= y <= 223:
            if board1['1'] == '':
                circle(60, 80)
                board1.update({'1': 'o'})
                count -= 1
            return count
        # 2
        if 271 <= x <= 413 and 52 <= y <= 223:
            if board1['2'] == '':
                circle(280, 80)
                board1.update({'2': 'o'})
                count -= 1
            return count
        # 3
        if 458 <= x <= 635 and 52 <= y <= 223:
            if board1['3'] == '':
                circle(470, 80)
                board1.update({'3': 'o'})
                count -= 1
            return count
        # 4
        if 48 <= x <= 226 and 271 <= y <= 414:
            if board1['4'] == '':
                circle(60, 280)
                board1.update({'4': 'o'})
                count -= 1
            return count
        # 5
        if 269 <= x <= 412 and 272 <= y <= 415:
            if board1['5'] == '':
                circle(280, 280)
                board1.update({'5': 'o'})
                count -= 1
            return count
        # 6
        if 454 <= x <= 630 and 272 <= y <= 410:
            if board1['6'] == '':
                circle(460, 280)
                board1.update({'6': 'o'})
                count -= 1
            return count
        # 7
        if 55 <= x <= 220 and 465 <= y <= 625:
            if board1['7'] == '':
                circle(60, 480)
                board1.update({'7': 'o'})
                count -= 1
            return count
        # 8
        if 271 <= x <= 415 and 460 <= y <= 625:
            if board1['8'] == '':
                circle(280, 480)
                board1.update({'8': 'o'})
                count -= 1
            return count
        # 9
        if 458 <= x <= 630 and 460 <= y <= 625:
            if board1['9'] == '':
                circle(470, 480)
                board1.update({'9': 'o'})
                count -= 1
            return count
        else:
            return count
    else:
        # 1
        if 44 <= x <= 218 and 52 <= y <= 223:
            if board1['1'] == '':
                cross(60, 80)
                board1.update({'1': 'x'})
                count -= 1
            return count
        # 2
        if 271 <= x <= 413 and 52 <= y <= 223:
            if board1['2'] == '':
                cross(280, 80)
                board1.update({'2': 'x'})
                count -= 1
            return count
        # 3
        if 458 <= x <= 635 and 52 <= y <= 223:
            if board1['3'] == '':
                cross(470, 80)
                board1.update({'3': 'x'})
                count -= 1
            return count
        # 4
        if 48 <= x <= 226 and 271 <= y <= 414:
            if board1['4'] == '':
                cross(60, 280)
                board1.update({'4': 'x'})
                count -= 1
            return count
        # 5
        if 269 <= x <= 412 and 272 <= y <= 415:
            if board1['5'] == '':
                cross(280, 280)
                board1.update({'5': 'x'})
                count -= 1
            return count
        # 6
        if 454 <= x <= 630 and 272 <= y <= 410:
            if board1['6'] == '':
                cross(460, 280)
                board1.update({'6': 'x'})
                count -= 1
            return count
        # 7
        if 55 <= x <= 220 and 465 <= y <= 625:
            if board1['7'] == '':
                cross(60, 480)
                board1.update({'7': 'x'})
                count -= 1
            return count
        # 8
        if 271 <= x <= 415 and 460 <= y <= 625:
            if board1['8'] == '':
                cross(280, 480)
                board1.update({'8': 'x'})
                count -= 1
            return count
        # 9
        if 458 <= x <= 630 and 460 <= y <= 625:
            if board1['9'] == '':
                cross(470, 480)
                board1.update({'9': 'x'})
                count -= 1
            return count
        else:
            return count


def winner():
    if board1['7'] == board1['8'] == board1['9'] == 'x':
        print("\nGame Over.\n")
        return 0, 'x'
    if board1['4'] == board1['5'] == board1['6'] == 'x':
        print("\nGame Over.\n")
        return 0, 'x'
    if board1['1'] == board1['2'] == board1['3'] == 'x':
        print("\nGame Over.\n")
        return 0, 'x'
    if board1['1'] == board1['4'] == board1['7'] == 'x':
        print("\nGame Over.\n")
        return 0, 'x'
    if board1['2'] == board1['5'] == board1['8'] == 'x':
        print("\nGame Over.\n")
        return 0, 'x'
    if board1['3'] == board1['6'] == board1['9'] == 'x':
        print("\nGame Over.\n")
        return 0, 'x'
    if board1['7'] == board1['5'] == board1['3'] == 'x':
        print("\nGame Over.\n")
        return 0, 'x'
    if board1['1'] == board1['5'] == board1['9'] == 'x':
        print("\nGame Over.\n")
        return 0, 'x'
    if board1['7'] == board1['8'] == board1['9'] == 'o':
        print("\nGame Over.\n")
        return 0, 'o'
    if board1['4'] == board1['5'] == board1['6'] == 'o':
        print("\nGame Over.\n")
        return 0, 'o'
    if board1['1'] == board1['2'] == board1['3'] == 'o':
        print("\nGame Over.\n")
        return 0, 'o'
    if board1['1'] == board1['4'] == board1['7'] == 'o':
        print("\nGame Over.\n")
        return 0, 'o'
    if board1['2'] == board1['5'] == board1['8'] == 'o':
        print("\nGame Over.\n")
        return 0, 'o'
    if board1['3'] == board1['6'] == board1['9'] == 'o':
        print("\nGame Over.\n")
        return 0, 'o'
    if board1['7'] == board1['5'] == board1['3'] == 'o':
        print("\nGame Over.\n")
        return 0, 'o'
    if board1['1'] == board1['5'] == board1['9'] == 'o':
        print("\nGame Over.\n")
        return 0, 'o'
    else:
        return 1, ''


def game_over_text(symbol):
    over_text_1 = over_font.render("GAME OVER !!", True, (0, 0, 255))
    over_text_2 = over_font.render(symbol + " Wins", True, (0, 0, 255))
    screen.blit(over_text_1, (150, 250))
    screen.blit(over_text_2, (260, 320))


def game_over_text1():
    over_text_1 = over_font.render("GAME OVER !!", True, (0, 0, 255))
    over_text_2 = over_font.render("IT's A TIE", True, (0, 0, 255))
    screen.blit(over_text_1, (150, 250))
    screen.blit(over_text_2, (230, 320))


count = 9
cont = 1

while running:

    for event in pygame.event.get():

        # when game is closed
        if event.type == pygame.QUIT:
            running = False

        # who will play first X or O
        if first == 'X':
            # on clicking mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound = mixer.Sound('mouse-click.wav')
                click_sound.play()
                x, y = pygame.mouse.get_pos()
                count = place_checker_for_x(count, x, y)
                if count < 5:
                    cont, symbol = winner()
                    if cont == 0:
                        board_x = 2000
                        board_y = 2000
                        game_over_text(symbol)
                        break

                if count == 0:
                    board_x = 2000
                    board_y = 2000
                    game_over_text1()
        if first == 'O':
            # on clicking mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound = mixer.Sound('mouse-click.wav')
                click_sound.play()
                x, y = pygame.mouse.get_pos()
                count = place_checker_for_y(count, x, y)
                if count < 5:
                    cont, symbol = winner()
                    if cont == 0:
                        board_x = 2000
                        board_y = 2000
                        game_over_text(symbol)
                        break

                if count == 0:
                    board_x = 2000
                    board_y = 2000
                    game_over_text1()

    board(board_x, board_y)
    pygame.display.update()
