from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.color(99, 204, 250)
# leo.speed(50)
leo.pencolor("pink")
leo.fillcolor(32, 67, 93)

leo.penup()
leo.goto(0, 0)
leo.pendown()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()
leo.hideturtle()

done()