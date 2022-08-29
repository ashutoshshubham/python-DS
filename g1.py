import pgzrun

WIDTH = 500
HEIGHT = 500

box = Rect((200,200), (50,100))    #(200,200) -> coordinate or shape , (50,100) -> pixels
box2 = Rect((105,150), (50,50))


def draw():
    screen.fill('red')
    screen.draw.text('LOOOOOOOOOOOOOOOLz', (50,50), color = 'white')
    screen.draw.text('this is game programming', (50,100), color = 'yellow', fontsize = 30)
    screen.draw.rect(box, color = 'white')
    screen.draw.filled_rect(box2, color = 'black')

def update():
    box.x += 1      # 1 -> speed in pixels
    box2.y += 2     # 2 -> speed in pixels


pgzrun.go() 

