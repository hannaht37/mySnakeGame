"WARNING! WITHOUT PYGAME, THIS GAME WILL NOT WORK!"

import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (109, 255, 136)
blue = (0, 153, 204)
b2 = (155, 206, 209)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Sea Snake Sisters")

icon = pygame.image.load("fishyboi.png")
pygame.display.set_icon(icon)

#2. I changed the image of the apple to a fish to fit the underwater theme and it changes colors too.
# To achieve my code, I used paint and list functions.
img = pygame.image.load("seaboi.png")
img2 = pygame.image.load("fishyboi.png")
img3 = pygame.image.load("fishyboi1.png")
img4 = pygame.image.load("fishyboi2.png")
img5 = pygame.image.load("fishyboi3.png")
bgimg = pygame.image.load("water.png")
harm = pygame.image.load("trashyboi.png")
clock = pygame.time.Clock()

fishcolors = [img2, img3, img4, img5]
FishThicc = 30
block_size =  20
FPS = 15
PlasThicc = 30

direction = "right"

# different fonts
gameoverfont = pygame.font.SysFont("chiller", 80)
smolfont = pygame.font.SysFont("centurygothic", 25)
medfont = pygame.font.SysFont("centurygothic", 50)
largefont = pygame.font.SysFont("centurygothic", 80)

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                    
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                    
        gameDisplay.fill(white)
        message_to_screen("Paused!", black, -100, size="large")
        message_to_screen("Press C to Continue or Q to Quit. ", black, 25 , size="medium")
        pygame.display.update()
        clock.tick(5)

# function to keep track of the score
def score(score):
    text = smolfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0,0])
    
def randFishGen():
    randFishx = round(random.randrange(0, display_width-FishThicc))#/10.0)*10.0 
    randFishy = round(random.randrange(0, display_height-FishThicc))#/10.0)*10.0
    return randFishx, randFishy

#4 BEWARE! As people around the earth litter the oceans, underwater sea creatures are prone to the damage. Running into the plastic will kill you.
# The code I used was from inspiration from the tutorial from the NewBoston and also trial and error.
def randTrashGen():
    randtrashx = round(random.randrange(0, display_width-PlasThicc))#/10.0)*10.0 
    randtrashy = round(random.randrange(0, display_height-PlasThicc))#/10.0)*10.0
    return randtrashx, randtrashy

def gameintro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(b2)
        message_to_screen("Welcome to Sea Snake Sisters!", blue, -100, size = "medium")
        message_to_screen("The objective of the game is to eat fish.", black, -30)
        message_to_screen("The more fish you eat, the longer you get.", black, 10)
        message_to_screen("Use the error keys to move.", black, 40)
        message_to_screen("If you run into yourself, the edges,or the plastic, you die.", black, 70)
        message_to_screen("Press P to play, P to Pause a second time, or Q to Quit", black, 180)

        pygame.display.update()
        clock.tick(15)

# function to define the different text sizes/fonts
def text_obj(text, color, size):
    if size == "small":
        textSurface = smolfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    elif size == "scary":
        textSurface = gameoverfont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size = "small"):
    textSurf, textRect = text_obj(msg, color, size)
    textRect.center = (display_width/2), (display_height/2)+ y_displace
    gameDisplay.blit(textSurf, textRect)

def snake(block_size, snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
        
    gameDisplay.blit(head,(snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        #3. I modified the rectangles into circles. It took some trial and error,
        #and a bit of help from pygame's website.
        pygame.draw.circle(gameDisplay, black,[int(XnY[0] + 10), int(XnY[1] + 10)] , 10, 0)

def gameLoop():
    global direction
    direction = "right"
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    
    lead_x_change = 10
    lead_y_change = 0

    snakelist = []
    snakelength = 1

    randFishx, randFishy = randFishGen()
    randtrashx, randtrashy = randTrashGen()
    
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over!", red, y_displace = -50, size = "scary")
            #5 I added a ending score to the quit screen. I used my function; no inspiration or code and error needed.
            message_to_screen("You Ate: " + str(snakelength - 1) + " fish. Yum!", blue, 0, size = "medium")
            message_to_screen("Press P to play again or Q to quit", black, 100, size = "medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_p:
                        gameLoop()

        # directions for the snake!!!!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()
                    
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y <0:
                gameOver = True
        
        lead_x += lead_x_change
        lead_y += lead_y_change
        
#1. Instead of using GameDisplay.fill() for the background, I decided to not only use a different function, but a completely different image. The code was found by
#   just trial and error.
        gameDisplay.blit(bgimg, [0,0])

        gameDisplay.blit(random.choice(fishcolors), [randFishx, randFishy])
        gameDisplay.blit(harm, [randtrashx, randtrashy])
        
        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        yay = 1

        if len(snakelist) > snakelength:
            del snakelist[0]

        for eachSegment in snakelist[:-1]:
            if eachSegment == snakehead:
                gameOver = True
                
        snake(block_size, snakelist)

        score(snakelength-1)
        
        pygame.display.update()

        if lead_x > randFishx and lead_x < randFishx + FishThicc or lead_x + block_size > randFishx and lead_x + block_size < randFishx + FishThicc:

            if lead_y > randFishy and lead_y < randFishy + FishThicc:
                
                randFishx, randFishy = randFishGen()
                snakelength += 1
                randtrashx, randtrashy = randTrashGen()


            elif lead_y + block_size > randFishy and lead_y + block_size < randFishy + FishThicc:

                randFishx, randFishy = randFishGen()
                snakelength += 1
                randtrashx, randtrashy = randTrashGen()
    
        if lead_x > randtrashx and lead_x < randtrashx + PlasThicc or lead_x + block_size > randtrashx and lead_x + block_size < randtrashx + PlasThicc:

            if lead_y > randtrashy and lead_y < randtrashy + PlasThicc:
                
                gameOver = True

            elif lead_y + block_size > randtrashy and lead_y + block_size < randtrashy + PlasThicc:

                gameOver = True

        clock.tick(FPS)

    pygame.quit()
    quit()
gameintro()
gameLoop()





