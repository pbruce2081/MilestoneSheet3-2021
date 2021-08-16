from user304_rsf8mD0BOQ_1 import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 400
HEIGHT = 400

IMG = simplegui.load_image('http://www.cs.rhul.ac.uk/courses/CS1830/sprites/coach_wheel-512.png')
IMG_CENTRE = (256, 256)
IMG_DIMS = (512, 512)

STEP = 0.5

# Global variables
img_dest_dim = (128,128)
#img_pos = [WIDTH/2, 2*HEIGHT/3.]
img_rot = 0

class Walls:
    def __init__(self, x, border, colour):
        self.x = x
        self.border = border
        self.colour = colour
        self.normal = Vector(1,0)
        self.edge_l = x + border
        self.edge_r = x + border
        
    def draw_l(self, canvas):
        canvas.draw_line((self.x, 0),
                         (self.x, HEIGHT),
                         2*self.border + 1,
                          self.colour)
            
    def draw_r(self, canvas):
        canvas.draw_line((self.x, 500),
                         (self.x, HEIGHT),
                         2*self.border + 1,
                          self.colour)
                      
    def hit_l(self, wheel):
        if self.x >= wheel.offset()[0]:
            return True
        return False
    
    def hit_r(self, wheel):
        if self.x <= wheel.offset()[0]:
            return True
        return False
                
class Wheel:
    def __init__(self, pos, radius=10):
        self.pos = pos
        self.vel = Vector()
        self.radius = max(radius, 10)
        self.colour = 'White'

    def draw(self, canvas):
        global img_rot
        img_rot += STEP
        canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, self.pos.get_p(), img_dest_dim, img_rot)
        
    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.5)
    
    def offset(self):
        return self.pos.get_p()
                                                         
    def wrap(self, x, y):
        self.pos = Vector(x, y)
    
class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False

class Interaction:
    def __init__(self, wheels, keyboard, wall_l, wall_r):
        self.wheels = wheels
        self.keyboard = keyboard
        self.wall_l = wall_l
        self.wall_r = wall_r
        
    def draw(self, canvas):
        self.update()
        self.wall = wall
        self.wheels = wheels

    def update(self):
        if self.keyboard.right:
            for wheel in self.wheels:
                wheel.vel.add(Vector(1, 0))
        if self.keyboard.left:
            for wheel in self.wheels:
                wheel.vel.add(Vector(-1, 0))
        for wheel in self.wheels:
            wheel.update()
            if self.wall_l.hit_l(wheel):
                wheel.wrap(749, HEIGHT - 40)
            elif self.wall_r.hit_r(wheel):
                wheel.wrap(-749, HEIGHT - 40)
                
wall_l = Walls(-750, 2*1, "Black")
wall_r = Walls(750, 2*1, "Black")
kbd = Keyboard()
wheel_1 = Wheel(Vector(WIDTH/2, HEIGHT-40), 40)
wheel_2 = Wheel(Vector(WIDTH/2 - 500, HEIGHT-40), 40)
wheel_3 = Wheel(Vector(WIDTH/2 + 500, HEIGHT-40), 40)
Wheels = []
Wheels.append(wheel_1)
Wheels.append(wheel_2)
Wheels.append(wheel_3)
inter = Interaction(Wheels, kbd, wall_l, wall_r)

def draw(canvas):
    inter.update()
    for wheel in Wheels:
        wheel.draw(canvas)

frame = simplegui.create_frame('Interactions', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_canvas_background('#2C6A6A')
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()