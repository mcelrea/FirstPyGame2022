import random
import pygame


#declare variables
player1 = {"x": 640,
          "y" : 360,
          "oldx": 640,
          "oldy:" : 360,
          "size": 10,
          "speed": 5,
          "color": pygame.Color(255,255,0)}

player2 = {"x": 840,
           "y" : 160,
           "oldx": 840,
           "oldy:" : 160,
           "size": 10,
           "speed": 5,
           "color": pygame.Color(0,255,0)}

map = [] #a list of rectangles

def drawMap():
    for currentRect in map:
        #draw a rectangle?
        pygame.draw.rect(screen,pygame.Color(0,255,255),currentRect)

def createMap1():
    map.append(pygame.Rect(400,200,100,250))
    map.append(pygame.Rect(300,100,10,500))
    map.append(pygame.Rect(0,0,1280,10))
    map.append(pygame.Rect(0,0,10,720))
    map.append(pygame.Rect(900,100,300,10))

def checkPlayerCollision(player):
    playerRect = getPlayerCollisionRectangle(player)

    for wall in map:
        if pygame.Rect.colliderect(playerRect,wall):
            # reverse the move back to their previous position
            player["x"] = player["oldx"]
            player["y"] = player["oldy"]
            player["color"] = (random.randint(0, 255),
                                random.randint(0,255),
                                random.randint(0,255))


def getPlayerCollisionRectangle(player):
    return pygame.Rect(player["x"] - player["size"], player["y"] - player["size"], player["size"] * 2, player["size"] * 2)

def drawPlayerCollisionBox(player):
    pygame.draw.rect(screen, pygame.Color(255,0,255), getPlayerCollisionRectangle(player), 1)

def clearScreen():
    pygame.draw.rect(screen, pygame.Color(0,0,0), (0,0,1280,720))

def drawPlayers():
    pygame.draw.circle(screen, player1["color"], (player1["x"], player1["y"]), player1["size"])
    pygame.draw.circle(screen, player2["color"], (player2["x"], player2["y"]), player2["size"])

def playerMovement():
    keys = pygame.key.get_pressed()

    #remember where the player was BEFORE movement
    player1["oldx"] = player1["x"]
    player1["oldy"] = player1["y"]
    player2["oldx"] = player2["x"]
    player2["oldy"] = player2["y"]

    #player 1 keys
    if keys[pygame.K_d]:
        player1["x"] += player1["speed"]
    if keys[pygame.K_w]:
        player1["y"] -= player1["speed"]
    if keys[pygame.K_s]:
        player1["y"] += player1["speed"]
    if keys[pygame.K_a]:
        player1["x"] -= player1["speed"]

    #player 2 keys
    if keys[pygame.K_RIGHT]:
        player2["x"] += player2["speed"]
    if keys[pygame.K_UP]:
        player2["y"] -= player2["speed"]
    if keys[pygame.K_DOWN]:
        player2["y"] += player2["speed"]
    if keys[pygame.K_LEFT]:
        player2["x"] -= player2["speed"]

#start of the program
pygame.init() #start the pygame engine
FPS = 60 #keep game at 60 FPS
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))
gameOver = False
createMap1()

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
    checkPlayerCollision(player1)
    checkPlayerCollision(player2)

    #draw code
    clearScreen()
    drawMap()
    drawPlayers()
    drawPlayerCollisionBox(player1)
    drawPlayerCollisionBox(player2)

    #put all the graphics on the screen
    #should be the LAST LINE of game code
    pygame.display.flip()
    fpsClock.tick(FPS) #slow the game down to 60 loops a second