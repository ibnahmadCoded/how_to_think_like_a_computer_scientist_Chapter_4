import turtle

def draw_spiral(animal, size):
        animal.forward(size)
        animal.right(90)

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")

tess.left(270)
size = 5


for _ in range(115):
    draw_spiral(tess, size)
    size += 2



window.mainloop()
