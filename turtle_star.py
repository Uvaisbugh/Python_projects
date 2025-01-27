from turtle import *

def draw_star(t, size):
    for i in range(5):
        t.forward(size)
        t.right(144)
        


t1 = Turtle()
t1.color('blue')
t1.width(5)

t1.begin_fill()
draw_star(t1, 100)
t1.end_fill()

done()

