import os
import pygame
import sys
from pygame.locals import *
import random
import array as arr
import collections
import time

win = False
lose = False
pygame.init()
screen = pygame.display.set_mode((900, 725), 0, 32)
grey = (184, 184, 184)
filepath = os.path.dirname(__file__)


def main():
    clickable = True
    screen.fill(grey)

    image_smile = pygame.image.load(os.path.join(filepath, "./images/smile.png"))

    image_small_smile = pygame.transform.scale(image_smile, (400, 340))
    screen.blit(image_small_smile, (293, -62))

    winCheck = 0
    x = 50
    y = 100

    add_col = 0
    add_row = 0
    row_num = 11
    column_num = 15

    game_running = True
    pygame.display.set_caption("MineSweeper")

    image = pygame.image.load(os.path.join(filepath, "./images/blank.png"))
    image_small = pygame.transform.scale(image, (50, 50))
    image_flag = pygame.image.load(os.path.join(filepath, "./images/flag.png"))
    image_flag_small = pygame.transform.scale(image_flag, (50, 50))
    image_mine = pygame.image.load(os.path.join(filepath, "./images/mine.PNG"))
    image_mine_small = pygame.transform.scale(image_mine, (50, 50))
    image1 = pygame.image.load(os.path.join(filepath, "./images/1.png"))
    image1_small = pygame.transform.scale(image1, (50, 50))
    image2 = pygame.image.load(os.path.join(filepath, "./images/2.png"))
    image2_small = pygame.transform.scale(image2, (50, 50))
    image3 = pygame.image.load(os.path.join(filepath, "./images/3.png"))
    image3_small = pygame.transform.scale(image3, (50, 50))
    image4 = pygame.image.load(os.path.join(filepath, "./images/4.PNG"))
    image4_small = pygame.transform.scale(image4, (50, 50))
    image5 = pygame.image.load(os.path.join(filepath, "./images/5.png"))
    image5_small = pygame.transform.scale(image5, (50, 50))
    image0 = pygame.image.load(os.path.join(filepath, "./images/0000.gif"))
    image0_small = pygame.transform.scale(image0, (50, 50))

    mine_coordinates = []
    mine_coordinates_win = []
    mine_num = 20
    mine_add = 0
    mine_near = 0
    flag_coor = []
    coor = []
    while add_row <= row_num:
        while add_col <= column_num:
            b = screen.blit(image_small, (x, y))
            x = x + 50
            add_col = add_col + 1
        y = y + 50
        x = 50
        add_col = 0
        add_row = add_row + 1

    while mine_add <= mine_num:
        mine_x = random.randint(1, 16)
        mine_y = random.randint(2, 13)
        mine_x_y = (mine_x * 50, mine_y * 50)
        mine_coordinates.append((mine_x_y))
        mine_coordinates_win.append((mine_x_y))

        mine_add = mine_add + 1
    pygame.event.get()
    while game_running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_x_calc = mouse_x // 50
            mouse_y_calc = mouse_y // 50
            mouse_calc_x_y = (mouse_x_calc, mouse_y_calc)
            if (
                event.type == MOUSEBUTTONDOWN
                and event.button == 3
                and clickable == True
            ):
                flag_y = (mouse_y // 50) * 50
                flag_x = (mouse_x // 50) * 50
                if (1 <= mouse_x_calc <= 16) and (2 <= mouse_y_calc <= 14):
                    b3 = screen.blit(image_flag_small, (flag_x, flag_y))
                    flags = []
                    print(mine_coordinates_win)
                    if (flag_x, flag_y) in mine_coordinates_win:
                        mine_coordinates_win.remove((flag_x, flag_y))
                        coor.append((flag_x, flag_y))
                    elif (flag_x, flag_y) in coor:
                        screen.blit(image_small, (flag_x, flag_y))
                        coor.remove((flag_x, flag_y))
                    coor.append((flag_x, flag_y))

                    if sorted(mine_coordinates_win) == sorted(flag_coor):
                        global win
                        win = True
                        print("you win")
                        image_sad = pygame.image.load(
                            os.path.join(filepath, "./images/sunglass.jpg")
                        )
                        image_small_sad = pygame.transform.scale(image_sad, (135, 104))
                        screen.blit(image_small_sad, (400, -3))

                else:
                    print("non square")

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mine_x_click, mine_y_click = pygame.mouse.get_pos()
                mine_x_click_calc = (mine_x_click // 50) * 50
                mine_y_click_calc = (mine_y_click // 50) * 50
                mine_calc_x_y = (mine_x_click_calc, mine_y_click_calc)
                if mine_calc_x_y in flag_coor:
                    print("you cannot click on a flag sucker")
                elif (400 <= mine_x_click_calc <= 450) and (
                    -62 <= mine_y_click_calc <= 50
                ):
                    main()

                elif (
                    (50 <= mine_x_click_calc <= 16 * 50)
                    and (2 * 50 <= mine_y_click_calc <= 13 * 50)
                    and clickable == True
                ):

                    def nine(pocket_x, pocket_y):
                        if pocket_x == 50:
                            surrounding_x = [
                                (pocket_x + 50),
                                (pocket_x + 50),
                                (pocket_x + 50),
                                (pocket_x),
                                (pocket_x),
                            ]
                            surrounding_y = [
                                pocket_y,
                                (pocket_y + 50),
                                (pocket_y - 50),
                                (pocket_y + 50),
                                (pocket_y - 50),
                            ]
                            check = 0
                            while check < 5:
                                print((surrounding_x[check], surrounding_y[check]))
                                print(check)
                                bubbles(surrounding_x[check], surrounding_y[check])
                                check += 1
                        elif pocket_x == 800:
                            surrounding_x = [
                                (pocket_x - 50),
                                (pocket_x - 50),
                                (pocket_x - 50),
                                (pocket_x),
                                (pocket_x),
                            ]
                            surrounding_y = [
                                pocket_y,
                                (pocket_y + 50),
                                (pocket_y - 50),
                                (pocket_y + 50),
                                (pocket_y - 50),
                            ]
                            check = 0
                            while check < 5:
                                print((surrounding_x[check], surrounding_y[check]))
                                print(check)
                                bubbles(surrounding_x[check], surrounding_y[check])
                                check += 1
                        elif pocket_y == 100:
                            surrounding_y = [
                                (pocket_y + 50),
                                (pocket_y + 50),
                                (pocket_y + 50),
                                (pocket_y),
                                (pocket_y),
                            ]
                            surrounding_x = [
                                pocket_x,
                                (pocket_x + 50),
                                (pocket_x - 50),
                                (pocket_x - 50),
                                (pocket_x + 50),
                            ]
                            check = 0
                            while check < 5:
                                print((surrounding_x[check], surrounding_y[check]))
                                print(check)
                                bubbles(surrounding_x[check], surrounding_y[check])
                                check += 1
                        elif pocket_y == 650:
                            print(800)
                            surrounding_y = [
                                (pocket_y - 50),
                                (pocket_y - 50),
                                (pocket_y - 50),
                                (pocket_y),
                                (pocket_y),
                            ]
                            surrounding_x = [
                                pocket_x,
                                (pocket_x + 50),
                                (pocket_x - 50),
                                (pocket_x - 50),
                                (pocket_x + 50),
                            ]
                            check = 0
                            while check < 5:
                                print((surrounding_x[check], surrounding_y[check]))
                                print(check)
                                bubbles(surrounding_x[check], surrounding_y[check])
                                check += 1

                        else:
                            surrounding_x = [
                                (pocket_x - 50),
                                (pocket_x + 50),
                                (pocket_x + 50),
                                (pocket_x + 50),
                                (pocket_x - 50),
                                (pocket_x - 50),
                                (pocket_x),
                                (pocket_x),
                            ]
                            surrounding_y = [
                                pocket_y,
                                pocket_y,
                                (pocket_y + 50),
                                (pocket_y - 50),
                                (pocket_y + 50),
                                (pocket_y - 50),
                                (pocket_y + 50),
                                (pocket_y - 50),
                            ]
                            check = 0
                            while check < 8:
                                print((surrounding_x[check], surrounding_y[check]))
                                print(check)
                                bubbles(surrounding_x[check], surrounding_y[check])
                                if (
                                    bubbles3(surrounding_x[check], surrounding_y[check])
                                    == 0
                                ):
                                    peck = 0
                                    while peck < 8:
                                        print(
                                            (surrounding_x[check], surrounding_y[check])
                                        )
                                        print(check)
                                        bubbles(
                                            surrounding_x[check], surrounding_y[check]
                                        )
                                        peck += 1
                                check += 1

                    def bubbles(bubble_x, bubble_y):
                        bubbles_left = ((bubble_x - 50), bubble_y)
                        bubbles_right = ((bubble_x + 50), bubble_y)
                        bubbles_right_up = ((bubble_x + 50), bubble_y + 50)
                        bubbles_right_down = ((bubble_x + 50), bubble_y - 50)
                        bubbles_left_up = ((bubble_x - 50), bubble_y + 50)
                        bubbles_left_down = ((bubble_x - 50), bubble_y - 50)
                        bubbles_up = ((bubble_x), bubble_y + 50)
                        bubbles_down = ((bubble_x), bubble_y - 50)
                        mines = 0
                        if bubbles_left in mine_coordinates:
                            mines += 1
                        if bubbles_right in mine_coordinates:
                            mines += 1
                        if bubbles_right_up in mine_coordinates:
                            mines += 1
                        if bubbles_right_down in mine_coordinates:
                            mines += 1
                        if bubbles_left_up in mine_coordinates:
                            mines += 1
                        if bubbles_left_down in mine_coordinates:
                            mines += 1
                        if bubbles_up in mine_coordinates:
                            mines += 1
                        if bubbles_down in mine_coordinates:
                            mines += 1
                            # check number
                        if mines == 0:
                            screen.blit(image0_small, (bubble_x, bubble_y))
                        if mines == 1:
                            screen.blit(image1_small, (bubble_x, bubble_y))
                        if mines == 2:
                            screen.blit(image2_small, (bubble_x, bubble_y))
                        if mines == 3:
                            screen.blit(image3_small, (bubble_x, bubble_y))
                        if mines == 4:
                            screen.blit(image4_small, (bubble_x, bubble_y))
                        if mines == 5:
                            screen.blit(image5_small, (bubble_x, bubble_y))

                    def bubbles3(bubble_x, bubble_y):
                        bubbles_left = ((bubble_x - 50), bubble_y)
                        bubbles_right = ((bubble_x + 50), bubble_y)
                        bubbles_right_up = ((bubble_x + 50), bubble_y + 50)
                        bubbles_right_down = ((bubble_x + 50), bubble_y - 50)
                        bubbles_left_up = ((bubble_x - 50), bubble_y + 50)
                        bubbles_left_down = ((bubble_x - 50), bubble_y - 50)
                        bubbles_up = ((bubble_x), bubble_y + 50)
                        bubbles_down = ((bubble_x), bubble_y - 50)
                        mines = 0
                        if bubbles_left in mine_coordinates:
                            mines += 1
                        if bubbles_right in mine_coordinates:
                            mines += 1
                        if bubbles_right_up in mine_coordinates:
                            mines += 1
                        if bubbles_right_down in mine_coordinates:
                            mines += 1
                        if bubbles_left_up in mine_coordinates:
                            mines += 1
                        if bubbles_left_down in mine_coordinates:
                            mines += 1
                        if bubbles_up in mine_coordinates:
                            mines += 1
                        if bubbles_down in mine_coordinates:
                            mines += 1
                            # check number
                        if mines == 0:
                            return 0

                        if mines == 1:
                            return 0
                        if mines == 2:
                            return 2
                        if mines == 3:
                            return 3
                        if mines == 4:
                            return 4
                        if mines == 5:
                            return 5

                    def bubbles2(bubble_x, bubble_y):
                        bubbles_left = ((bubble_x - 50), bubble_y)
                        bubbles_right = ((bubble_x + 50), bubble_y)
                        bubbles_right_up = ((bubble_x + 50), bubble_y + 50)
                        bubbles_right_down = ((bubble_x + 50), bubble_y - 50)
                        bubbles_left_up = ((bubble_x - 50), bubble_y + 50)
                        bubbles_left_down = ((bubble_x - 50), bubble_y - 50)
                        bubbles_up = ((bubble_x), bubble_y + 50)
                        bubbles_down = ((bubble_x), bubble_y - 50)
                        mines = 0
                        if bubbles_left in mine_coordinates:
                            mines += 1
                        if bubbles_right in mine_coordinates:
                            mines += 1
                        if bubbles_right_up in mine_coordinates:
                            mines += 1
                        if bubbles_right_down in mine_coordinates:
                            mines += 1
                        if bubbles_left_up in mine_coordinates:
                            mines += 1
                        if bubbles_left_down in mine_coordinates:
                            mines += 1
                        if bubbles_up in mine_coordinates:
                            mines += 1
                        if bubbles_down in mine_coordinates:
                            mines += 1
                            # check number
                        if mines == 0:
                            screen.blit(image0_small, (bubble_x, bubble_y))
                            nine(bubble_x, bubble_y)
                        if mines == 1:
                            screen.blit(image1_small, (bubble_x, bubble_y))
                        if mines == 2:
                            screen.blit(image2_small, (bubble_x, bubble_y))
                        if mines == 3:
                            screen.blit(image3_small, (bubble_x, bubble_y))
                        if mines == 4:
                            screen.blit(image4_small, (bubble_x, bubble_y))
                        if mines == 5:
                            screen.blit(image5_small, (bubble_x, bubble_y))

                    bubbles2(mine_x_click_calc, mine_y_click_calc)

                    print(mine_calc_x_y)

                if mine_calc_x_y in mine_coordinates:
                    print("you lose")
                    mine_add_1 = 0
                    while mine_add_1 <= 15:
                        m_x = mine_coordinates[mine_add_1]
                        screen.blit(image_mine_small, (m_x))
                        mine_add_1 = mine_add_1 + 1

                    global lose
                    lose = True
                    print("sleep")
                    image_sad = pygame.image.load(
                        os.path.join(filepath, "./images/sad.png")
                    )
                    image_small_sad = pygame.transform.scale(image_sad, (135, 104))
                    screen.blit(image_small_sad, (400, -3))

                    # global clickable
                    clickable = False

        pygame.display.update()


while lose == False:
    main()
    print(lose)
