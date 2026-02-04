import turtle

# Create turtles
t = turtle.Turtle()
c = turtle.Turtle()

# First circle (Red)
t.fillcolor("red")
t.begin_fill()
t.circle(100)
t.end_fill()

# Move second turtle to center
c.penup()
c.goto(0, -20)
c.pendown()

# Second circle (Yellow)
c.fillcolor("yellow")
c.begin_fill()
c.circle(60)
c.end_fill()

turtle.done()
