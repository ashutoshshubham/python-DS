# https://kenney.nl/
# https://electronstudio.github.io/pygame-zero-book/



import random
import pgzrun

WIDTH = 600
HEIGHT = 800
MAX_BULLETS = 8

level = 0
lives = 3
score = 0

if_started = False
game_over = False
game_start = True
win_over = False

background1 = Actor('background1')
background2 = Actor('background2')
background3 = Actor('background3')
player = Actor('player',(200,500))
enemies = []
bullets = []
bombs = []

def draw():
    if game_start:
        if_game_start()
    if if_started:
        started()
    if game_over:
        if_game_over()
    if win_over:
        if_win_over()

def update():
    global if_started
    global win_over
    if keyboard.space:
        if_started = True
    move_player()
    move_bullets()
    move_enemies()
    create_bombs()
    move_bombs()
    check_for_end_of_level()

def create_enemies():
    for x in range(0, 600, 60):
        for y in range(0, 200, 60):
            enemy = Actor('enemy',(x, y))
            enemy.vx = level * 2
            enemies.append(enemy)

def move_player():
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5
    if player.right > WIDTH:
        player.right = WIDTH
    if player.left < 0:
        player.left = 0
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
    if player.y < 500:
        player.y = 500

def move_enemies(): 
    global score
    global game_over
    global lives
    for enemy in enemies:
        enemy.x = enemy.x + enemy.vx
        if enemy.x > WIDTH or enemy.x < 0:
            enemy.vx = -enemy.vx
            animate(enemy, duration = 0.1, y = enemy.y + 60)
        for bullet in bullets:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 1
        if enemy.colliderect(player):
            lives -= 1
            if lives == 0:
                game_over = True

def draw_text():
    screen.draw.text(f'Level : {level}', (0,0), color = 'red')
    screen.draw.text(f'Score : {score}', (100,0), color = 'red')
    screen.draw.text(f'Lives : {lives}', (200,0), color = 'red')

def on_key_down(key):
    if key == keys.SPACE and len(bullets) < MAX_BULLETS:
        bullet = Actor('bullet', pos = (player.x, player.y))
        bullets.append(bullet)

def move_bullets():
    for bullet in  bullets:
        bullet.y -= 6
        if bullet.y < 0:
            bullets.remove(bullet)

def create_bombs():
    if random.randint(0, 100 - level * 6) == 0:
        enemy = random.choice(enemies)
        bomb = Actor('bomb', enemy.pos)
        bombs.append(bomb)
    
def move_bombs():
    global lives
    global game_over
    for bomb in bombs:
        bomb.y = bomb.y + 10
        if bomb.colliderect(player):
            bombs.remove(bomb)
            lives -= 1
            if lives == 0:
                game_over = True

def check_for_end_of_level():
    global level
    global win_over
    if len(enemies) == 0:
        level += 1
        create_enemies()
    if level > 3:
        win_over = True

def if_game_over():
    background3.draw()
    screen.draw.text('GAME OVER', center = (WIDTH//2, HEIGHT//2), color = 'yellow', fontsize = 100)
    screen.draw.text('BETTER LUCK NEXT TIME', center = (WIDTH//2, HEIGHT//2 + 60), color = 'yellow', fontsize = 60)

def if_win_over():
    background3.draw()
    screen.draw.text('WINNER', center = (WIDTH//2, HEIGHT//2), color = 'red', fontsize = 100)
    screen.draw.text('GAME OVER', center = (WIDTH//2, HEIGHT//2 + 60), color = 'red', fontsize = 60)

def if_game_start():
    background1.draw()
    screen.draw.text("HELLO GAMER!",center = (WIDTH//2, 100), color = 'white', fontsize = 100)
    screen.draw.text("YOU WANT TO PLAY.....",center = (WIDTH//2, 220), color = 'white', fontsize = 60)
    screen.draw.text("Press SPACE to continue........", center = (WIDTH//2, HEIGHT//2 + 220), color = 'red', fontsize = 30)

def started():
    screen.clear()
    background2.draw()
    player.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    for bomb in bombs:
        bomb.draw()
    draw_text()

pgzrun.go()

