import turtle

def draw_star(animal, size):
    """
    Draws a star given the animal and the size of its sides.
    """
    animal.forward(100)
    animal.left(144)

window = turtle.Screen()

tess = turtle.Turtle()
tess.hideturtle()
tess.pensize(3)
tess.left(45)

for _ in range(5):
    draw_star(tess, 100)
