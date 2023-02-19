# -*- coding: utf-8 -*-
import random
import sys
import os

import pygame
from pygame import *

FPS = 30
COLORS = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'CYAN': (0, 183, 235),
    'GREY': (187, 187, 187)
}

QUESTIONS = [pygame.image.load(f'Вопросы/{i}') for i in os.listdir('Вопросы')]

pygame.font.init()
FONT = pygame.font.SysFont('comicsansms', 70)
FONT2 = pygame.font.SysFont('comicsansms', 40)


class GameQuestion:
    def __init__(self, question_img, price, answer):
        self.question_img = pygame.image.load(question_img)
        self.price = price
        self.answer = answer
        self.is_answered = False


class GameMember:
    def __init__(self, team_name):
        self.team_name = team_name
        self.team_score = 0


class Teams:
    def __init__(self, team_amount):
        self.team_amount = team_amount

    def teams_amount(self):
        return self.team_amount


# -- screen settings start --
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.init()
# -- screen settings end --

member_list = []


def choose_teams():
    how_many_teams = 0
    pygame.init()
    pygame.font.init()
    FONT = pygame.font.SysFont('comicsansms', 50)

    size_block = 100
    margin = 222  # отступ

    size_window = (1280, 1024)
    screen = pygame.display.set_mode(size_window)
    pygame.display.set_caption('Викторина-выбор команд')

    field = [[0] * 2 for i in range(3)]

    running = True
    while running:
        # screen.fill(COLORS['GREY'])
        screen.blit(pygame.image.load('game_background.jpg'), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    col = x_mouse // (size_block + margin)
                    row = y_mouse // (size_block + margin)

                    if field[row][col] == 'x':
                        field[row][col] = 0

                        # main_game()
                        # exit(0)


                    else:
                        if any([any(i) for i in field]):
                            pass
                        else:
                            field[row][col] = 'x'

                            # ЛЮТЫЙ ГОВНОКОД КОТОРЫЙ СТЫДНО ПОКАЗАТЬ ДАЖЕ МАТЕРИ
                            if row == 0 and col == 0:
                                how_many_teams = 1

                            elif row == 0 and col == 1:
                                how_many_teams = 2

                            elif row == 1 and col == 0:
                                how_many_teams = 3

                            elif row == 1 and col == 1:
                                how_many_teams = 4

                            elif row == 2 and col == 0:
                                how_many_teams = 5

                            elif row == 2 and col == 1:
                                how_many_teams = 6

                        # print(sum([len(i) for i in field]))
                        # print('r-', row)
                        # print('c-', col)
                        # main_game()
                        # exit(0)

                except IndexError:
                    print('IndexError')

            elif event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    print(how_many_teams)
                    for team_number in range(how_many_teams):
                        member_list.append(GameMember(f'Команда {team_number + 1}'))

                    print([i.team_name for i in member_list])
                    main_main_game(member_list)
                    sys.exit()

        counter = 1
        for row in range(3):
            for col in range(2):
                if field[row][col] == 'x':
                    color = COLORS['CYAN']

                else:
                    color = COLORS['WHITE']

                x = col * size_block + (col + 1) * (margin * 1)
                y = row * size_block + (row + 1) * (margin * 1)
                # pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                pygame.draw.circle(screen, color, (x, y), radius=70)

                text = FONT.render(f"{counter}", True, COLORS['BLACK'])
                counter += 1
                screen.blit(text, (x - 18, y - 35))

        text = FONT.render('Выберите количество команд', True, COLORS['WHITE'])
        screen.blit(text, (SCREEN_WIDTH / 15, 50))
        pygame.display.update()


def true_answer(member, price):
    return member.team_score + price


def wrong_answer(member, price):
    if member.team_score - price < 0:
        return member.team_score
    else:
        return member.team_score - price


def switch_team(member_list, current_inx):
    current_inx += 1

    try:
        member_list[current_inx]

    except IndexError:
        current_inx = 0

    return current_inx


def switch_question_or_finish(quest_list, current_inx):
    current_inx += 1

    try:
        quest_list[current_inx]

    except IndexError:
        return 'end'

    return current_inx


def main_main_game(members):
    pygame.display.set_caption('Викторина --идёт игра--')

    current_team_index = 0
    current_quest_index = 0
    question_image = QUESTIONS[current_quest_index]
    player_now = members[current_team_index]

    running = True
    game_ending = True

    while running:
        screen.fill(COLORS['WHITE'])
        screen.blit(question_image, (0, 0))
        cursor_on_left_side = False
        cursor_on_right_side = False
        img_width, img_height = question_image.get_rect()[2:4]

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x < img_width // 2:
            cursor_on_left_side = True
            cursor_on_right_side = False

        elif mouse_x > img_width // 2:
            cursor_on_right_side = True
            cursor_on_left_side = False

        quest_wrong = FONT.render('Неправильно', True, COLORS['BLACK'])
        quest_true = FONT.render('Правильно', True, COLORS['BLACK'])
        team_playing_now = FONT2.render(f'Отвечает {player_now.team_name}: счёт {player_now.team_score}', True,
                                        COLORS['BLACK'])

        if cursor_on_right_side:
            quest_wrong = FONT.render('Неправильно', True, COLORS['RED'])

        if cursor_on_left_side:
            quest_true = FONT.render('Правильно', True, COLORS['GREEN'])

        # E V E N T S
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    # question_image = random.choice(QUESTIONS)

                    if cursor_on_right_side:
                        player_now.team_score = wrong_answer(player_now, price=1)

                    else:
                        player_now.team_score = true_answer(player_now, price=100)

                    current_team_index = switch_team(members, current_team_index)
                    current_quest_index = switch_question_or_finish(QUESTIONS, current_quest_index)

                    player_now = members[current_team_index]

                    if current_quest_index == 'end':
                        running = False
                    else:
                        question_image = QUESTIONS[current_quest_index]

        # E V E N T S

        # ОТРИСОВКА ВСЕГО, ЧТО НАКОДИЛ
        screen.blit(quest_true, (-100 + img_width // 5, img_height))
        screen.blit(quest_wrong, (100 + img_width // 2, img_height))
        screen.blit(team_playing_now, (img_width // 8, img_height + 150))

        pygame.display.flip()

        # FPS LOCK
        pygame.time.Clock().tick(10)

    while game_ending:
        pygame.display.set_caption('Викторина --Таблица результатов--')
        screen.blit(pygame.image.load('background2.jpg'), (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_ending = False

        margin = 100
        for member in sorted(member_list, key=lambda x: x.team_score)[::-1]:
            text = FONT.render(f"{member.team_name}: счёт {member.team_score}", True, COLORS['WHITE'])
            screen.blit(text, (100, (margin + 100)))
            margin += 100
            # for i in

        pygame.display.flip()


choose_teams()