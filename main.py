import random
import pygame
import time


#declare variables
player1 = {"x": 640,
          "y" : 360,
          "oldx": 640,
          "oldy:" : 360,
          "size": 10,
          "speed": 5,
          "color": pygame.Color(255,0,0),
          "lastDir": "right",
          "shotTimeStamp": 0,
          "nextShot": 0,
          "score": 0}

player2 = {"x": 840,
           "y" : 160,
           "oldx": 840,
           "oldy:" : 160,
           "size": 10,
           "speed": 5,
           "color": pygame.Color(0,255,0),
           "lastDir": "right",
           "shotTimeStamp": 0,
           "nextShot": 0,
           "score": 0}

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
            #player["color"] = (random.randint(0, 255),
            #                    random.randint(0,255),
            #                    random.randint(0,255))


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
        pygame.draw.circle(screen, b["color"], (b["x"], b["y"]), b["size"])

def newRound():
    #remove all the bullets
    bullets.clear()

    #reset the player locations
    player1["x"] = 100;
    player1["y"] = 100;
    player2["x"] = 900;
    player2["y"] = 600;

def updateBullets():
    for b in bullets:
        #move the bullet
        b["x"] += b["xvel"]
        b["y"] += b["yvel"]

        #if bullet is off screen remove it
        if isOffScreen(b["x"], b["y"]):
            bullets.remove(b) #kill this bullet

        #check if the bullet is hitting a player
        player1Rect = getPlayerCollisionRectangle(player1)
        player2Rect = getPlayerCollisionRectangle(player2)
        bulletRect = pygame.Rect(b["x"] - b["size"], b["y"] - b["size"], b["size"] * 2, b["size"] * 2)
        if pygame.Rect.colliderect(bulletRect, player1Rect) and b["owner"] == "p2":
            player2["score"] += 1
            newRound()
        elif pygame.Rect.colliderect(bulletRect, player2Rect) and b["owner"] == "p1":
            player1["score"] += 1
            newRound()

        #check this bullet for collision with every wall
        for wall in map:
            bulletRect = pygame.Rect(b["x"] - b["size"], b["y"] - b["size"], b["size"] * 2, b["size"] * 2)
            if pygame.Rect.colliderect(wall, bulletRect):
                b["xvel"] *= -1
                b["yvel"] *= -1

def isOffScreen(x, y):
    if x < 0 or x > 1280 or y < 0 or y > 720:
        return True
    else:
        return False

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
    if keys[pygame.K_f] and player1["nextShot"] < time.time_ns():
        if player1["lastDir"] == "right":
            bullets.append({"x": player1["x"],
                            "y": player1["y"],
                            "size": 5,
                            "owner": "p1",
                            "color": player1["color"],
                            "xvel": 20,
                            "yvel": 0})
            #I think 1000 ns is equals to 1 second
            player1["nextShot"] = time.time_ns() + 1_000_000_000;
        elif player1["lastDir"] == "left":
            bullets.append({"x": player1["x"],
                            "y": player1["y"],
                            "size": 5,
                            "owner": "p1",
                            "color": player1["color"],
                            "xvel": -20,
                            "yvel": 0})
            player1["nextShot"] = time.time_ns() + 1_000_000_000;
        elif player1["lastDir"] == "up":
            bullets.append({"x": player1["x"],
                            "y": player1["y"],
                            "size": 5,
                            "owner": "p1",
                            "color": player1["color"],
                            "xvel": 0,
                            "yvel": -20})
            player1["nextShot"] = time.time_ns() + 1_000_000_000;
        elif player1["lastDir"] == "down":
            bullets.append({"x": player1["x"],
                            "y": player1["y"],
                            "size": 5,
                            "owner": "p1",
                            "color": player1["color"],
                            "xvel": 0,
                            "yvel": 20})
            player1["nextShot"] = time.time_ns() + 1_000_000_000;



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
    if keys[pygame.K_m] and player2["nextShot"] < time.time_ns():
        if player2["lastDir"] == "right":
            bullets.append({"x": player2["x"],
                            "y": player2["y"],
                            "size": 5,
                            "owner": "p2",
                            "color": player2["color"],
                            "xvel": 20,
                            "yvel": 0})
            #I think 1000 ns is equals to 1 second
            player2["nextShot"] = time.time_ns() + 1_000_000_000;
        elif player2["lastDir"] == "left":
            bullets.append({"x": player2["x"],
                            "y": player2["y"],
                            "size": 5,
                            "owner": "p2",
                            "color": player2["color"],
                            "xvel": -20,
                            "yvel": 0})
            player2["nextShot"] = time.time_ns() + 1_000_000_000;
        elif player2["lastDir"] == "up":
            bullets.append({"x": player2["x"],
                            "y": player2["y"],
                            "size": 5,
                            "owner": "p2",
                            "color": player2["color"],
                            "xvel": 0,
                            "yvel": -20})
            player2["nextShot"] = time.time_ns() + 1_000_000_000;
        elif player2["lastDir"] == "down":
            bullets.append({"x": player2["x"],
                            "y": player2["y"],
                            "size": 5,
                            "owner": "p2",
                            "color": player2["color"],
                            "xvel": 0,
                            "yvel": 20})
            player2["nextShot"] = time.time_ns() + 1_000_000_000;

# HUD - Heads Up Display
def drawHUD():
    textSurface = timesFont.render("Player 1 Score: " + str(player1["score"]), True, (255,255,255))
    screen.blit(textSurface, (50, 30))
    textSurface = timesFont.render("Player 2 Score: " + str(player2["score"]), True, (255,255,255))
    screen.blit(textSurface, (1050, 30))

#start of the program
pygame.init() #start the pygame engine
pygame.font.init() #start the font engine
timesFont = pygame.font.SysFont('Times New Roman', 23) #load a font for use
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
    drawHUD()

    #put all the graphics on the screen
    #should be the LAST LINE of game code
    pygame.display.flip()
    fpsClock.tick(FPS) #slow the game down to 60 loops a second