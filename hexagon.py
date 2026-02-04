import turtle
hexagon = turtle.Turtle()
# executing loop 6 times for 6 sides
turtle.bgcolor("yellow")
hexagon.fillcolor("red")
hexagon.begin_fill()
for i in range(6):
	# Move forward by 90 units
	 hexagon.forward(90)
	# Turn left the turtle by 300 degrees
	 hexagon.left(300)
hexagon.end_fill()
turtle.done()