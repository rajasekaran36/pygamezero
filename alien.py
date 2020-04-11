WIDTH = 600
HEIGHT = 600
alien = Actor('alien',(50,200))
screencolor = 'black'
clickcount = 0
def draw():
    screen.fill(screencolor)
    alien.draw()

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

def update():
    move_alien()
