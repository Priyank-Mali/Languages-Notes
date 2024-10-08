import turtle

# Set up screen
win = turtle.Screen()
win.bgcolor("white")

# Create turtle object
t = turtle.Turtle()
t.speed(1)

# Draw outer circle
t.penup()
t.goto(0, -100)
t.pendown()
t.color("blue")
t.begin_fill()
t.circle(100)
t.end_fill()

# Draw Django logo
t.penup()
t.goto(-50, 50)
t.pendown()
t.color("green")
t.begin_fill()
t.circle(20)
t.end_fill()

# Draw Python snake
t.penup()
t.goto(-70, 0)
t.pendown()
t.color("blue")
t.width(5)
t.goto(70, 0)

# Draw JavaScript code snippet
t.penup()
t.goto(-60, -20)
t.pendown()
t.color("yellow")
t.write("JS", font=("Arial", 16, "bold"))

# Draw React logo
t.penup()
t.goto(0, -50)
t.pendown()
t.color("blue")
t.begin_fill()
t.circle(10)
t.end_fill()

# Hide turtle object
t.hideturtle()

# Keep window open
turtle.done()