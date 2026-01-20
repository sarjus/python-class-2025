import turtle

# Create turtle object
tree = turtle.Turtle()
tree.speed(0)
tree.left(90)        # Make the turtle face upward
tree.color("brown")
tree.width(2)

# Recursive function to draw the tree
def draw_tree(branch_length):
    if branch_length < 10:
        return

    tree.forward(branch_length)

    tree.left(30)
    draw_tree(branch_length - 15)

    tree.right(60)
    draw_tree(branch_length - 15)

    tree.left(30)
    tree.backward(branch_length)

# Move turtle to starting position
tree.penup()
tree.goto(0, -250)
tree.pendown()

# Draw the tree
draw_tree(100)

# Keep the window open
turtle.done()
