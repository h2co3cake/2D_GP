from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
coutn = 0

def draw(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)
    
while(1):

    while(x<800):
        draw(x,y)
        x=x+10

    while(y<600):
        draw(x,y)
        y=y+10

    while(0<x):
        draw(x,y)
        x=x-10

    while(90<y):
        draw(x,y)
        y=y-10

    x=400
    y=90

    while(y<290):
        draw(x,y)
        x=x+40
        y=y+40

    while(400<x):
        draw(x,y)
        x=x-40
        y=y+40

    while(290<y):
        draw(x,y)
        x=x-40
        y=y-40

    while(x<400):
        draw(x,y)
        x=x+40
        y=y-40

    x=0
    y=90
    
close_canvas()
