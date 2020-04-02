import turtle

def draw_spiral(animal, size):
        animal.forward(size)
        animal.right(89)

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")

size = 5
tess.left(270)

for _ in range(5):   
    tess.forward(size)
    tess.right(90)
    size += 2

for _ in range(118):
    draw_spiral(tess, size)
    size += 2



window.mainloop()
