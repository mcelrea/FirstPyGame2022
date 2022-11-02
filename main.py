import random
import pygame


#declare variables
player1 = {"x": 640,
          "y" : 360,
          "oldx": 640,
          "oldy:" : 360,
          "size": 10,
          "speed": 5,
          "color": pygame.Color(255,255,0),
          "lastDir" : "right"}

player2 = {"x": 840,
           "y" : 160,
           "oldx": 840,
           "oldy:" : 160,
           "size": 10,
           "speed": 5,
           "color": pygame.Color(0,255,0),
           "lastDir": "right"}

map = [] #a list of rectangles
bullets = [] #a list of bullets in the game
"""
bullets[0] -> x
bullets[1] -> y
bullets[2] -> size
bullets[3] -> player who shot bullet
bullets[4] -> color
bullets[5] -> x-velocity
bullets[6] -> y-velocity
"""

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

def drawBullets():
    for b in bullets:
        pygame.draw.circle(screen,b[4],(b[0],b[1]),b[2])

def updateBullets():
    """
    this stupid function does not work! :(
    I cannot change the values in a tuple, which is how I am
    storing each bullet

    I need to re-think how to store a bullet, so that I can change it,
    so it can move, change colors, sizes, and all kinds of exciting things
    :return:
    """
    for b in bullets:
        b[0] = (b[0] + b[5]) # x += x-velocity
        b[1] = (b[1] + b[6]) # y += y-velocity

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
        player1["lastDir"] = "right"
    if keys[pygame.K_w]:
        player1["y"] -= player1["speed"]
        player1["lastDir"] = "up"
    if keys[pygame.K_s]:
        player1["y"] += player1["speed"]
        player1["lastDir"] = "down"
    if keys[pygame.K_a]:
        player1["x"] -= player1["speed"]
        player1["lastDir"] = "left"
    if keys[pygame.K_f]:
        if player1["lastDir"] == "right":
            bullets.append((player1["x"], player1["y"],5,"p1",player1["color"],20,0))
        elif player1["lastDir"] == "left":
            bullets.append((player1["x"], player1["y"],5,"p1",player1["color"],-20,0))
        elif player1["lastDir"] == "up":
            bullets.append((player1["x"], player1["y"],5,"p1",player1["color"],0,20))
        elif player1["lastDir"] == "down":
            bullets.append((player1["x"], player1["y"],5,"p1",player1["color"],0,-20))



    #player 2 keys
    if keys[pygame.K_RIGHT]:
        player2["x"] += player2["speed"]
        player2["lastDir"] = "right"
    if keys[pygame.K_UP]:
        player2["y"] -= player2["speed"]
        player2["lastDir"] = "up"
    if keys[pygame.K_DOWN]:
        player2["y"] += player2["speed"]
        player2["lastDir"] = "down"
    if keys[pygame.K_LEFT]:
        player2["x"] -= player2["speed"]
        player2["lastDir"] = "left"

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
    updateBullets()
    checkPlayerCollision(player1)
    checkPlayerCollision(player2)

    #draw code
    clearScreen()
    drawMap()
    drawBullets()
    drawPlayers()
    drawPlayerCollisionBox(player1)
    drawPlayerCollisionBox(player2)

    #put all the graphics on the screen
    #should be the LAST LINE of game code
    pygame.display.flip()
    fpsClock.tick(FPS) #slow the game down to 60 loops a second