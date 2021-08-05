# importing the required modules
import pygame
import sys
from pygame import mixer
import random
import math
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

import time

# initialising the pygame
pygame.init()

# variables_used
line_image = pygame.image.load(resource_path('—Pngtree—black simple and proportional thin_5487818 (1).png'))
height = 675
width = 500
icon = pygame.image.load(resource_path("001-tank16.png"))
background_image_1 = pygame.image.load(resource_path('Screenshot 2021-03-24 203113.png'))
background_image_2 = pygame.image.load(resource_path('Screenshot 2021-03-24 203113.png'))
tank_image = pygame.image.load(resource_path('001-tank64.png'))
y1 = 0
y2 = -675
track_speed = 1

tank_x = width / 2 - 25
tank_y = height - 100
tank_xc = 0
bullet_y = height - 100
bullet_x = tank_x + 20
bullet_image = pygame.image.load(resource_path('001-bullet.png'))
bullet_yc = 0
bullet_xc = 0
# ##### enemy #######
enemy_1x = random.randint(40, 410)
enemy_1y = -100
enemy_1xc = 0
enemy_1yc = 3
enemy_1_image = pygame.image.load(resource_path('002-tank-1.png'))

enemy_2x = random.randint(40, 410)
enemy_2y = -20000
enemy_2xc = 0
enemy_2yc = 10
enemy_2_image = pygame.image.load(resource_path('002-jet-1.png'))

mine_x = random.randint(150, 300)
mine_y = -200
mine_xc = 0
mine_yc = track_speed
mine_image = pygame.image.load(resource_path('icons8-fluent-50.png'))

mine_2x = random.randint(150, 300)
mine_2y = -400
mine_2xc = 0
mine_2yc = track_speed
mine_2image = pygame.image.load(resource_path('icons8-fluent-50.png'))

boss_x = random.randint(120, 300)
boss_y = -3000
boss_xc = 4
boss_yc = 2
boss_image = pygame.image.load(resource_path('009-tank.png'))
boss_life = 30
# score
score = 0
highscore = []
life = 100
life_image = pygame.image.load(resource_path('001-heart.png'))
life_x = random.randint(120, 300)
life_y = -1000
life_xc = 4
life_yc = 3
# designing the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TANK SHOOTING")
pygame.display.set_icon(icon)

# background music
mixer.music.load(resource_path('videoplayback (3).mp3'))
pygame.mixer.music.set_volume(0.1)
mixer.music.play(-1)

explosions = [pygame.image.load(resource_path('exp1.png')), pygame.image.load(resource_path('exp2.png')), pygame.image.load(resource_path('exp3.png')),
              pygame.image.load(resource_path('exp4.png')), pygame.image.load(resource_path('exp5.png'))]
clock = pygame.time.Clock()

run = True


# defining the functions.
def show_tank():
    screen.blit(tank_image, (tank_x, tank_y))


def show_bullet():
    global tank_y
    global tank_x
    if bullet_y < tank_y:
        screen.blit(bullet_image, (bullet_x, bullet_y))


def ready_bullet():
    global bullet_yc
    global bullet_y
    global bullet_x
    global tank_x
    global tank_y
    bullet_yc = 0
    bullet_y = tank_y
    bullet_x = tank_x + 20


def fire_bullet():
    global bullet_yc
    global bullet_y
    global bullet_x
    global tank_x
    global tank_y
    bullet_x = tank_x + 20
    bullet_yc = -20


def show_enemy():
    screen.blit(enemy_1_image, (enemy_1x, enemy_1y))
    screen.blit(enemy_2_image, (enemy_2x, enemy_2y))
    screen.blit(boss_image, (boss_x, boss_y))


def show_mine():
    screen.blit(mine_image, (mine_x, mine_y))
    screen.blit(mine_image, (mine_2x, mine_2y))


def is_collision(a, b, x, y,d):
    dist_btw_bullet_enemy = math.sqrt(math.pow(a - x, 2) + math.pow(b - y, 2))
    if dist_btw_bullet_enemy <= d:
        return True


def explosion_animation(x, y):
    for explosion in explosions:
        screen.blit(explosion, (x, y))
        pygame.display.update()
        if explosion == explosions[4]:
            break


def score_display(x, y):
    font = pygame.font.Font(resource_path('FreeSansBold.ttf'), 32)

    score_display = font.render('SCORE:' + str(score), True, (230, 230, 230))
    screen.blit(score_display, (x, y))


def highscore_display(x, y):
    font = pygame.font.Font(resource_path('FreeSansBold.ttf'), 25)

    highscore_display = font.render('HIGH-SCORE:' + str(max(highscore)), True, (230, 230, 230))
    screen.blit(highscore_display, (x, y))


def life_display(x, y):
    screen.blit(life_image, (life_x, life_y))
    font = pygame.font.Font(resource_path('FreeSansBold.ttf'), 25)

    life_display = font.render('LIFE:' + str(life), True, (250, 230, 230))
    screen.blit(life_display, (x, y))


def game_over(x, y, x1, y1):
    screen.blit(background_image_1, (0, 0))
    font = pygame.font.Font(resource_path('FreeSansBold.ttf'), 60)
    game_over_display = font.render('GAME  OVER', True, (255, 0, 0))
    screen.blit(game_over_display, (x, y))

    font_replay = pygame.font.Font(resource_path('FreeSansBold.ttf'), 25)
    replay = font_replay.render('press enter to replay.', True, (230, 230, 230))
    screen.blit(replay, (x1, y1))
    score_display(60, 320)
    highscore_display(60, 360)


def main():
    global score
    global life
    global bullet_yc
    global bullet_y
    global bullet_x
    global tank_x
    global tank_y
    global tank_xc
    global y1
    global y2
    global track_speed
    global enemy_1x
    global enemy_1y
    global enemy_2x
    global enemy_2y
    global enemy_2yc
    global enemy_2xc
    global enemy_1xc
    global enemy_1yc
    global boss_x
    global boss_y
    global boss_yc
    global boss_xc
    global boss_life
    global mine_y
    global mine_x
    global mine_2x
    global mine_yc
    global mine_2xc
    global mine_2y
    global life_x
    global life_y
    global life_yc
    global life_xc
    global run
    global acceleration_sound

    # resetting variables to initial value
    run = True
    y1 = 0
    y2 = -675
    track_speed = 1
    tank_x = width / 2 - 25
    tank_y = height - 100
    tank_xc = 0
    bullet_y = height - 100
    bullet_x = tank_x + 20
    bullet_yc = 0
    # ##### enemy #######
    enemy_1x = random.randint(40, 410)
    enemy_1y = -100
    enemy_1xc = 0
    enemy_1yc = 3
    enemy_2x = random.randint(40, 410)
    enemy_2y = -20000
    enemy_2xc = 0
    enemy_2yc = 10
    mine_x = random.randint(150, 300)
    mine_y = -200
    mine_yc = track_speed
    mine_2x = random.randint(150, 300)
    mine_2y = -400
    mine_2xc = 0
    boss_x = random.randint(120, 300)
    boss_y = -5000
    boss_xc = 4
    boss_yc = 2
    boss_life = 5
    # score
    score = 0
    life = 100
    life_x = random.randint(120, 300)
    life_y = -1000
    life_xc = 4
    life_yc = 6
    # making the infinite loop.
    while run:
        pygame.time.delay(20)
        screen.blit(background_image_1, (0, y1))
        screen.blit(background_image_2, (0, y2))
        for event in pygame.event.get():
            # exit event
            if event.type == pygame.QUIT:
                sys.exit()

            # moving tank and firing the bullets
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    tank_xc = 10

                if event.key == pygame.K_LEFT:
                    tank_xc = -10
                if event.key == pygame.K_UP:
                    track_speed = 4
                    enemy_1yc = 6
                    enemy_2yc = 20
                    boss_yc = 2 * 2
                    life_yc = 6
                    acceleration_sound = mixer.Sound(
                        resource_path('Car-Driving-B1-www.fesliyanstudios.com-[AudioTrimmer.com] (1).mp3'))
                    acceleration_sound.play(-1)

                if event.key == pygame.K_SPACE:
                    if bullet_y == tank_y:
                        bullet_sound = mixer.Sound(resource_path('GunShotSnglShotIn PE1097906.mp3'))
                        bullet_sound.play()
                        fire_bullet()
                if event.key == pygame.K_RETURN:
                    run = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    tank_xc = 0
                if event.key == pygame.K_UP:
                    track_speed = 1
                    enemy_1yc = 3
                    enemy_2yc = 10
                    boss_yc = 2
                    life_yc = 3
                    acceleration_sound.stop()
            # #### collision ######
            collision1 = is_collision(enemy_1x+40, enemy_1y+40, bullet_x, bullet_y,100)
            if collision1 == True:
                ex_sound = mixer.Sound(resource_path('mixkit-bomb-explosion-in-battle-2800.wav'))
                ex_sound.play()
                explosion_animation(enemy_1x, enemy_1y)
                enemy_1x = random.randint(40, 410)
                enemy_1y = -200
                ready_bullet()
                score += 1
            collision2 = is_collision(enemy_2x+40, enemy_2y+40, bullet_x, bullet_y,100)
            if collision2 == True:
                ex_sound = mixer.Sound(resource_path('mixkit-bomb-explosion-in-battle-2800.wav'))
                ex_sound.play()
                explosion_animation(enemy_2x, enemy_2y)
                enemy_2x = random.randint(40, 410)
                enemy_2y = -6000
                ready_bullet()
                score += 10
            collision3 = is_collision(boss_x+80, boss_y+60, bullet_x, bullet_y,100)
            if collision3 == True:
                ex_sound = mixer.Sound(resource_path('mixkit-bomb-explosion-in-battle-2800.wav'))
                ex_sound.play()
                explosion_animation(boss_x+30, boss_y)
                ready_bullet()
                boss_life -= 1
                if boss_life <= 0:
                    boss_x = random.randint(40, 410)
                    boss_y = -3000
                    explosion_animation(boss_x, boss_y)
                    boss_life = 30
                    score += 50
            collision4 = is_collision(mine_x+25, mine_y+25, x=tank_x, y=tank_y,d=50)
            if collision4 == True:
                ex_sound = mixer.Sound(resource_path('mixkit-bomb-explosion-in-battle-2800.wav'))
                ex_sound.play()
                explosion_animation(mine_x, mine_y)
                ready_bullet()
                mine_x = random.randint(40, 410)
                mine_y = random.randint(300, 450)
                explosion_animation(mine_x, mine_y)
                life -= 20
            collision5 = is_collision(mine_2x+25, mine_2y+25, x=tank_x, y=tank_y,d=50)
            if collision5 == True:
                ex_sound = mixer.Sound(resource_path('mixkit-bomb-explosion-in-battle-2800.wav'))
                ex_sound.play()
                explosion_animation(mine_2x, mine_2y)
                ready_bullet()
                mine_2x = random.randint(40, 410)
                mine_2y = random.randint(0, 100)
                explosion_animation(mine_2x, mine_2y)
                life -= 20
            collision6 = is_collision(life_x, life_y, x=tank_x, y=tank_y,d=50)
            if collision6 == True:
                ex_sound = mixer.Sound(resource_path('preview.mp3'))
                ex_sound.play()
                life_x = random.randint(40, 410)
                life_y = random.randint(-4000, -1000)
                life += 5

        y1 += track_speed
        y2 += track_speed

        # making the bullet to move seperately.

        if y1 >= 675:
            y1 = -675
        if y2 >= 675:
            y2 = -675
        bullet_y += bullet_yc
        if bullet_y < 0:
            ready_bullet()

        if tank_x <= 40:
            tank_x = 40
        if tank_x >= 410:
            tank_x = 410
        tank_x += tank_xc

        show_bullet()
        if bullet_y == tank_y:
            bullet_x = tank_x + 20

        # ##### respawning enemy1 #######
        if enemy_1y >= 675:
            enemy_1x = random.randint(40, 410)
            enemy_1y = 0
            life-=10

        enemy_1y += enemy_1yc

        # ##### respawning enemy2 ########
        if enemy_2y >= 675:
            enemy_2x = random.randint(40, 410)
            enemy_2y = -2000
            life-=10

        enemy_2y += enemy_2yc

        # ##### respawning the boss ######
        if boss_y >= 675:
            boss_x = random.randint(120, 300)
            boss_y = -3000
            haha_sound = mixer.Sound(resource_path('videoplayback (7).mp3'))
            haha_sound.play()
            boss_life = 30
            life-=30
        # moving the boss on x axis
        if boss_x >= 300:
            boss_x = 300
            boss_xc = -4

        if boss_x <= 120:
            boss_x = 120
            boss_xc = 4
        # life #####

        if life_y >= 675:
            life_x = random.randint(120, 300)
            life_y = -4000
            # moving the boss on x axis
        if life_x >= 300:
            life_x = 300
            life_xc = -8

        if life_x <= 120:
            life_x = 120
            life_xc = 8

        # when boss is in nobody is allowed.

        if boss_y >= -300 and boss_y <= 675:

            enemy_1yc = 0
            enemy_2yc = 0
            enemy_1y = -100
            enemy_2y = -1000
        elif boss_y >= 675:
            enemy_1yc = 3
            enemy_2yc = 15

        boss_y += boss_yc
        boss_x += boss_xc

        # ##### respawning the mine #######
        if mine_y >= 675:
            mine_y = random.randint(300, 450)
            mine_x = random.randint(40, 380)

        mine_y += track_speed

        if mine_2y >= 675:
            mine_2y = random.randint(0, 100)
            mine_2x = random.randint(40, 380)

        mine_2y += track_speed

        show_mine()
        show_tank()
        show_enemy()
        score_display(10, 10)
        highscore.append(score)
        if enemy_1y >= 530 and enemy_1y <= 600:
            life -= 1
        if enemy_2y >= 530 and enemy_2y <= 600:
            life -= 1
        if boss_y >= 530 and boss_y <= 600:
            life -= 2

        life_x += life_xc
        life_y += life_yc

        life_display(10, 50)
        if life <= 0:
            game_over(60, 250, 10, 10)

        pygame.display.update()

    main()


main()
