import pgzrun
import pygame
import random


WIDTH = 600
HEIGHT = 800

# paddle = pygame.image.load('p_p.jpg')
# paddle = Actor('p_p.jpg')
# paddle.x = 350
# paddle.y = 370

# rewrite with class

# ball = Actor('r_b.png')
# ball.x = 260
# ball.y = 260

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.color = RED

    def update(self):
        global ball
        global ball_x, ball_y
        if ball_x == 'left':
            ball.x -= velx
            if ball.x < 10:
                ball_x = 'right'
        if ball_y == 'down':
            ball.y += vel_y
        if ball_y == 'up':
            ball.y -= vel_y
            if ball.y < 30:
                ball_y = 'down'
        if ball_x == 'right':
            ball.x += velx
            if ball.x > 490:
                ball_x == 'left'

        gfxdraw.filled_circle(screen, ball.x, ball.y, 6, self.color)
        self.rect = pygame.Rect(self.x, self.y, 6, 6)

class Brick:
    def __init__(self, x, y, randomcolor):
        self.x = x
        self.y = y
        # self.color = randomcolor
        # self.rect = pygame.Rect(self.x, self.y, 50, 20)

    def update(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 20))


# paddle = pygame.image.load('p_p.jpg')
# paddle = Actor('p_p.jpg')
# paddle.x = 350
# paddle.y = 370

class paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 60
    def update(self):
        paddle = pygame.image.load('p_p.jpg')
        # pygame.draw.rect(screen, RED, (self.x, self.y, self.size, 10))
        self.rect = pygame.Rect(self.x, self.y, self.size, 10)






ball_x_speed = -3
ball_y_speed = -3

bars_list = []

def draw():
    surface = pygame.display.set_mode((WIDTH, HEIGHT))


    color = (0, 100, 100)
    surface.fill(color)
    pygame.display.flip()
    paddle.draw()
    ball.draw()
    for bar in bars_list:
        bar.draw()

def place_bars(x,y,image):
    bar_x = x
    bar_y = y
    for i in range(8):
        bar = Actor(image)
        bar.x = bar_x
        bar.y = bar_y
        bar_x += 70
        bars_list.append(bar)



def update(dt):
    global ball_x_speed, ball_y_speed
    if keyboard.left:             #rewrite using mouse
        paddle.x = paddle.x - 5
    if keyboard.right:
        paddle.x = paddle.x + 5

    update_ball()
    for bar in bars_list:
        if ball.colliderect(bar):
            bars_list.remove(bar)
            ball_y_speed *= -1

    if paddle.colliderect(ball):
        ball_y_speed *= -1
        rand = random.randint(0,1)
        if rand:
            ball_x_speed *= -1

def update_ball():
    global ball_x_speed, ball_y_speed
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    if (ball.x >= WIDTH) or (ball.x <=0):
        ball_x_speed *= -1
    if (ball.y >= HEIGHT) or (ball.y <=0):
        ball_y_speed *= -1
    if ball.y > HEIGHT:
        pass
        #lives counter func
def lives():
    pass



coloured_box_list = ["r_g.jpg", "r_o.jpg","r_p.jpg"]
x = 50
y = 100
for coloured_box in coloured_box_list:
    place_bars(x, y, coloured_box)
    y += 50

