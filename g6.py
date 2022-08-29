import pgzrun
from random import randint

WIDTH = 1000
HEIGHT = 600

p = Actor('ironman',(50,200))
c = Actor('char1',(randint(0,WIDTH), randint(0,HEIGHT)))
e = Actor('thanos',(800,400))

speed = 7 
espeed = 2

score = 0      #global variable

def draw():
    screen.fill('black')
    p.draw()
    screen.draw.text(f'Score - {score}',(900,560), color = 'white', fontsize = 25)
    c.draw()
    e.draw()

def update():
    player_controls()
    check_score()
    enemy_movement()

def check_score():
    global score
    if p.colliderect(c):
        score += 5
        c.pos = (randint(0,WIDTH), randint(0,HEIGHT))
#        sounds.s1.play()     #to play sound during collision   (.wav formate)

def enemy_movement():
    if p.x > e.x:
        e.x += espeed
    if p.y > e.y:
        e.y += espeed
    if p.x < e.x:
        e.x -= espeed
    if p.y < e.y:
        e.y -= espeed
#    if p.colliderect(e):
#        p.image = 'IMAGE NAME'     #to change image of p to image with name 'IMAGE NAME'



def player_controls():                            
    
    if (keyboard.UP and not p.top < 0):
        p.y += -speed                              #speed in y direction
        p.angle = 0
    elif keyboard.DOWN and not p.bottom > HEIGHT:
        p.y += speed
        p.angle = 180
    elif keyboard.LEFT and not p.left < 0:
        p.x += -speed                                  #speed in x direction
        p.angle = 90
    elif keyboard.RIGHT and not p.right > WIDTH:
        p.x += speed
        p.angle = -90
    else:
        p.angle = 0






pgzrun.go()