from user304_rsf8mD0BOQ_1 import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 500
HEIGHT = 500
CANVAS_DIMS = (WIDTH, HEIGHT)

IMG = simplegui.load_image('http://www.cs.rhul.ac.uk/courses/CS1830/sprites/coach_wheel-512.png')
IMG_CENTRE = (256, 256)
IMG_DIMS = (512, 512)

STEP = 0.45
Radius = 40
img_rot = 0
b = -2              
class Wheel:
    def __init__(self, pos, radius):
        self.pos = pos
        self.vel = Vector()
        self.radius = radius
        self.colour = 'White'

    def draw(self, canvas):
        global img_rot
        if kbd.right:
            img_rot -= STEP
        if kbd.left:
            img_rot += STEP
        canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, self.pos.get_p(), (self.radius*2,self.radius*2), img_rot)
                
    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.8)
        
    def on_ground(self):
        if self.pos.y == HEIGHT-Radius:
            return True
        return False
    
class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.space = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True
        if key == simplegui.KEY_MAP['space']:
            self.space = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['space']:
            self.space = False

class Interaction:
    def __init__(self, wheel, keyboard):
        self.wheel = wheel
        self.keyboard = keyboard

    def draw(self, canvas):
        self.update()
        self.wall = wall
        self.wheels = wheels

    def update(self):
        global b
        if self.keyboard.right:
            wheel.vel.add(Vector(1, 0))
        if self.keyboard.left:
            wheel.vel.add(Vector(-1, 0))
        if self.keyboard.space:
            if b < 0:
                wheel.vel.add(Vector(0, b))    


                
        wheel.update()
        if wheel.pos.y < HEIGHT-Radius:
            if b < 0:
                b += 0.07
            if b > 0:
                b += 0.11
            wheel.vel.add(Vector(0, b))
        if wheel.pos.y > HEIGHT-Radius:
            wheel.pos.y = HEIGHT-Radius
            b = -2   

kbd = Keyboard()
wheel = Wheel(Vector(WIDTH/2, HEIGHT-Radius), Radius)
inter = Interaction(wheel, kbd)

def draw(canvas):
    inter.update()
    wheel.draw(canvas)

frame = simplegui.create_frame('Interactions', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.set_canvas_background('#2C6A6A')
frame.start()