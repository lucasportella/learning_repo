import turtle
tutu = turtle.Turtle()
wn = turtle.Screen()
tutu.shape('turtle')
tutu.penup()
tutu.forward(100)
tutu.left(90)
tutu.pendown()
for c in range(360):
    tutu.left(1)
    tutu.forward(1)
wn.exitonclick()
