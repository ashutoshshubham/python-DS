import pgzrun

WIDTH = 1000
HEIGHT = 650


p1 = Actor('thanos',(50,100))
p2 = Actor('ironman',(950,100))
p3 = Actor('im_l')
p4 = Actor('th_l')



speed1 = 7
speed2 = 9
speed3 = 10
speed4 = 10

def draw():
    screen.fill('white')
    p1.draw()
    p2.draw()
    


def update():
    # if keyboard.W and p1.top > 0:
    #     p1.y += -speed1 
    # elif keyboard.S and p1.bottom < HEIGHT:
    #     p1.y += speed1
    # elif keyboard.A and p1.left > 0:
    #     p1.x += -speed1
    # elif keyboard.D and p1.right < WIDTH:
    #     p1.x += speed1
    # elif keyboard.UP and p2.top > 0:
    #     p2.y += -speed2
    # elif keyboard.DOWN and p2.bottom < HEIGHT:
    #     p2.y += speed2
    # elif keyboard.LEFT and  p2.left > 0:
    #     p2.x += -speed2
    # elif keyboard.RIGHT and p2.right <WIDTH:
    #     p2.x += speed2
    control_thanos()
    control_ironman()

# by defining control_ironman() and control_thanos(), we can move both characters simultaneously
# but if give control directly in update() function we cannot be able to do the above thing

def control_ironman():
    if keyboard.UP:
        p2.y += -speed2
        if p2.bottom < 0:
            p2.top = HEIGHT
    elif keyboard.DOWN:
        p2.y += speed2
        if p2.top > HEIGHT:
            p2.bottom = 0
    elif keyboard.LEFT:
        p2.x += -speed2
        if p2.right < 0:
            p2.left = WIDTH
    elif keyboard.RIGHT:
        p2.x += speed2
        if p2.left > WIDTH:
            p2.right = 0

def control_thanos():
    if keyboard.W:
        p1.y += -speed1
        if p1.bottom < 0:
            p1.top = HEIGHT 
    elif keyboard.S:
        p1.y += speed1
        if p1.top > HEIGHT:
            p1.bottom = 0
    elif keyboard.A:
        p1.x += -speed1
        if p1.right < 0:
            p1.left = WIDTH
    elif keyboard.D:
        p1.x += speed1
        if p1.left > WIDTH:
            p1.right = 0




        





pgzrun.go()