import turtle
import random
def art():
    win = turtle.Screen()
    win.bgcolor("BLACK")
    win.colormode(255)
    win.title("MINI_PROJ")
    t = turtle.Turtle()
    t.shape('arrow')
    t.color('BLACK')
    t.speed(0)
    for l in range(0,400):
          red = random.randint(0,255)
          blue = random.randint(0,255)
          green = random.randint(0,255)
          t.pencolor(red,blue,green)
          t.pendown()
          t.forward(l+50)
          t.right(91)
    win.exitonclick()
art()
    
