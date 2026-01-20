import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.hideturtle()
pen.color("cyan")
pen.penup()

while True:
    pen.clear()
    current_time = time.strftime("%H:%M:%S")
    pen.goto(0, 0)
    pen.write(current_time, align="center",
              font=("Arial", 48, "bold"))
    time.sleep(1)
