import turtle

def draw_star(animal, size):
    """
    Draws a star given the animal and the size of its sides.
    """
    animal.forward(100)
    animal.left(144)

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.hideturtle()
tess.pensize(3)
tess.color("hotpink")
tess.left(45)

for n in range(5):
    for _ in range(5):
        draw_star(tess, 100)
    tess.penup()
    tess.forward(350)
    tess.right(144)
    tess.pendown()
