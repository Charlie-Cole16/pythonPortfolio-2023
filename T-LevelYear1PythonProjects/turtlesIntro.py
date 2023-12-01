import turtle
import time

Chaz = turtle.Turtle()

for i in range(350):
    Chaz.speed(25)
    Chaz.fd(i)
    Chaz.right(i)

Chaz.screen.mainloop()
