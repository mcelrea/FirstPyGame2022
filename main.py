import pygame


#declare variables
player = {"x": 640,
          "y" : 360,
          "size": 10,
          "speed": 5,
          "color": pygame.Color(255,255,0)}

def clearScreen():
    pygame.draw.rect(screen, pygame.Color(0,0,0), (0,0,1280,720))

def drawPlayer():
    pygame.draw.circle(screen, player["color"], (player["x"],player["y"]), player["size"])

def playerMovement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player["x"] += player["speed"]
    if keys[pygame.K_w]:
        player["y"] -= player["speed"]
    if keys[pygame.K_s]:
        player["y"] += player["speed"]
    if keys[pygame.K_a]:
        player["x"] -= player["speed"]

#start of the program
pygame.init() #start the pygame engine
FPS = 60 #keep game at 60 FPS
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))
gameOver = False

while(not gameOver):
    #loop through and empty the event queue, key presses
    #buttons, clicks, etc.
    for event in pygame.event.get():
        #if the event is a click on the "x" close button
        if event.type == pygame.QUIT:
            gameOver = True

    #player input
    playerMovement()

    #ai

    #draw code
    clearScreen()
    drawPlayer()

    #put all the graphics on the screen
    #should be the LAST LINE of game code
    pygame.display.flip()
    fpsClock.tick(FPS) #slow the game down to 60 loops a second