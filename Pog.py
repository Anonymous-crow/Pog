import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"  ##makes that annoying help text
import pygame, sys, math, time, random
##double hash comments by jake
#single dash comments by jon
pygame.init() ##initalise pygame
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) ##creates the game window, in fullscreen mode

w = pygame.K_w; s = pygame.K_s; a = pygame.K_a; d = pygame.K_d; e = pygame.K_e; q = pygame.K_q; bk = pygame.K_BACKSPACE; sp = pygame.K_SPACE; tb = pygame.K_TAB; esc = pygame.K_ESCAPE; sh = pygame.K_LSHIFT; p = pygame.K_p ##defines a ton of variables and sets thier values to the values of certian keys in the pygame.events list
k = {w: 0, s: 0, a: 0, d: 0, e: 0, q: 0, bk: 0, sp: 0, tb: 0, esc: 0, sh: 0, p: 0} ##made a dcitonary of varibles that store keystates

pogrimg = pygame.image.load('Assets/pogball_r.png') ##imports pog right image -jake ## https://www.freepngimg.com/thumb/mouth/92712-ear-head-twitch-pogchamp-emote-free-download-png-hq.png
poglimg = pygame.image.load('Assets/pogball_l.png') ##imports left pog
angle = 0

pog_x = (1920 / 2) - 30 # the ball will start in the center of the screen: the size is 60 so I have subtracted 30
pog_y = (1080 / 2) - 30
score = 1
pog_m_x = 0  ## the slope of the pogball
pog_m_y = -4
pog_edge = 0

P1_pdle_x = (1920 / 2) - 80  ##starting position of the player 1 paddle
P1_pdle_y = (7 * 1080 / 8) - 10

AI_pdle_x = (1920 / 2) - 80  #starting position of the pogball
AI_pdle_y = (1080 / 8) - 10

state = "paused" ##sets the starting state
player_pause_input = 0 ##checks to see if game is paused or not

def text_objects(text, font, colour): ##creates text objects
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def message_display(text, position, size, colour):  ##defines messages to be typed and displayed and whatnot
    smallText = pygame.font.Font('Assets/shitty-serif.ttf',size)
    TextSurf, TextRect = text_objects(text, smallText, colour)
    TextRect.center = position
    screen.blit(TextSurf, TextRect)

def clear(): ##probably wont use this
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
clear()
running = 1  ##defines main loop condition
while running: ##main loop
    for event in pygame.event.get():## makes the program mortal
       if event.type == pygame.QUIT:
           running = 0
           sys.exit()
       if k[esc]:##if escape is pressed, exit game
           running = 0
           sys.exit()
       if event.type == pygame.KEYDOWN: ##detects keydown events in the pygame event stream
           for this in k:
               if this == event.key: ##sets key variables to 1  when key is pressed
                   k[this] = 1
       if event.type == pygame.KEYUP: ##detects keyup events in the pygame event stream
           for this in k:
               if this == event.key: ##sets key variables to 1  when key is un-pressed
                   k[this] = 0
    message_display("score:"+str(score),(100, 100),15,(255,255,255))  ##displays score
    message_display("spinnage:"+str(angle),(100, 200),15,(255,255,255))  ##displays spinnage
    spin = pygame.transform.rotate(pogrimg, angle) ##creates spinning pog image
    screen.blit(spin, (pog_x, pog_y)) ##displays pog
    pygame.draw.rect(screen, ((125, 125, 125)), (P1_pdle_x, P1_pdle_y, 160, 20)) ##draws player paddle
    pygame.draw.rect(screen, ((125, 125, 125)), (AI_pdle_x, AI_pdle_y, 160, 20)) ##draws AI paddle

    if state == "paused": ##if game is paused
        message_display(PAUSED,((1920 / 2), (1080 / 2)),200,(255,255,255))  ##display paused message
        if k[sp]:  ##if keyspace  pressed, unpause
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
        if k[d] and P1_pdle_x <= 1760:
            P1_pdle_x += 6

        pog_x += pog_m_x
        pog_y += pog_m_y

        if P1_pdle_x <= pog_x + 60 and P1_pdle_x + 160 >= pog_x and P1_pdle_y + 20 >= pog_y and P1_pdle_y <= pog_y + 60:
            pog_m_y *= -1.02
            pog_m_x = ((P1_pdle_x + 80) - (pog_x + 30)) / -20
            score += 1

        if AI_pdle_x <= pog_x + 60 and AI_pdle_x + 160 >= pog_x and AI_pdle_y + 20 >= pog_y and AI_pdle_y <= pog_y + 60:
            pog_m_y *= -1.02
            pog_m_x = ((AI_pdle_x + 80) - (pog_x + 30)) / -20

        if pog_x + 60 >= 1920 or pog_x <= 0:
            pog_edge = 1

        if pog_edge == 1:
            pog_m_x *= -1
            pog_edge = 0

        if pog_x + 30 > AI_pdle_x + 80 and :
            AI_pdle_x += 6

        if pog_x + 30 < AI_pdle_x + 80:
            AI_pdle_x -= 6

        angle += 5

    pygame.time.wait(10)
    pygame.display.flip()
    screen.fill((0, 0, 0))
