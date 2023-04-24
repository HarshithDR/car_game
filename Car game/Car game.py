import pygame
import time
import random
import sys

pygame.init()

gray = (126, 126, 126)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (139, 0, 0)
bright_red = (255, 0, 0)
blue = (0, 0, 200)
bright_blue = (0, 0, 255)
green = (0, 200, 0)
bright_green = (0, 255, 0)
display_width = 800
display_height = 600
gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Car Game')
clock = pygame.time.Clock()
car_img = pygame.image.load('mycar1.png')
car_width = 50
background_pic = pygame.image.load('download12.jpg')
yellow_strip = pygame.image.load('yellow strip.jpg')
strip = pygame.image.load('strip.jpg')
intro_background = pygame.image.load('background.jpg')
instruction_background = pygame.image.load('background2.jpg')
pause = False

def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(intro_background, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("CAR GAME", largetext)
        TextRect.center = (400, 100)
        gamedisplays.blit(TextSurf, TextRect)
        button("START", 150, 520, 100, 50, green, bright_green, "play")
        button("QUIT", 550, 520, 100, 50, red, bright_red, "quit")
        button("INSTRUCTION", 300, 520, 200, 50, blue, bright_blue, "intro")
        pygame.display.update()
        clock.tick(50)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gamedisplays, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                countdown()
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action == "intro":
                introduction()
            elif action == "menu":
                intro_loop()
            elif action == "pause":
                paused()
            elif action == "unpause":
                unpaused()


    else:
        pygame.draw.rect(gamedisplays, ic, (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = ((x + (w / 2)), (y + (h / 2)))
    gamedisplays.blit(textsurf, textrect)


def introduction():
    introduction = True
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 80)
        smalltext = pygame.font.Font('freesansbold.ttf', 20)
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)
        textSurf, textRect = text_objects("This is an car game in which you need dodge the coming cars", smalltext)
        textRect.center = ((350), (200))
        TextSurf, TextRect = text_objects("INSTRUCTION", largetext)
        TextRect.center = ((400), (100))
        gamedisplays.blit(TextSurf, TextRect)
        gamedisplays.blit(textSurf, textRect)
        stextSurf, stextRect = text_objects("ARROW LEFT : LEFT TURN", smalltext)
        stextRect.center = ((150), (400))
        hTextSurf, hTextRect = text_objects("ARROW RIGHT : RIGHT TURN", smalltext)
        hTextRect.center = ((150), (450))
        atextSurf, atextRect = text_objects("A : ACCELERATOR", smalltext)
        atextRect.center = ((150), (500))
        rtextSurf, rtextRect = text_objects("B : BRAKE ", smalltext)
        rtextRect.center = ((150), (550))
        ptextSurf, ptextRect = text_objects("ESC : PAUSE  ", smalltext)
        ptextRect.center = ((150), (350))
        sTextSurf, sTextRect = text_objects("CONTROLS", mediumtext)
        sTextRect.center = ((350), (300))
        gamedisplays.blit(sTextSurf, sTextRect)
        gamedisplays.blit(stextSurf, stextRect)
        gamedisplays.blit(hTextSurf, hTextRect)
        gamedisplays.blit(atextSurf, atextRect)
        gamedisplays.blit(rtextSurf, rtextRect)
        gamedisplays.blit(ptextSurf, ptextRect)
        button("BACK", 600, 450, 100, 50, blue, bright_blue, "menu")
        pygame.display.update()
        clock.tick(30)


def paused():
    global pause
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        textsurf, textrect = text_objects('PAUSED', largetext)
        textrect.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(textsurf, textrect)
        button('CONTINUE', 150, 450, 150, 50, green, bright_green, 'unpause')
        button('RESTART', 350, 450, 150, 50, blue, bright_blue, 'play')
        button('MAIN MENU', 550, 450, 200, 50, red, bright_red, 'menu')
        pygame.display.update()
        clock.tick(30)


def unpaused():
    global pause
    pause = False


def countdown_background():
    font = pygame.font.SysFont(None, 25)
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    gamedisplays.blit(background_pic, (0, 0))
    gamedisplays.blit(background_pic, (0, 200))
    gamedisplays.blit(background_pic, (0, 400))
    gamedisplays.blit(background_pic, (700, 0))
    gamedisplays.blit(background_pic, (700, 200))
    gamedisplays.blit(background_pic, (700, 400))
    gamedisplays.blit(yellow_strip, (400, 100))
    gamedisplays.blit(yellow_strip, (400, 200))
    gamedisplays.blit(yellow_strip, (400, 300))
    gamedisplays.blit(yellow_strip, (400, 400))
    gamedisplays.blit(yellow_strip, (400, 100))
    gamedisplays.blit(yellow_strip, (400, 500))
    gamedisplays.blit(yellow_strip, (400, 0))
    gamedisplays.blit(yellow_strip, (400, 600))
    gamedisplays.blit(strip, (120, 200))
    gamedisplays.blit(strip, (120, 0))
    gamedisplays.blit(strip, (120, 100))
    gamedisplays.blit(strip, (680, 100))
    gamedisplays.blit(strip, (680, 0))
    gamedisplays.blit(strip, (680, 200))
    gamedisplays.blit(car_img, (x, y))
    text = font.render("DODGED: 0", True, black)
    score = font.render("SCORE: 0", True, red)
    gamedisplays.blit(text, (0, 50))
    gamedisplays.blit(score, (0, 30))
    button("PAUSE", 650, 0, 150, 50, blue, bright_blue, "pause")


def countdown():
    countdown = True
    countdown_number = 3
    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        while countdown_number >= 1:
            gamedisplays.fill(gray)
            countdown_background()
            largetext = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = text_objects(str(countdown_number), largetext)
            TextRect.center = ((display_width / 2), (display_height / 2))
            gamedisplays.blit(TextSurf, TextRect)
            countdown_number -= 1
            pygame.display.update()
            clock.tick(1)
        gamedisplays.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("GO!!!", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        game_loop()


def score_system(dodged, score, level):
    font = pygame.font.SysFont(None, 25)
    text = font.render('DODGED ' + str(dodged), True, black)
    score = font.render('SCORE ' + str(score), True, red)
    level = font.render('LEVEL ' + str(level), True, yellow)
    gamedisplays.blit(text, (0, 50))
    gamedisplays.blit(score, (0, 30))
    gamedisplays.blit(level, (0, 10))


def obstacle(obs_startx, obs_starty, obs):
    obs_pic = pygame.image.load('car' + str(obs) + '.jpg')
    gamedisplays.blit(obs_pic, (obs_startx, obs_starty))


def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf', 80)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((display_width / 2), (display_height / 2))
    gamedisplays.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    message_display('YOU CRASHED')


def background():
    gamedisplays.blit(background_pic, (0, 0))
    gamedisplays.blit(background_pic, (0, 200))
    gamedisplays.blit(background_pic, (0, 400))
    gamedisplays.blit(background_pic, (697, 0))
    gamedisplays.blit(background_pic, (697, 200))
    gamedisplays.blit(background_pic, (697, 400))
    gamedisplays.blit(strip, (120, 0))
    gamedisplays.blit(strip, (120, 200))
    gamedisplays.blit(strip, (120, 400))
    gamedisplays.blit(strip, (673, 0))
    gamedisplays.blit(strip, (673, 200))
    gamedisplays.blit(strip, (673, 400))
    gamedisplays.blit(yellow_strip, (380, 0))
    gamedisplays.blit(yellow_strip, (380, 100))
    gamedisplays.blit(yellow_strip, (380, 200))
    gamedisplays.blit(yellow_strip, (380, 300))
    gamedisplays.blit(yellow_strip, (380, 400))
    gamedisplays.blit(yellow_strip, (380, 500))


def car(x, y):
    gamedisplays.blit(car_img, (x, y))


def game_loop():
    global pause
    x = (display_width * 0.475)
    y = (display_height * 0.83)
    x_change = 0
    obstacle_speed = 5
    obs = random.randrange(1, 6)
    obs_startx = random.randrange(120, (display_width - 130))
    obs_starty = -750
    obs_width = 50
    obs_height = 115
    dodged = 0
    level = 0
    score = 0
    y2 = 7

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Keys control
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_a:
                    obstacle_speed += 2
                if event.key == pygame.K_b:
                    obstacle_speed -= 2
                if event.key == pygame.K_ESCAPE:
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        pause = True

        gamedisplays.fill(gray)

        rel_y = y2 % background_pic.get_rect().width
        gamedisplays.blit(background_pic, (0, rel_y - background_pic.get_rect().width))
        gamedisplays.blit(background_pic, (697, rel_y - background_pic.get_rect().width))
        if rel_y < 800:
            gamedisplays.blit(background_pic, (0, rel_y))
            gamedisplays.blit(background_pic, (697, rel_y))
            gamedisplays.blit(yellow_strip, (380, rel_y))
            gamedisplays.blit(yellow_strip, (380, rel_y + 100))
            gamedisplays.blit(yellow_strip, (380, rel_y + 200))
            gamedisplays.blit(yellow_strip, (380, rel_y + 300))
            gamedisplays.blit(yellow_strip, (380, rel_y + 400))
            gamedisplays.blit(yellow_strip, (380, rel_y + 500))
            gamedisplays.blit(yellow_strip, (380, rel_y - 100))
            gamedisplays.blit(strip, (120, rel_y - 200))
            gamedisplays.blit(strip, (120, rel_y + 20))
            gamedisplays.blit(strip, (120, rel_y + 30))
            gamedisplays.blit(strip, (673, rel_y - 100))
            gamedisplays.blit(strip, (673, rel_y + 20))
            gamedisplays.blit(strip, (673, rel_y + 30))

        y2 += obstacle_speed

        obs_starty -= (obstacle_speed / 4)
        obstacle(obs_startx, obs_starty, obs)
        obs_starty += obstacle_speed

        car(x, y)

        score_system(dodged, score, level)

        if x > 673 - car_width or x < 120:
            crash()
        if x > display_width - (car_width + 120) or x < 120:
            crash()

        if obs_starty > display_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(130, (display_width - 300))
            obs = random.randrange(1, 6)
            dodged += 1
            score = dodged * 10
            if int(dodged) % 10 == 0:
                level += 1
                obstacle_speed + 2
                largetext = pygame.font.Font('freesansbold.ttf', 80)
                textsurf, textrect = text_objects('LEVEL ' + str(level), largetext)
                textrect.center = ((display_width / 2), (display_height / 2))
                gamedisplays.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        if y < obs_starty + obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x + car_width > obs_startx and x + car_width < obs_startx + obs_width:
                crash()
        button('Pause', 650, 0, 150, 50, blue, bright_blue, 'pause')
        pygame.display.update()
        clock.tick(150)

intro_loop()
game_loop()
pygame.quit()
quit()
