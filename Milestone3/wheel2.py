from user304_rsf8mD0BOQ_1 import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 500
HEIGHT = 500

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
        canvas.draw_circle(self.pos.get_p(), self.radius, 1, self.colour, self.colour)
        
    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)
        
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
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()