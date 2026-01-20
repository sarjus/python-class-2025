import turtle
count = 0
while(count < 360):
    turtle.forward(2)
    turtle.left(1)
    count = count + 1
count=0
turtle.right(180)
while(count < 360):
    turtle.back(2)
    turtle.right(1)
    count = count + 1
print("Finished!")
turtle.done()
