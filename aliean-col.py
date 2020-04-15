WIDTH = 500
HEIGHT = 300
alien = Actor('alien',(50,150))
villan = Actor('p1_duck',(300,150))
show_villan = True
background=Actor('back',(0,0))
screencolor = 'black'
clickcount = 0
points = 0
def draw():
    screen.fill(screencolor)
    background.draw()
    alien.draw()
    if(show_villan==True):
        villan.draw()
    screen.draw.text(str(points),(400,50))

def move_alien():
    if(alien.x<WIDTH):
        alien.x = alien.x + 1
    else:
        alien.x = 0

def on_mouse_down(pos):
    global screencolor,clickcount

    if(clickcount==3):
        screencolor = 'green'
        clickcount=0
    else:
        screencolor='black'

    if(alien.collidepoint(pos)):
        set_alien_hurt()
    clickcount += 1

def set_alien_hurt():
    global screencolor
    screencolor = 'red'
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal,1)

def set_alien_normal():
    global screencolor
    screencolor = 'black'
    alien.image = 'alien'

def check_for_movement():
    global show_villan,points
    if(keyboard.right):
        alien.x = alien.x + 5
    elif(keyboard.left):
        alien.x = alien.x - 5
    elif(keyboard.up):
        alien_jump()

    print(alien.x,villan.x)

    if(alien.colliderect(villan)):
        show_villan=False
        points+=1

def alien_jump():
    move_alien_up()

def move_alien_up():
    alien.y = alien.y - 5
    clock.schedule(move_alien_down,0.5)

def move_alien_down():
    alien.y = alien.y + 5
    print("down")


def update():
    check_for_movement()