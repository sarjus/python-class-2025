'''
Draw a Right Angle Triangle using Turtle
'''
import math
import turtle
triangle = turtle.Turtle()
#draw base
triangle.forward(300)
triangle.left(90)
triangle.forward(300)
triangle.left(135)
c= math.sqrt(300**2+300**2)
triangle.forward(c)
turtle.done()