import turtle

def draw_square(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)

    tess.penup()
    tess.forward(size * 2)
    tess.pendown()

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

for _ in range(5):
    draw_square(tess, 20)


window.mainloop()
