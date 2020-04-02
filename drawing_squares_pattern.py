import turtle

def draw_square(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

for _ in range(5):
    draw_square(tess, 200)
    tess.penup()
    tess.forward(30)
    tess.right(90)
    tess.forward(20)
    tess.left(105)
    tess.pendown()

#for _ in range(1):
    #tess.penup()
    #tess.left(45)
    #tess.forward(15)
    #tess.right(90)
    #tess.forward(15)
    #tess.left(45)
    #tess.pendown()
    #draw_square(tess, 200)


window.mainloop()
