# Write your code here :-)
import random
from time import *
WIDTH =600
HEIGHT=800
length = 150

ball = Rect(WIDTH/2, HEIGHT/2, 15, 15)
bat = Rect(WIDTH/2, 750, length, 10)
bricks = []
BRICKX = 10
BRICKY = 5
for x in range(0, BRICKX):
    for y in range(0, BRICKY):
        brick = Rect(x*55 + 25,y*25, 50, 20)
        bricks.append(brick)
score = 0
lives = 6
xvel = 5
yvel = 5
state = "paused"
colours2 = ["brown", "green", "red", "blue", "white", "gray", "yellow", "orange", "purple", "black", "pink"]
colours = ["white", "black", "black", "black", "black"]
def draw():
    global state
    global lives
    if state == "playing":
        screen.clear()
        for brick in bricks:
            screen.draw.filled_rect(brick, random.choice(colours))
        screen.draw.text("Lives: " + str(lives), (10, 10), color="red")
        screen.draw.text("Score: " + str(score), (10, 30), color="red")
        screen.draw.filled_circle(ball.center, 10, random.choice(colours2))
        screen.draw.filled_rect(bat, "red")
        if keyboard[keys.SPACE] and lives > 0 and state != "paused":
            state = "playing"
        if keyboard[keys.P] and state == "playing":
            state = "paused"
    elif state == "gamover":
        screen.draw.text("Lives: " + str(lives), (10, 10), color="red")
        screen.draw.text("GAME OVER!", (200, 150), color = "red")
        screen.draw.text("Score: " + str(score), (10, 30), color="red")
    elif state == "paused":
        screen.draw.text("Paused", (150, 150), color = "yellow")
        screen.draw.text("Lives: " + str(lives), (10, 10), color="red")
        screen.draw.text("Score: " + str(score), (10, 30), color="red")
        if keyboard[keys.O] and state == "paused":
            state = "playing"



def update():
    global xvel
    global yvel
    global lives
    global state
    global score
    global colours
    global bat
    global length
    if state == "playing":
        ball.x = ball.x + xvel
        ball.y = ball.y + yvel
        if ball.right > WIDTH:
            xvel = xvel * -1
            xvel += random.uniform(-1, 1)
        if ball.bottom > HEIGHT:
            ball.x = WIDTH / 2
            ball.y = HEIGHT/2
            lives -= 1
            yvel = random.uniform(-7, -5)
            xvel = random.uniform(7, 5)
        if ball.left < 0:
            xvel = xvel * -1
            xvel += random.uniform(-1, 1)
        if ball.top < 0:
            yvel = yvel * -1
            yvel += random.uniform(-1, 1)
        if keyboard[keys.D] and bat.right <600:
            bat.x = bat.x + 10
        elif keyboard[keys.A] and bat.left > 0:
            bat.x = bat.x - 10
        if keyboard[keys.L]:
            colours = ["white"]
        if bat.colliderect(ball) and yvel > 0:
            yvel = yvel * -1
            if yvel <= 12 and yvel >= -12:
                yvel = yvel * 1.05
            if xvel <= 12 and xvel >= -12:
                xvel = xvel * 1.05
            if random.randint(0, 15) == 1:
                lives += 1
            yvel += random.uniform(-1, 1)
        for brick in bricks:
            if brick.colliderect(ball):
                if (brick.x + 24 < ball.x and ball.y < brick.y + 19 and ball.y > brick.y - 19) or (brick.x - 24 > ball.x and ball.y < brick.y + 19 and ball.y > brick.y - 19):
                    xvel = xvel * -1
                yvel = yvel * -1
                score += 10
                bricks.remove(brick)
                yvel += random.uniform(-1, 1)
        if lives == 0:
            state = "gameover"
        if len(bricks) == 0:
            lives += 2
            yvel = random.uniform(-6, -4.5)
            xvel = random.uniform(6, -6)
            if xvel <= 2 and xvel >= -2:
                xvel *= 2
            ball.x = WIDTH/2
            ball.y = HEIGHT/2
            if length > 60:
                length -= 30
                bat = Rect(bat.x, bat.y, length, 10)
            for x in range(0, BRICKX):
                for y in range(0, BRICKY):
                    brick = Rect(x*55 + 25,y*25, 50, 20)
                    bricks.append(brick)
