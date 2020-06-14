import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"  ##makes that annoying help text
import pygame, sys, math, time

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

w = pygame.K_w; s = pygame.K_s; a = pygame.K_a; d = pygame.K_d; e = pygame.K_e; q = pygame.K_q; bk = pygame.K_BACKSPACE; sp = pygame.K_SPACE; tb = pygame.K_TAB; esc = pygame.K_ESCAPE; sh = pygame.K_LSHIFT
k = {w: 0, s: 0, a: 0, d: 0, e: 0, q: 0, bk: 0, sp: 0, tb: 0, esc: 0, sh: 0}

pogrimg = pygame.image.load('Assets/pogball_r.png') ##imports pog right image -jake ## https://www.freepngimg.com/thumb/mouth/92712-ear-head-twitch-pogchamp-emote-free-download-png-hq.png
poglimg = pygame.image.load('Assets/pogball_l.png') ##imports right pog
angle = 0

pog_x = (1920 / 2) - 30 # the ball will start in the center of the screen: the size is 60 so I have subtracted 30
pog_y = (1080 / 2) - 30

pog_m_x = 0
pog_m_y = -10

P1_pdle_x = (1920 / 2) - 80
P1_pdle_y = (7 * 1080 / 8) - 10

AI_pdle_x = (1920 / 2) - 80
AI_pdle_y = (1080 / 8) - 10

state = "paused"
player_pause_input = 0

running = 1
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:  ## makes the program mortal
           running = 0
           sys.exit()
       if event.type == pygame.KEYDOWN:
           for this in k:
               if this == event.key:
                   k[this] = 1
       if event.type == pygame.KEYUP:
           for this in k:
               if this == event.key:
                   k[this] = 0

    spin = pygame.transform.rotate(pogrimg, angle)
    screen.blit(spin, (pog_x, pog_y))
    pygame.draw.rect(screen, ((125, 125, 125)), (P1_pdle_x, P1_pdle_y, 160, 20))
    pygame.draw.rect(screen, ((125, 125, 125)), (AI_pdle_x, AI_pdle_y, 160, 20))

    if state == "paused":
        if k[sp]:
            player_pause_input = 1
        if k[sp] == 0 and player_pause_input == 1:
            state = "go"

    if state == "go":
        if k[sp]:
            player_pause_input = 1
        if k[sp] == 0 and player_pause_input == 1:
            state = "paused"

        if k[a] and P1_pdle_x >= 0:
            P1_pdle_x -= 6
        if k[d] and P1_pdle_x <= 1860:
            P1_pdle_x += 6

        pog_x += pog_m_x
        pog_y += pog_m_y



        angle += 5

    pygame.time.wait(10)
    pygame.display.flip()
    screen.fill((0, 0, 0))
