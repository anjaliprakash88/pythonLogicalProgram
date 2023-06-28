import turtle

turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
colors = ["yellow", "red", "yellow", "red"]

for i in range(120):
    for c in colors:
        turtle.color(c)
        turtle.circle(200-i, 100)
        turtle.lt(90)  # Modified angle from 90 to 61
        turtle.circle(200-i, 100)
        turtle.rt(600)  # Modified angle from 600 to 121
        turtle.end_fill()

turtle.mainloop()
