import sys

import pygame
from pygame.locals import *

pygame.init()

f=0
fps = 60
fpsClock = pygame.time.Clock()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

#из равновесия в лево и обратно
def rov_to_l(f, lever):
    if f % 5 != 0:
        lever[0][1] = lever[0][1] + 1  # y
        lever[1][1] = lever[1][1] - 1  # y
        lever[2][1] = lever[2][1] - 1  # y
        lever[3][1] = lever[3][1] + 1  # y
        if f % 6 == 0:
            lever[1][0] = lever[1][0] - 1  # x
            lever[3][0] = lever[3][0] + 1  # x
    else:
        lever[0][0] = lever[0][0] + 1  # x
        lever[0][1] = lever[0][1] + 1  # y
        lever[1][0] = lever[1][0] - 1  # x
        lever[1][1] = lever[1][1] - 1  # y
        lever[2][0] = lever[2][0] - 1  # x
        lever[2][1] = lever[2][1] - 1  # y
        lever[3][0] = lever[3][0] + 1  # x
        lever[3][1] = lever[3][1] + 1  # y
        if f % 6 == 0:
            lever[1][0] = lever[1][0] - 1  # x
            lever[3][0] = lever[3][0] + 1  # x
    return lever

def l_to_rov(f, lever):
    if f % 5 != 0:
        lever[0][1] = lever[0][1] - 1  # y
        lever[1][1] = lever[1][1] + 1  # y
        lever[2][1] = lever[2][1] + 1  # y
        lever[3][1] = lever[3][1] - 1  # y
        if f % 6 == 0:
            lever[1][0] = lever[1][0] + 1  # x
            lever[3][0] = lever[3][0] - 1  # x
    else:
        lever[0][0] = lever[0][0] - 1  # x
        lever[0][1] = lever[0][1] - 1  # y
        lever[1][0] = lever[1][0] + 1  # x
        lever[1][1] = lever[1][1] + 1  # y
        lever[2][0] = lever[2][0] + 1  # x
        lever[2][1] = lever[2][1] + 1  # y
        lever[3][0] = lever[3][0] - 1  # x
        lever[3][1] = lever[3][1] - 1  # y
        if f % 6 == 0:
            lever[1][0] = lever[1][0] + 1  # x
            lever[3][0] = lever[3][0] - 1  # x
    return lever

#из равновесия в лево и обратно
#из равновесия в право и обратно

def r_to_rov(f, lever):
    if f % 5 != 0:
        lever[0][1] = lever[0][1] + 1  # y
        lever[1][1] = lever[1][1] - 1  # y
        lever[2][1] = lever[2][1] - 1  # y
        lever[3][1] = lever[3][1] + 1  # y
        if f % 6 == 0:
            lever[0][0] = lever[0][0] - 1  # x
            lever[2][0] = lever[2][0] + 1  # x
    else:
        lever[0][0] = lever[0][0] - 1  # x
        lever[0][1] = lever[0][1] + 1  # y
        lever[1][0] = lever[1][0] + 1  # x
        lever[1][1] = lever[1][1] - 1  # y
        lever[2][0] = lever[2][0] + 1  # x
        lever[2][1] = lever[2][1] - 1  # y
        lever[3][0] = lever[3][0] - 1  # x
        lever[3][1] = lever[3][1] + 1  # y
        if f % 6 == 0:
            lever[0][0] = lever[0][0] - 1  # x
            lever[2][0] = lever[2][0] + 1  # x
    return lever

def rov_to_r(f, lever):
    if f % 5 != 0:
        lever[0][1] = lever[0][1] - 1  # y
        lever[1][1] = lever[1][1] + 1  # y
        lever[2][1] = lever[2][1] + 1  # y
        lever[3][1] = lever[3][1] - 1  # y
        if f % 6 == 0:
            lever[0][0] = lever[0][0] + 1  # x
            lever[2][0] = lever[2][0] - 1  # x
    else:
        lever[0][0] = lever[0][0] + 1  # x
        lever[0][1] = lever[0][1] - 1  # y
        lever[1][0] = lever[1][0] - 1  # x
        lever[1][1] = lever[1][1] + 1  # y
        lever[2][0] = lever[2][0] - 1  # x
        lever[2][1] = lever[2][1] + 1  # y
        lever[3][0] = lever[3][0] + 1  # x
        lever[3][1] = lever[3][1] - 1  # y
        if f % 6 == 0:
            lever[0][0] = lever[0][0] + 1  # x
            lever[2][0] = lever[2][0] - 1  # x
    return lever
#из равновесия в право и обратно
#движение верёвок вверх
def rope_u(rope):
    rope[0][1] = rope[0][1] - 1
    rope[1][1] = rope[1][1] - 1
    rope[2][1] = rope[2][1] - 1
#движение верёвок вверх
#движение верёвок вниз
def rope_d(rope):
    rope[0][1] = rope[0][1] + 1
    rope[1][1] = rope[1][1] + 1
    rope[2][1] = rope[2][1] + 1
#движение верёвок вниз

#создание объектов
ground = pygame.Rect(0, 500, 1280, 240)
color1 = (53, 104, 45)
"земля"
rect1 = pygame.Rect(400 - 250, 560, 480, 100)
rect2 = pygame.Rect(590 - 250, 100, 100, 500)
color2 = (164, 116, 73)
"подставка"
rect3 = pygame.Rect(340 - 250, 120, 600, 50)
lever = [[90, 120], [690, 120], [690, 170], [90, 170]]
color3 = (101, 56, 24)
"плечо"
l_scales = pygame.Rect(280 - 250, 340, 240, 25)
color4 = (128, 128, 128)
"левая чаша"
l_rope = [[150, 140], [40, 340], [260, 340]]
color5 = (10, 10, 10)
"левые верёвки"
r_scales = pygame.Rect(760 - 250, 340, 240, 25)
"правая чаша"
r_rope = [[150+480, 140], [40+480, 340], [260+480, 340]]
"правые верёвки"


# Game loop.
while True:
    screen.fill((66, 170, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if f < 90:
        rov_to_l(f, lever)
        rope_d(l_rope)
        rope_u(r_rope)
        l_scales.y += 1
        r_scales.y -= 1
        f += 1
    if 90 <= f < 180:
        l_to_rov(f, lever)
        rope_d(r_rope)
        rope_u(l_rope)
        l_scales.y -= 1
        r_scales.y += 1
        f += 1
    if 180 <= f < 270:
        rov_to_r(f, lever)
        rope_d(r_rope)
        rope_u(l_rope)
        l_scales.y -= 1
        r_scales.y += 1
        f += 1
    if 270 <= f < 360:
        r_to_rov(f, lever)
        rope_d(l_rope)
        rope_u(r_rope)
        l_scales.y += 1
        r_scales.y -= 1
        f += 1


    """if f < 600:
        rect1.x += 1
        f += 1"""

    # Draw.
    pygame.draw.rect(screen, color1, ground, 0)
    pygame.draw.rect(screen, color2, rect1, 0)
    pygame.draw.rect(screen, color2, rect2, 0)
    pygame.draw.polygon(screen, color3, lever, 0)
    pygame.draw.polygon(screen, color5, l_rope, 10)
    pygame.draw.polygon(screen, color5, r_rope, 10)
    pygame.draw.rect(screen, color4, l_scales, 0)
    pygame.draw.rect(screen, color4, r_scales, 0)
    pygame.display.flip()
    fpsClock.tick(fps)