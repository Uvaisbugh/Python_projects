from turtle import *
import random

# def draw_circles(t, size, num_circles):
#     for i in range(num_circles):
#         t.circle(size)
#         t.right(360 / num_circles)
        
# t1 = Turtle()
# t1.color('red')
# t1.width(5)

# t1.begin_fill()
# draw_circles(t1, 100, 6)
# t1.end_fill()

# done()

def project(t):
    for i in range(10):
        color = ['red','blue','green','yellow','orange','purple','black','pink','brown','cyan','magenta','grey']
        t.color(random.choice(color))
        t.width(5)
        
        t.up()
        random_x = random.randint(-200,200)
        random_y = random.randint(-200,200)
        t.goto(random_x,random_y)
        t.down()
        t.begin_fill()
        t.circle(random.randint(20,100))
        t.end_fill()
    done()
    
def project2(t,n):
    
    for i in range(n):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        colorx=(r/255,g/255,b/255)
        
        x=random.randint(-200,200)
        y=random.randint(-200,200)
        
        t.up()
        t.goto(x,y)
        t.down()
        
        t.color(colorx)
        t.begin_fill()
        for i in range(6):
            t.forward(100)
            t.right(60)
        t.end_fill()
    
    
t1 = Turtle()
project2(t1,10)
    
    
done()