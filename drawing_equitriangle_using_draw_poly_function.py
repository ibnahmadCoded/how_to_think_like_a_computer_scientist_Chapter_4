import turtle

def draw_poly(t, n, sz):
    for _ in range(n):
        t.forward(sz)
        t.left(360/n)

def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)


window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

draw_equitriangle(tess, 200)

window.mainloop()
