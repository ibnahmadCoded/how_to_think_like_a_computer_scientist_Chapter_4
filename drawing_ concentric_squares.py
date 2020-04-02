import turtle

def draw_square(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

size = 20
for _ in range(5):
    draw_square(tess, size)
    tess.penup()
    tess.left(90)
    tess.backward(10)
    tess.right(90)
    tess.backward(10)
    size += 20
    tess.pendown()


window.mainloop()
